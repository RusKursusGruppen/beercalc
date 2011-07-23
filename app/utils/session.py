# -*- coding: utf-8 -*-
from uuid import uuid4

sessions = dict()

class InvalidCookieException(Exception):
    pass

class Session(object):
    def __init__(self, id_):
        self.id = id_
        self.is_init = False
    
    def init(self):
        if self.is_init:
            return
        self.is_init = True
        if self.id != None:
            try:
                self.load_session()
                return
            except InvalidCookieException:
                pass
        self.new_session()
    
    def load_session(self):
        try:
            self.data = sessions[self.id]
        except IndexError:
            raise InvalidCookieException()
        
    def new_session(self):
        self.id = uuid4().hex
        self.data = dict()
    
    def get(self, *args, **kwargs):
        self.init()
        return self.data.get(*args,**kwargs)
    
    def __setitem__(self, *args, **kwargs):
        self.init()
        return self.data.__setitem__(*args, **kwargs)
    
    def set_cookie(self, response):
        if self.is_init:
            response.set_cookie("session", self.id, max_age=31536000)
