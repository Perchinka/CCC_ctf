from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_products(query=None):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    if query:
        cursor.execute(f"SELECT * FROM products WHERE name = '{query}'")
    else:
        cursor.execute("SELECT * FROM products LIMIT 3")

    results = cursor.fetchall()
    conn.close()

    # Convert results to a list of dictionaries
    products = [{'id': row[0], 'name': row[1], 'price': row[2], 'description': row[3]} for row in results]
    
    return products


@app.route('/')
def index():
    products = get_products()
    return render_template('index.html', products=products)


@app.route('/search')
def search():
    query = request.args.get('query')
    products = get_products(query)
    return render_template('search_results.html', products=products)

if __name__ == '__main__':
    app.run(debug=False, port=5000, host='0.0.0.0')