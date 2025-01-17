# Proyecto final de publicacion de Eventos
## Propósito 
Este proyecto tiene todas las referencias de las practicas aprendidas en el trayecto del curso, el propósito del curso es elicitar, especificar las funcionalidades de cada fase para la construccion de este trabajo, estas fases fueron; analizar los requisitos de software y definir las especificaciones funcionales y no funcionales para el desarrollo de un sistema web que gestiona distintintos eventos y ponencias. 
Este sistema será utilizado por personal de la Escuela de Ciencia de la Computación e interesados del area.


## Tecnologias usadas
En el presente proyecto usamos HTML, CSS , Bootstrap; el gestor de Base de Datos se uso MySQL y SQLAlchemy, para la conexion de la Base de Datos y el frontend se usó Python (Flask) y Path (libreria incluida en Python que se utilizo para especificar las rutas y carpetas consultadas en todo el proyecto). 

## Funcionalidades
- Mostrar resumen general: El sistema debe mostrar información general sobre eventos de la Semana de la Computación, así como también algunos ponentes.
  <p align="center">
    <img src="Images/D_1.jpeg" width="25%">
  </p>

- Inicio de sesión de usuario: los usuarios deberán identificarse para poder inscribirse a los concursos organizados por la escuela.
   
- Registrar usuario: El sistema debe permitir al usuario registrarse. El sistema pedirá al usuario ingresar su correo electrónico institucional (si es que es estudiante de la UNSA) o personal (si es un usuario no relacionado con la UNSA) y contraseña.
   
- Visualizar evento: El sistema permite a los usuarios en general tener acceso a los eventos. No es necesario que se inicie sesión.
  - Mostrar información general: Se muestra el título, información del ponente, tema, fecha, hora, lugar o link del evento.
 
- Gestionar eventos: 
  - Publicar evento: El sistema permite al administrador crear un evento, dependiendo el tipo de evento, el sistema pedirá que ingresar la información general del evento : 
  - Presentación: Ingresar un título, nombre del ponente, tema, descripción,  fecha, hora, lugar o link del evento.
  - Editar Evento: Solo el administrador puede editar la información de un evento.  
  
  - Eliminar Evento:  Solo el administrador puede eliminar un evento.

## Estilos de Programación aplicados
* Pipeline Style: 
Esta enfocado en funciones que tienen un input y un output
```python
class Administrator_repository(DbConnection.Model, Administrator):
    tablename = 'administrator'
    id = DbConnection.Column(DbConnection.Integer, primary_key=True)

    def init(self, id=0, name="", email="", password=""):
        Administrator.init(self, id, name, email, password)

    def insert(self):
        try:
            DbConnection.session.add(self)
            DbConnection.session.commit()
        except Exception as e:
            print(e)
            DbConnection.session.rollback()
            return False
        return True

    def update(self):
        try:
            DbConnection.session.commit()
        except Exception as e:
            print(e)
            DbConnection.session.rollback()
            return False
        return True
```
* 	Cookbook Style: 
El sistema está diseñado de forma que pueda llamar las funciones secuencialmente.
```python
# Se importa Flask
from flask import Flask

import sys
from pathlib import Path

# Se importa el archivo de configuracion para el path
file = Path(file).resolve()
package_root = file.parents[1]
sys.path.append(str(package_root))

# se importa la conexion a la base de datos y los controladores de admin, event, participant, registered, speaker
from infrastructure.repository.db_connection import setup_db
from controllers.admin_controller import admin_blueprint
from controllers.event_controller import event_blueprint
from controllers.participant_controller import participant_blueprint
from controllers.registered_controller import registered_blueprint
from controllers.speaker_controller import speaker_blueprint

# Funcion principal para iniciar la aplicacion
def create_app():
    # Se crea la aplicacion Flask
    app = Flask(name)
    # Se registran los blueprints de la aplicacion (PARTE DEL PRINCIPIO SOLID OPEN CLOSED)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(event_blueprint)
    app.register_blueprint(participant_blueprint)
    app.register_blueprint(registered_blueprint)
    app.register_blueprint(speaker_blueprint)
    setup_db(app)
    return app
```
 
* Kingdom of Nouns Style: se crean clases para acceder a los atributos de las clases
  Esta sección muestra como se crean clases para acceder a los atributos de las clases. 
```python
# Creacion de la clase RegistredPerson
class Registered_person:
    # Constructor de la clase
    def init(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    # Metodo para obtener el id de la persona (ENCAPSULAMIENTO)
    def getId(self):
        return self.id

    # Metodo para obtener el nombre de la persona (ENCAPSULAMIENTO)
    def getName(self):
        return self.name

    # Metodo para obtener el email de la persona (ENCAPSULAMIENTO)
    def getEmail(self):
        return self.email

    # Metodo para obtener la contraseña de la persona (ENCAPSULAMIENTO)
    def getPassword(self):
        return self.password

    # Metodo para asignar el id de la persona (ENCAPSULAMIENTO)
    def setId(self, id):
        self.id = id

    # Metodo para asignar el nombre de la persona (ENCAPSULAMIENTO)
    def setName(self, name):
        self.name = name

    # Metodo para asignar el email de la persona (ENCAPSULAMIENTO)
    def setEmail(self, email):
        self.email = email
```
* Persistent Tables Style:
   Este Estilo esta dedicado a la información que se almacenan en bases de datos para mantener persistencia sobre los mismos.
```python
class Event_repository(DbConnection.Model, Event):
    tablename = 'event'
    id = DbConnection.Column(DbConnection.Integer, primary_key=True)
    title = DbConnection.Column(DbConnection.String(50), nullable=False)
    theme = DbConnection.Column(DbConnection.String(100), nullable=False)
    description = DbConnection.Column(DbConnection.String(100), nullable=False)
    date_time = DbConnection.Column(DbConnection.DateTime, nullable=False)
    platform = DbConnection.Column(DbConnection.String(20), nullable=False)
    access_link = DbConnection.Column(DbConnection.String(50), nullable=False)
    administrator_id = DbConnection.Column(DbConnection.Integer, nullable=False)

    def init(self, id=0, title="", theme="", description="", date_time="", platform="", access_link="", administrator_id=0):
        Event.init(self, id, title, theme, description, date_time, platform, access_link, administrator_id)

    def insert(self):
        try:
            DbConnection.session.add(self)
            DbConnection.session.commit()
        except Exception as e:
            print(e)
            DbConnection.session.rollback()
            return False
        return True

    def update(self):
        try:
            DbConnection.session.commit()
        except Exception as e:
            print(e)
            DbConnection.session.rollback()
            return False
        return True
```
## Practicas/Estandares/Convenciones
* Comentarios autoexplicativos: 
   Se comentan las líneas de código importante para entender el funcionamiento.
```python
# Dependencias de Flask y flask_cors
from flask import jsonify
from flask import request
from flask import abort
from flask import Blueprint
from flask_cors import cross_origin

# Se importa la clase del repositorio de Administrador
from infrastructure.repository.admin_repository import Administrator_repository

# Se registra el blueprint del Administrador, principio SOLID de OPEN CLOSED
admin_blueprint = Blueprint('admin_blueprint', name)
admin = Administrator_repository()

# Se crea la ruta para crear un Administrador, el metodo POST
@admin_blueprint.route('/admin', methods=['POST'])
@cross_origin()
def create_admin():
    # Se verifica que el request sea un JSON, si no es asi, se aborta con un 400 (PROGRAMACION DEFENSIVA)
    if not request.json:
        abort(400)
    # Se crea un objeto de la clase Administrador, con los datos del request
    admin = Administrator_repository(request.json['id'], request.json['name'], request.json['email'], request.json['password'])
    # Se inserta el objeto en la base de datos
    admin = admin.insert()
    # Se retorna el objeto creado
    return jsonify(admin)

# Se crea la ruta para obtener todos los Administradores, el metodo GET
@admin_blueprint.route('/admin', methods=['GET'])
@cross_origin()
def get_admins():
    # Se obtienen todos los Administradores de la base de datos
    admins = admin.get_all()
    # Se retornan los Administradores
    return jsonify(admins)
```
* Indentación consistente:
   Se respeta los espacios de indentación y se ordena para un facil entendimiento del usuario

```python
# Asigna el valor de la fecha y hora del evento
    def setDateTime(self, date_time):
        self.date_time = date_time

    # Asigna el valor de la plataforma del evento
    def setPlatform(self, platform):
        self.platform = platform

    # Asigna el valor del link de acceso al evento
    def setAccessLink(self, access_link):
        self.access_link = access_link

    # Asigna el valor del ID del administrador del evento
    def setIdAdministrator(self, id_administrator):
        self.id_administrator = id_administrator

    # Retorno un diccionario con los datos del evento, para convertirlo a JSON
    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'theme': self.theme,
            'description': self.description,
            'date_time': self.date_time,
            'platform': self.platform,
            'access_link': self.access_link,
            'id_administrator': self.id_administrator
        }
```
* Esquema consistente de Nombramiento:
Se nombran las variables según el formato impuesto por el lenguaje de programacion
```python
# Creacion de la clase Event
class Event:

    # Constructor de la clase
    def init(self, id=0, title="", theme="", description="", date_time="", platform="", access_link="", id_administrator=0):
        self.id = id
        self.title = title
        self.theme = theme
        self.description = description
        self.date_time = date_time
        self.platform = platform
        self.access_link = access_link
        self.id_administrator = id_administrator

    # Retorna el valor del id del evento
    def getId(self):
        return self.id

    # Retorna el valor del titulo del evento
    def getTitle(self):
        return self.title
```
* Evitar el anidamiento profundo:
Se utilizan funciones compactas que se combinan con la programación defensiva para hacer código facil de leer y consistente 
```python
def insert(self):
        try:
            DbConnection.session.add(self)
            DbConnection.session.commit()
        except Exception as e:
            print(e)
            DbConnection.session.rollback()
            return False
        return True

    def update(self):
        try:
            DbConnection.session.commit()
        except Exception as e:
            print(e)
            DbConnection.session.rollback()
            return False
        return True

    def delete(self):
        try:
            DbConnection.session.delete(self)
            DbConnection.session.commit()
        except Exception as e:
            print(e)
            DbConnection.session.rollback()
            return False
        return True
```
* Organización y correcto nombramiento de las carpetas
Se distribuyen las carpetas y archivos dentro de la estructura DDD (Domain Driven Design)
<p align="center">
    <img src="Images/Organizacion.png" width="20%">
  </p>

* Nombres significativos, se utilizan variables con nombres significativos
```python
# Creacion de la clase Participante
class Participant(Registered_person):
    # Constructor de la clase
    def init(self, id, name, email, password, universidad, ciclo):
        super().init(self, id, name, email, password)
        self.universidad = universidad
        self.ciclo = ciclo

    # Metodo para obtener la universidad de la persona (ENCAPSULAMIENTO)
    def getUniversidad(self):
        return self.universidad

    # Metodo para obtenter el ciclo de la persona (ENCAPSULAMIENTO)
    def getCiclo(self):
        return self.ciclo

    # Metodo para asignar la universidad de la persona (ENCAPSULAMIENTO)
    def setUniversidad(self, universidad):
        self.universidad = universidad

    # Metodo para obtener el ciclo de la persona (ENCAPSULAMIENTO)
    def setCiclo(self, ciclo):
        self.ciclo = ciclo

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'universidad': self.universidad,
            'ciclo': self.ciclo
        }
```
## Principios SOLID aplicados
* Single-responsability : 
  El principio de responsabilidad única ( SRP ) es un principio de programación de computadoras que establece que cada módulo , clase o función en un programa de computadora debe   tener responsabilidad sobre una sola parte de la funcionalidad de ese programa , y debe encapsular esa parte. Todo eso de la función módulo, clase o servicios deben estar alineados estrechamente con esa responsabilidad.
  
Se utilizan diversas clases que cumplen con diferentes funciones específicas cada una, por ejemplo en el siguiente código se presenta la clase ParticipantController que realiza los cambios en la base de datos:
```python
class Participant_repository(DbConnection.Model, Participant):
    tablename = 'participant'
    id = DbConnection.Column(DbConnection.Integer, primary_key=True)
    universidad = DbConnection.Column(DbConnection.String(50), nullable=False)
    ciclo = DbConnection.Column(DbConnection.Integer, nullable=False)

    def init(self, id=0, name="", email="", password="", universidad="", ciclo=0):
        Participant.init(self, id, name, email, password, universidad, ciclo)

    def insert(self):
        try:
            DbConnection.session.add(self)
            DbConnection.session.commit()
        except Exception as e:
            print(e)
            DbConnection.session.rollback()
            return False
        return True
 ```
Por otro lado, el modelo de Participant solamente almacena los datos para su posterior modificación, por lo que queda aislado de la conexión a la base de datos. A continuación se presenta el código:

```python
# Creacion de la clase Participante
class Participant(Registered_person):
    # Constructor de la clase
    def init(self, id, name, email, password, universidad, ciclo):
        super().init(self, id, name, email, password)
        self.universidad = universidad
        self.ciclo = ciclo

    # Metodo para obtener la universidad de la persona (ENCAPSULAMIENTO)
    def getUniversidad(self):
        return self.universidad

    # Metodo para obtenter el ciclo de la persona (ENCAPSULAMIENTO)
    def getCiclo(self):
        return self.ciclo

    # Metodo para asignar la universidad de la persona (ENCAPSULAMIENTO)
    def setUniversidad(self, universidad):
        self.universidad = universidad

    # Metodo para obtener el ciclo de la persona (ENCAPSULAMIENTO)
    def setCiclo(self, ciclo):
        self.ciclo = ciclo
```
* Open-Closed :
Se utilizan Blueprints para construir los endpoints progresivamente, estos endpoints pueden extenderse pero no modificar a los que ya existen. A continuación se presenta el código de ParticipantController:

```python
participant_blueprint = Blueprint('participant_blueprint', name)
participant = Participant_repository()

@participant_blueprint.route('/participant', methods=['POST'])
@cross_origin()
def create_participant():
    if not request.json:
        abort(400)
    participant = Participant_repository(request.json['id'], request.json['name'], request.json['email'], request.json['password'], request.json['universidad'], request.json['ciclo'])
    participant.insert()
    return jsonify(participant)

@participant_blueprint.route('/participant', methods=['GET'])
@cross_origin()
def get_participants():
    participants = participant.get_all()
    return jsonify(participants)

@participant_blueprint.route('/participant/<int:id>', methods=['GET'])
@cross_origin()
def get_participant(id):
    participant = participant.get(id)
    return jsonify(participant)
```
* Liskov-Sutitution:
  En el proyecto, se utiliza herencia para las clases de Participant, Speaker y Administrator para que pueda cumplir la mismas funciones de mostrar y cambiar datos, de la clase Padre RegisteredPerson.
```python
# Creacion de la clase RegistredPerson
class Registered_person:
    # Constructor de la clase
    def init(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    # Metodo para obtener el id de la persona (ENCAPSULAMIENTO)
    def getId(self):
        return self.id

    # Metodo para obtener el nombre de la persona (ENCAPSULAMIENTO)
    def getName(self):
        return self.name

    # Metodo para obtener el email de la persona (ENCAPSULAMIENTO)
    def getEmail(self):
        return self.email

    # Metodo para obtener la contraseña de la persona (ENCAPSULAMIENTO)
    def getPassword(self):
        return self.password

    # Metodo para asignar el id de la persona (ENCAPSULAMIENTO)
    def setId(self, id):
        self.id = id
Donde su clase hija es:
# Creacion de la clase Participante
class Participant(Registered_person):
    # Constructor de la clase
    def init(self, id, name, email, password, universidad, ciclo):
        Registered_person.init(self, id, name, email, password)
        self.universidad = universidad
        self.ciclo = ciclo
```
## Conceptos DDD aplicados

La estructura DDD se puede ver reflejado en la distribución de las carpetas y el modo en el que las clases interactuan entre si.

* En la parte de Domain, estamos declarando las clases que servirán como modelos para los metodos de get, set y format:
 
   <p align="center">
    <img src="Images/D_1.jpeg" width="25%">
  </p>

* En la parte de infraestructura se crea el esquema de la base de datos y las conexiones de cada Entidad a la base de datos: 

   <p align="center">
      <img src="Images/D_2.jpeg" width="25%">
       </p>
      
*  En la parte de presentation, se adjuntan los controladores de cada Entidad, que especifican las rutas de los endpoints y la interfaz que se muestra al usuario:

      <p align="center">
       <img src="Images/D_3.jpeg" width="25%">
      </p>
  
