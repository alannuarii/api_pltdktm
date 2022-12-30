from database.connection import conn, cur

class Unit:
    def get_units(self):
        cur.execute(f"SELECT * FROM apar")
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result