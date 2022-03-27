from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja
#Dojos Class Methods Page
#This defines Dojos
class Dojo:
    db= "dojos_and_ninjas_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

#This allows you to Select one Dojo, and show all associated Ninjas
    @classmethod
    def get_one_with_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        print (results)
        dojo = cls(results[0])
        for row in results:
            ninja = {
                "id": row["ninjas.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "age": row["age"],
                "created_at": row["ninjas.created_at"],
                "updated_at": row["ninjas.updated_at"]
            }
            dojo.ninjas.append(Ninja(ninja))
        return dojo

#This allows to shoe all dojos currently avaliable 
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.db).query_db(query)
        print(results)
        all_dojos = []
        for dict in results:
            all_dojos.append(cls(dict))
        return all_dojos

#This allows a new Dojo to save to the list
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        results = connectToMySQL(cls.db).query_db(query,data)
        return results