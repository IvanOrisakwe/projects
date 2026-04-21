import mysql.connector
from user import User

class DB:
    """
    Handles all MySQL operations for the user database.
    """

    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="Ivan",
            password="Ivan", 
            database="pankki"
        )
        self.cursor = self.conn.cursor()

    def fetch_users(self):
        self.cursor.execute("SELECT * FROM kayttajat")
        return self.cursor.fetchall()

    def insert_user(self, user):
        sql = "INSERT INTO kayttajat (nimi, ika, sukupuoli, varat) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, user.to_tuple())
        self.conn.commit()

    def update_user(self, id, user):
        sql = "UPDATE kayttajat SET nimi=%s, ika=%s, sukupuoli=%s, varat=%s WHERE id=%s"
        self.cursor.execute(sql, (*user.to_tuple(), id))
        self.conn.commit()

    def delete_user(self, id):
        self.cursor.execute("DELETE FROM kayttajat WHERE id=%s", (id,))
        self.conn.commit()
