from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AWS Cloud Deployment</title>
    </head>
    <body>
        <h1>AWS Cloud Deployment</h1>
        <h2>Deployment Successful</h2>

        <p><strong>Application:</strong> Flask Web Server</p>
        <p><strong>Environment:</strong> Docker Container</p>
        <p><strong>Architecture:</strong> Nginx Reverse Proxy</p>

        <hr>

        <h3>Hello World!</h3>
        <p>Welcome to my AWS Docker Deployment project.</p>

        <p>Developed by <strong>YASH</strong></p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)