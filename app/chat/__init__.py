from app.controllers.home import blueprint
from flask import Blueprint

blueprint = Blueprint('chat', __name__)

from . import routes, events
