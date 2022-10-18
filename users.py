from mysqlconnection import connectToMySQL

class User:
    
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data ['last_name']
        self.email = data ['email']
        self.created_at = data ['created_at']
        self.update_at = data ['update_at']

    @classmethod
    def guardar(cls, formulario ):
        query = "INSERT INTO users(first_name, last_name, email) VALUES ( %(first_name)s, %(last_name)s, %(email)s )" # Esto es una interpolación 
    # La interpolación interpreta un diccionario y a travez de eso le podemos dar le valor de la llave del diccionario,
    #  esto evita que personas maliciosas entren a la base de datos 
        result = connectToMySQL('esquema_usuarios').query_db(query, formulario)
        return result   
