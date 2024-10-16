from flask import Flask

app=Flask(__name__)

@app.route('/flask')
def hello_world():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Flask Basic</title>
</head>
<body>
    <h1>Flask Basic</h1>
    <p>Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself. Extensions exist for object-relational mappers, form validation, upload handling, various open authentication technologies and several common framework related tools. Extensions are updated far more regularly than the core Flask program.</p>
    </body>
</html>
    """

if __name__ == '__main__':
    app.debug=True
    app.run()