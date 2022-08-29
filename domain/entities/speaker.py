import sys
from pathlib import Path

file = Path(__file__).resolve()
package_root = file.parents[0]
sys.path.append(str(package_root))

from registered_person import Registered_person

# Creacion de la clase Speaker
class Speaker(Registered_person):    
    # Constructor de la clase
    def __init__(self, id, name, email, password, ac_level, description, especialty, phone):
        Registered_person.__init__(self, id, name, email, password)
        self.academic_level = ac_level
        self.description = description
        self.especialty = especialty
        self.phone = phone
    
    def getAcademicLevel(self):
        return self.academic_level
    
    def getDescription(self):
        return self.description
    
    def getEspecialty(self):
        return self.especialty
    
    def getPhone(self):
        return self.phone
    
    def setAcademicLevel(self, ac_level):
        self.academic_level = ac_level
    
    def setDescription(self, description):
        self.description = description
    
    def setEspecialty(self, especialty):
        self.especialty = especialty
    
    def setPhone(self, phone):
        self.phone = phone
    
    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'academic_level': self.academic_level,
            'description': self.description,
            'especialty': self.especialty,
            'phone': self.phone
        }
