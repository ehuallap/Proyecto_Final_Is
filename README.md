# Proyecto_Final_Is
# Estilos de programación empleados
En este proyecto se emplearon los siguientes estilos de programación:
* Pipeline Style
* Kingdom of Nouns Style
* Persistent Tables Style
A continuación se muestra un ejemplo de cada estilo:
## Pipeline Style
```python
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
```
## Kingdom of Nouns Style
```python
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
    def __repr__(self):
        return "<Usuario('%s','%s','%s','%s')>" % (self.id, self.name, self.email, self.password)
    def __str__(self):
        return "Usuario [id=%s, name=%s, email=%s, password=%s]" % (self.id, self.name, self.email, self.password)
    def format(self):
        return {'id': self.id, 'name': self.name, 'email': self.email, 'password': self.password}
```
## Persistent Tables Style
```python
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
``` 