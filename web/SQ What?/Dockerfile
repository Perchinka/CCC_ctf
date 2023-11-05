FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the challenge files into the container
COPY src /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose any necessary ports if your challenge requires network access
EXPOSE 5000

# Specify how to run your challenge (e.g., run a script or command)
CMD ["python", "app.py"]