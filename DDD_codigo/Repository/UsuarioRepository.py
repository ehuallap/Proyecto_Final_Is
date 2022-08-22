#!/usr/bin/python
#-*- coding: utf-8 -*-

class UsuarioRepository:
    def __init__(self, db):
        self.db = db
    def getUsuarios(self):
        return self.db.usuarios.find()
    def getUsuario(self, id):
        return self.db.usuarios.find_one({'_id': id})
    def addUsuario(self, usuario):
        return self.db.usuarios.insert_one(usuario)
    def updateUsuario(self, id, usuario):
        return self.db.usuarios.update_one({'_id': id}, {'$set': usuario})
    def deleteUsuario(self, id):
        return self.db.usuarios.delete_one({'_id': id})
