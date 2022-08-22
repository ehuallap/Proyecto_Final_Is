
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
