# -*- coding: utf-8 -*-
from flask import Blueprint, request,json
from pusher import pusher

blueprint = Blueprint('guest', __name__)

@blueprint.route('/new/guest', methods=['POST'])
def guestUser():
        data = request.json
        pusher.trigger(u'general-channel', u'new-guest-details', { 
            'name' : data['name'], 
            'email' : data['email']
            })
        return json.dumps(data)