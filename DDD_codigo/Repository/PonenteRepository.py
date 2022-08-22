
# Creacion de la clase PonenteRepository
class PonenteRepository:
    
    # Constructor de la conexion a la base de datos
    def __init__(self, db):
        self.db = db    # Conexion a la base de datos
    
    # Metodo para obtener todos los ponentes
    def getPonentes(self):
        return self.db.ponentes.find()
    
    # Metodo para obtener un ponente por su id
    def getPonente(self, id):
        return self.db.ponentes.find_one({'_id': id})
    
    # Metodo para agregar un ponente
    def addPonente(self, ponente):
        return self.db.ponentes.insert_one(ponente)
    
    # Metodo para actualizar ponente por su id
    def updatePonente(self, id, ponente):
        return self.db.ponentes.update_one(
            {'_id': id}, {'$set': ponente}
            )
    
    # Metodo para obtener los ponentes por su nombre
    def deletePonente(self, id):
        return self.db.ponentes.delete_one({'_id': id})
    
