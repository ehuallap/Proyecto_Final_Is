import sys
from pathlib import Path

file = Path(__file__).resolve()
package_root = file.parents[0]
sys.path.append(str(package_root))

from registered_person import Registered_person

# Creacion de la clase Administrator
class Administrator(Registered_person):
    # Constructor de la clase
    
    def __init__(self, id, name, email, password):
        Registered_person.__init__(self, id, name, email, password)
    
    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password
        }
