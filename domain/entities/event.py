# Creacion de la clase Event
class Event:
    
    # Constructor de la clase
    def __init__(self, id=0, title="", theme="", description="", date_time="", platform="", access_link="", id_administrator=0):
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
    
    # Retorna el tema del evento
    def getTheme(self):
        return self.theme
    
    # Retorna la descripcion del evento
    def getDescription(self):
        return self.description
    
    # Retorna la fecha y hora del evento
    def getDateTime(self):
        return self.date_time
    
    # Retorna la plataforma del evento
    def getPlatform(self):
        return self.platform
    
    # Retorna el link de acceso al evento
    def getAccessLink(self):
        return self.access_link
    
    # Retorna el ID del administrador del evento
    def getIdAdministrator(self):
        return self.id_administrator
    
    # Asigna el valor del id del evento
    def setId(self, id):
        self.id = id
    
    # Asigna el valor del titulo del evento
    def setTitle(self, title):
        self.title = title
    
    # Asigna el valor del tema del evento
    def setTheme(self, theme):
        self.theme = theme
    
    # Asigna el valor de la descripcion del evento
    def setDescription(self, description):
        self.description = description
    
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
