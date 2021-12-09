from flask import Flask
from views import views

app = Flask(__name__)
#accessing the roots from "/"
app.register_blueprint(views, url_prefix="/")

if __name__ == '__main__':
    app.run(debug=False, port=8000)