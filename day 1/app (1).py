from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/getdetails')
def get_details():
    return 'Sarathy ram M-7376222AD194'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
