import logging

from config import Config

from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request

app_config = Config()
app = Flask(app_config.APP_NAME)


@app.route('/HTTP', methods=['GET', 'POST'])
def http_endpoint() -> str:
    # check for Accept header, if client wants json send it do them
    try:
        if request.headers['Accept'].lower() == "application/json":
            return jsonify({"message": "Good morning"})
    except KeyError:
        # No Accept header
        pass
    # otherwise, give them our html hello world
    return render_template('hello_world.html')


# for running in dev, using built in WSGI
if __name__ == '__main__':
    app.run(debug=app_config.DEBUG, use_reloader=False)

# for running in prod, behind gunicorn
if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
