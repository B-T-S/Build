from flask import Blueprint, request,json
from pusher import pusher

blueprint = Blueprint('pusherauth', __name__)
@blueprint.route("/pusher/auth", methods=['POST'])
def pusher_authentication():
        auth = pusher.authenticate(channel=request.form['channel_name'],socket_id=request.form['socket_id'])
        return json.dumps(auth)
