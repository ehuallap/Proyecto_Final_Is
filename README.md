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
# Practicas de programación legible empleadas
En este proyecto se emplearon las siguientes practicas de programación legible:
* Nombres de variables y funciones
* Comentarios
* Espacios en blanco
* Indentacion y alineacion
* Longitud de linea
A continuación se muestra un ejemplo de cada practica:
## Nombres de variables y funciones
```python
    # Dependencias de la aplicación
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy

    # Creacion del nombre y la conexion a la base de datos
    database_name = 'EventComp'
    database_path = 'postgres://{}/{}'.format('localhost:8085', database_name)
    database = SQLAlchemy()

    # Creacion de la funcion para crear la aplicacion
    def setup_db(app, database_path=database_path):
        app.config["SQLALCHEMY_DATABASE_URI"] = database_path   # Conexion a la base de datos
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False    # Desactivar el rastreo de modificaciones
        database.app = app                                      # Asignar la aplicacion a la base de datos
        database.init_app(app)                                  # Inicializar la base de datos
        database.create_all()                                   # Crear la base de datos
```
## Comentarios
```python
    class Administrador:
        # Constructor de la clase
        def __init__(self, id, name, email, password):
            self.id = id
            self.name = name
            self.email = email
            self.password = password
        
        # Metodo para representar el objeto en un diccionario
        def __repr__(self):
            return "<Administrador('%s','%s','%s','%s')>" % (self.id, self.name, self.email, self.password)
        
        # Metodo para representar el objeto en una tupla
        def __str__(self):
            return "Administrador [id=%s, name=%s, email=%s, password=%s]" % (self.id, self.name, self.email, self.password)
        
        # Metodo para verificar administradores repetidos
        def __eq__(self, other):
            return self.id == other.id
```
## Espacios en blanco
```python

    # Creacion de la clase EventoRepository
    class EventoRepository:
        
        # Constructor de la conexion a la base de datos
        def __init__(self, db):
            self.db = db
        
        # Metodo para obtener todos los eventos
        def getEventos(self):
            return self.db.eventos.find()
        
        # Metodo para obtener un evento por su id
        def getEvento(self, id):
            return self.db.eventos.find_one({'_id': id})
        
        # Metodo para agregar un evento
        def addEvento(self, evento):
            return self.db.eventos.insert_one(evento)
        
        # Metodo para actualizar evento por su id
        def updateEvento(self, id, evento):
            return self.db.eventos.update_one({'_id': id}, {'$set': evento})
        
        # Metodo para obtener los eventos por su nombre
        def deleteEvento(self, id):
            return self.db.eventos.delete_one({'_id': id})

```
## Indentacion y alineacion
```python
    # Metodo para asignar el email del administrador (ENCAPSULAMIENTO)
    def setEmail(self, email):
        self.email = email
    
    # Metodo para asignar el password del administrador (ENCAPSULAMIENTO)
    def setPassword(self, password):
        self.password = password
    
    # Metodo para obtener el objeto en formato JSON
    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password
            }
```
## Longitud de linea
```python
    # Metodo para agregar un ponente
    def addPonente(self, ponente):
        return self.db.ponentes.insert_one(ponente)
    
    # Metodo para actualizar ponente por su id
    def updatePonente(self, id, ponente):
        return self.db.ponentes.update_one(
            {'_id': id},
            {'$set': ponente}
            )
    
    # Metodo para obtener los ponentes por su nombre
    def deletePonente(self, id):
        return self.db.ponentes.delete_one(
            {'_id': id}
            )
```