# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from pusher import pusher

blueprint = Blueprint('admin', __name__)
@blueprint.route('/admin')
def admin():
        return render_template('chat/admin.html')
