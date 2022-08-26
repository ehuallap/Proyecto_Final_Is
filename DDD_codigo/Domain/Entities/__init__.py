
class Persona():
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    def __repr__(self):
        return '{} {}'.format(self.name, self.email)
