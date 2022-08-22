#!/usr/bin/python
#-*- coding: utf-8 -*-

class Usuario:
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
    def __repr__(self):
        return "<Usuario('%s','%s','%s','%s')>" % (self.id, self.name, self.email, self.password)
    def __str__(self):
        return "Usuario [id=%s, name=%s, email=%s, password=%s]" % (self.id, self.name, self.email, self.password)
    def __eq__(self, other):
        return self.id == other.id
    def getId(self):
        return self.id
    def getName(self):
        return self.name
    def getEmail(self):
        return self.email
    def getPassword(self):
        return self.password
    def setId(self, id):
        self.id = id
    def setName(self, name):
        self.name = name
    def setEmail(self, email):
        self.email = email
    def setPassword(self, password):
        self.password = password
    def format(self):
        return {'id': self.id, 'name': self.name, 'email': self.email, 'password': self.password}
