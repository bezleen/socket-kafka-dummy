from flask_socketio import Namespace
from flask_socketio import join_room, leave_room, rooms
from flask import request
import pydash as py_
import src.controllers as Controller
from src.extensions import socketio


class Dummy(Namespace):
    def __init__(self, namespace=None):
        self.namespace = namespace
        super().__init__(namespace)
        self.mmk_class = Controller.Dummy(namespace=self.namespace)

    def on_connect(self, *args, **kwargs):
        sid = request.sid
        join_room("public", sid=sid, namespace=self.namespace)
        # TODO: handle logic here
        return

    def on_disconnect(self):
        # TODO: handle logic here
        return
