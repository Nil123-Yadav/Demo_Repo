from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return '''
    <html>
        <head>
            <title>Welcome Page</title>
        </head>
        <body style="font-family: Arial, sans-serif;">
            <h1>🚀 Welcome to SAP BTP DevOps Training</h1>
            <p>This is a simple Python Flask app deployed on <strong>SAP BTP Cloud Foundry</strong>.</p>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

