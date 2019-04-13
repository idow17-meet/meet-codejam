from flask import Flask, render_template, jsonify
import requests

from backend.api import api


class VueFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='[%',
        block_end_string='%]',
        variable_start_string='[[',
        variable_end_string=']]',
        comment_start_string='[#',
        comment_end_string='#]',
        ))


# Blueprints

app = VueFlask(__name__,
        static_folder='./dist/static',
        template_folder='./dist')

app.register_blueprint(api)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    if app.debug:
        return requests.get(f'http://localhost:8080/{path}').text
    return render_template("index.html")

