from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
     return "Version 3: Successfully deployed through automated Jenkins CI/CD Pipeline!"  
     # Testing automatic Jenkins build through GitHub webhook

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
