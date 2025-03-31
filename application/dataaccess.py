
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="signupdb"
)


def main():
    print(mydb)

    cursor = mydb.cursor()

    sql = "INSERT INTO sign_up_ppf (firstname, lastname, email, SocietyName) VALUES (%s, %s, %s,%s)"
    val = ('Ross', 'Geller', 'gh@hj.com', 'Eat and Retreat Society');
    cursor.execute(sql, val)

    mydb.commit()

    print(cursor.rowcount, "record inserted.")


def get_ppgirls_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="signupdb"
    )

    return mydb


def add_member(firstname, lastname, email,societymembershipID ):
    conn = get_ppgirls_connection()
    cursor = conn.cursor()

    sql = "INSERT INTO person (firstname, lastname, email, SocietyName) VALUES (%s, %s, %s, %s)"
    val = (firstname, lastname, email, societymembershipID)
    cursor.execute(sql, val)

    conn.commit()


def get_member():
    conn = get_ppgirls_connection()
    cursor = conn.cursor()

    sql = "Select ID, Firstname, Lastname, email and SocietyName from person"
    cursor.execute(sql)

    result_set = cursor.fetchall()
    member_list = []
    for member in result_set:
        member.append({'ID': member[0], 'Firstname': member[1], 'Lastname': member[2], 'email': member[3],'Society Name': member[4] })
    return member_list


if __name__ == "__main__":
    main()
