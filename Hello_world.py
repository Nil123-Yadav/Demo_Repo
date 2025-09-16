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
            <h1>🚀 Welcome to SAP BTP App</h1>
            <p>This is a simple Python Flask app deployed on <strong>SAP BTP Cloud Foundry using load balancer</strong>.</p>
            <p> Tomorrow I will work on Kyma environment which is kuberneted based for microservice deployment.</p>
            <p> This application is single language based, tomorrow i will try to make multi language application and make them communicate using REST API and Event Mesh</p>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
