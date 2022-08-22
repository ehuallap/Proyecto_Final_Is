#!/usr/bin/python
#-*- coding: utf-8 -*-

class EventoRepository:
    DATABASE = 'DDD_codigo/Database/Eventos.db'
    TABLE = 'Eventos'
    def __init__(self):
        self.connection = sqlite3.connect(self.DATABASE)
        self.cursor = self.connection.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS %s (id INTEGER PRIMARY KEY, name TEXT, description TEXT, date TEXT, time TEXT, place TEXT, price TEXT, capacity TEXT, image TEXT)' % self.TABLE)
        self.connection.commit()
    def insert(self, evento):
        self.cursor.execute('INSERT INTO %s (name, description, date, time, place, price, capacity, image) VALUES (?, ?, ?, ?, ?, ?, ?, ?)' % self.TABLE, (evento.getName(), evento.getDescription(), evento.getDate(), evento.getTime(), evento.getPlace(), evento.getPrice(), evento.getCapacity(), evento.getImage()))
        self.connection.commit()
        return self.cursor.lastrowid
    def update(self, evento):
        self.cursor.execute('UPDATE %s SET name=?, description=?, date=?, time=?, place=?, price=?, capacity=?, image=? WHERE id=?' % self.TABLE, (evento.getName(), evento.getDescription(), evento.getDate(), evento.getTime(), evento.getPlace(), evento.getPrice(), evento.getCapacity(), evento.getImage(), evento.getId()))
        self.connection.commit()
    def delete(self, id):
        self.cursor.execute('DELETE FROM %s WHERE id=?' % self.TABLE, (id,))
        self.connection.commit()
