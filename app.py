import logging
from typing import List

from config import Config

from flask import Flask
from flask import jsonify
from flask import request

app_config = Config()
app = Flask(app_config.APP_NAME)

def json_response(messages: List[str]) -> str:
    return jsonify({"msgs": messages})

def plain_response(messages: List[str]) -> str:
    return "\n".join(messages)

def get_greeting(language: str = "en") -> str:
    """
    returns an appropriate greeting based on language
    i.e. en returns Hello
    es returns Hola
    """
    # for now only implements two languages, es and en. en is our default
    if language.lower() == "es":
        return "Hola"
    return "Hello"

@app.route('/<string:person_name>', methods=['GET'])
def hello(person_name: str) -> str:
    greeting = get_greeting(request.args.get("lang", "en"))
    # check for Accept header, if client wants json send it do them
    try:
        if request.headers['Accept'].lower() == "application/json":
            return json_response([f"{greeting} {person_name}!"])
    except KeyError:
        # No Accept header
        pass
    # otherwise, give them our html hello world
    return plain_response([f"{greeting} {person_name}!"])


# for running in dev, using built in WSGI
if __name__ == '__main__':
    app.run(debug=app_config.DEBUG, use_reloader=False)

# for running in prod, behind gunicorn
if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
