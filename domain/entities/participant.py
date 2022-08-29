import sys
from pathlib import Path

file = Path(__file__).resolve()
package_root = file.parents[0]
sys.path.append(str(package_root))

from registered_person import Registered_person

# Creacion de la clase Participante
class Participant(Registered_person):
    # Constructor de la clase    
    def __init__(self, id, name, email, password, universidad, ciclo):
        Registered_person.__init__(self, id, name, email, password)
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
    