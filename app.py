from flask import Flask
from rgz import rgz

app = Flask(__name__)

app.register_blueprint(rgz)
from flask import Flask, redirect, url_for, render_template
from rgz import rgz