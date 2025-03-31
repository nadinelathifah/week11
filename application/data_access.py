
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="sign"
)


def get_signupdb_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sign"
    )
    return mydb


def add_member(firstname, lastname, email, SocietyID):
    conn = get_signupdb_connection()
    cursor = conn.cursor()

    sql = "INSERT INTO student (firstname, lastname, email, SocietyID) VALUES (%s, %s, %s, %s)"
    val = (firstname, lastname, email, SocietyID)
    cursor.execute(sql, val)

    conn.commit()
    print(f"Student, {firstname} {lastname}, was added.")


def get_member():
    conn = get_signupdb_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT
        s.MemberID,
        s.firstname,
        s.lastname,
        s.email,
        soc.society_name
        FROM student as s
        INNER JOIN society as soc ON s.SocietyID = soc.SocietyID
        """)

    result_set = cursor.fetchall()
    members = []

    for member in result_set:
        members.append({
            'MemberID': member[0],
            'firstname': member[1],
            'lastname': member[2],
            'email': member[3],
            'SocietyID': member[4]
        })
    return members



def main():
    print(mydb)

    cursor = mydb.cursor()
    cursor.execute("""
        SELECT SocietyID
        FROM society
        WHERE society_name ='Eat and Retreat Society'
        """)

    result_set = cursor.fetchone()

    if result_set != None:
        result_set = result_set[0]

        sql = """INSERT INTO student (
        firstname, 
        lastname, 
        email, 
        SocietyID) 
        VALUES (%s, %s, %s,%s)"""

        val = ('Ross', 'Geller', 'gh@hj.com', result_set)
        cursor.execute(sql, val)

        mydb.commit()

        print(cursor.rowcount, "record inserted.")
    else:
        raise ValueError('That society is unavailable at PPU campus, please enter a valid society.')


if __name__ == "__main__":
    main()
