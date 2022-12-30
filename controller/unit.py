from database.connection import connection

class Unit:

    def get_units(self):
        query = f"SELECT * FROM apar"
        result = connection(query)
        return result
