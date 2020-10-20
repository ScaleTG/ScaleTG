from json import loads
from json import dumps

class Auth:
    def __init__(self, path='authorized.conf.json'):
        self.path = path
        try:
            with open(path, 'r') as file:
                self.obj = loads(file.read())
        except FileNotFoundError:
            self.obj = []

    def isAuthorized(self, user_id):
        return user_id in self.obj

    def addAuthorized(self, user_id):
        if user_id not in self.obj:
            self.obj.append(user_id)
            self._writeToConfig()
        return self

    def removeAuthorized(self, user_id):
        if user_id in self.obj:
            self.obj.remove(user_id)
        self._writeToConfig()
        return self
    
    def getAllAuthorized(self):
        return self.obj
    
    def _writeToConfig(self):
        with open(self.path, 'w+') as file:
            file.write(dumps(self.obj))
