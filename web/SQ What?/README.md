# SQ What?
Category: **web**

---
## Description
```
Our agent has gained access to the internal robot database, but cannot find the key. Help him with this

It might be useful for you to know that the agent has figured out the language that the robots use, they call it **SQL**
```

---
## Solution
Having opened the link, we see a site with a sign. Having tried to ask several queries, we understand that to create a table, an SQL query like ```SELECT * FROM table WHERE name='our data'``` is used. So we can use SQL injection attack to show the entire contents of the table.

Use payload: ```' OR 1=1 -- -```

The result query will look like this: ```SELECT * FROM table WHERE name = '' OR 1=1 -- -'```

You can read more at https://portswigger.net/web-security/sql-injection about how SQL injections works

---
The flag is: ```CCC{5Ql_1s_FuN!}```
