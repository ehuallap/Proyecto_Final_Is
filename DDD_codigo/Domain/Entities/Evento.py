#!/usr/bin/python
#-*- coding: utf-8 -*-

class Evento:
    def __init__(self, id, name, date, description, place, price, image, id_admin):
        self.id = id
        self.name = name
        self.date = date
        self.description = description
        self.place = place
        self.price = price
        self.image = image
        self.id_admin = id_admin
    def __repr__(self):
        return "<Evento('%s','%s','%s','%s','%s','%s','%s','%s')>" % (self.id, self.name, self.date, self.description, self.place, self.price, self.image, self.id_admin)
    def __str__(self):
        return "Evento [id=%s, name=%s, date=%s, description=%s, place=%s, price=%s, image=%s, id_admin=%s]" % (self.id, self.name, self.date, self.description, self.place, self.price, self.image, self.id_admin)
    def __eq__(self, other):
        return self.id == other.id
    def getId(self):
        return self.id
    def getName(self):
        return self.name
    def getDate(self):
        return self.date
    def getDescription(self):
        return self.description
    def getPlace(self):
        return self.place
    def getPrice(self):
        return self.price
    def getImage(self):
        return self.image
    def getId_admin(self):
        return self.id_admin
    def setId(self, id):
        self.id = id
    def setName(self, name):
        self.name = name
    def setDate(self, date):
        self.date = date
    def setDescription(self, description):
        self.description = description
    def setPlace(self, place):
        self.place = place
    def setPrice(self, price):
        self.price = price
    def setImage(self, image):
        self.image = image
    def setId_admin(self, id_admin):
        self.id_admin = id_admin
    def format(self):
        return {'id': self.id, 'name': self.name, 'date': self.date, 'description': self.description, 'place': self.place, 'price': self.price, 'image': self.image, 'id_admin': self.id_admin}
