#!/usr/bin/python
#-*- coding: utf-8 -*-

class PonenteRepository:
    def __init__(self, db):
        self.db = db
    def getPonentes(self):
        return self.db.ponentes.find()
    def getPonente(self, id):
        return self.db.ponentes.find_one({'_id': id})
    def addPonente(self, ponente):
        return self.db.ponentes.insert_one(ponente)
    def updatePonente(self, id, ponente):
        return self.db.ponentes.update_one({'_id': id}, {'$set': ponente})
    def deletePonente(self, id):
        return self.db.ponentes.delete_one({'_id': id})
    
