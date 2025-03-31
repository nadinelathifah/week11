
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="sign"
)


def main():
    print(mydb)

    cursor = mydb.cursor()
    cursor.execute("""
        SELECT SocietyID
        FROM society
        WHERE society_name ='Eat and Retreat Society'
        """)

    society_id = cursor.fetchone()

    if society_id is not None:
        society_id = society_id[0]

        sql = "INSERT INTO student (firstname, lastname, email, SocietyID) VALUES (%s, %s, %s,%s)"
        val = ('Ross', 'Geller', 'gh@hj.com', society_id)
        cursor.execute(sql, val)

        mydb.commit()

        print(cursor.rowcount, "record inserted.")
    else:
        raise ValueError('Society Not Found')


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

    sql = "INSERT INTO person (firstname, lastname, email, SocietyID) VALUES (%s, %s, %s, %s)"
    val = (firstname, lastname, email, SocietyID)
    cursor.execute(sql, val)

    conn.commit()
    print(f"Member {firstname} {lastname} was added.")


def get_member():
    conn = get_signupdb_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT
        s.firstname,
        s.lastname,
        s.email,
        soc.society_name
        FROM student as s
        INNER JOIN society as soc ON s.SocietyID = soc.SocietyID
        """)

    result_set = cursor.fetchall()
    member_list = []

    for member in result_set:
        member_list.append({
            'Student': member[0],
            'Firstname': member[1],
            'Lastname': member[2],
            'Email': member[3],
            'Society': member[4]
        })
    return member_list

if __name__ == "__main__":
    main()
