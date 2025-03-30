import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="signupDB"
)
def main():
    print(mydb)

    cursor = mydb.cursor()

    sql = "INSERT INTO person (firstname, lastname, email ) VALUES (%s, %s, %s)"
    val = ("Fred", "Flintstone", "abc@m.com")
    cursor.execute(sql, val)

    mydb.commit()

    print(cursor.rowcount, "record inserted.")


def get_db_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="signupDB"
    )
    return mydb



if __name__ == "__main__":
    main()
