# Creacion de la clase RegistredPerson
class Registered_person:   
    # Constructor de la clase
    def __init__(self, id, name, email, password):
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
    
    # Metodo para asignar la contraseña de la persona (ENCAPSULAMIENTO)
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
    