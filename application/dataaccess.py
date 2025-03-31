import mysql.connector


# Function to establish database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="signupdb"
    )


# Function to insert a member into the database
def add_member(firstname, lastname, email, society_name):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Fetch SocietyMembershipID based on SocietyName
    cursor.execute("SELECT SocietyMembershipID FROM society_ppf WHERE SocietyName = %s", (society_name,))
    society = cursor.fetchone()

    if not society:
        print("Error: Society does not exist.")
        return

    society_id = society[0]

    # Insert user details
    sql = "INSERT INTO sign_up_ppf (firstname, lastname, email, SocietyMembershipID) VALUES (%s, %s, %s, %s)"
    val = (firstname, lastname, email, society_id)
    cursor.execute(sql, val)

    conn.commit()
    print(f"{cursor.rowcount} record inserted.")

    cursor.close()
    conn.close()


# Function to retrieve all members
def get_members():
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = """SELECT s.MemberID, s.firstname, s.lastname, s.email, p.SocietyName
             FROM sign_up_ppf s
             JOIN society_ppf p ON s.SocietyMembershipID = p.SocietyMembershipID"""

    cursor.execute(sql)
    result_set = cursor.fetchall()

    members = []
    for member in result_set:
        members.append({
            'ID': member[0],
            'Firstname': member[1],
            'Lastname': member[2],
            'Email': member[3],
            'Society': member[4]
        })

    cursor.close()
    conn.close()
    return members


# Main function to insert a sample member
def main():
    add_member("Ross", "Geller", "gh@hj.com", "Eat and Retreat")
    print(get_members())


if __name__ == "__main__":
    main()


