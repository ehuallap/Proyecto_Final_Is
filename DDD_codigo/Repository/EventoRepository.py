#!/usr/bin/python
#-*- coding: utf-8 -*-

class EventoRepository:
    def __init__(self, db):
        self.db = db
    def getEventos(self):
        return self.db.eventos.find()
    def getEvento(self, id):
        return self.db.eventos.find_one({'_id': id})
    def addEvento(self, evento):
        return self.db.eventos.insert_one(evento)
    def updateEvento(self, id, evento):
        return self.db.eventos.update_one({'_id': id}, {'$set': evento})
    def deleteEvento(self, id):
        return self.db.eventos.delete_one({'_id': id})
    
