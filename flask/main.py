import flask
from flask import Flask
from blog.api import blog_router

app = flask.Flask(__name__)
app.register_blueprint(blog_router)
if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
