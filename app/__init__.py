from flask import Flask
import logging

app = Flask(__name__)

from app import routes, models

# Setup console logging
if not app.debug:
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    app.logger.addHandler(stream_handler)

app.logger.setLevel(logging.INFO)
app.logger.info('Flask App startup')