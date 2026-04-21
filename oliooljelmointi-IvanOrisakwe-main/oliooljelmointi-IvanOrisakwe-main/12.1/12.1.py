import mysql.connector
import random

# Database connection settings
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "" 
DB_NAME = "testikanta"  # database name from the SQL file

# Name pools
first_names = ["Lauri", "Anna", "Mikko", "Tiina", "Oskari", "Sanna", "Ville", "Liisa", "Antti", "Kaisa",
               "Juha", "Elina", "Jari", "Maria", "Eero"]
last_names = ["Virtanen", "Korhonen", "Mäkinen", "Nieminen", "Hämäläinen", "Laine", "Heikkinen", "Koski",
              "Järvinen", "Lehtonen", "Saarinen", "Salminen", "Heinonen", "Turunen", "Seppälä"]

genders = ["Male", "Female"]

# User class
class User:
    def __init__(self, first, last, age, gender):
        self.name = f"{first} {last}"
        self.age = age
        self.gender = gender

    def add_to_db(self, conn):
        cursor = conn.cursor()
        sql = "INSERT INTO kayttajat (nimi, ika, sukupuoli) VALUES (%s, %s, %s)"
        cursor.execute(sql, (self.name, self.age, self.gender))
        conn.commit()
        cursor.close()

# Function to create a random user
def create_random_user():
    first = random.choice(first_names)
    last = random.choice(last_names)
    age = random.randint(18, 65)
    gender = random.choice(genders)
    return User(first, last, age, gender)

# Main program
def main():
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

    for _ in range(20):
        user = create_random_user()
        user.add_to_db(conn)

    conn.close()
    print("20 random users added to kayttajat table.")

if __name__ == "__main__":
    main()
