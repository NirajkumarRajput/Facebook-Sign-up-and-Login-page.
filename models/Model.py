import mysql.connector

class DB:
    def __init__(self):
        # Initialize attributes
        self.conn = None
        self.mycursor = None

        # Connect to the database
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='login_page'
            )
            self.mycursor = self.conn.cursor()
            print('Connection established')
        except mysql.connector.Error as error:
            print(f"Connection error: {error}")

    def insert_data(self, email_id,password,first_name,sur_name,gender,day,month,year):
        try:
            self.email_id = email_id
            self.password = password
            self.first_name = first_name
            self.sur_name = sur_name
            self.gender = gender
            self.day = day
            self.month = month
            self.year = year

            # Check if the email exists
            self.mycursor.execute("SELECT * FROM login WHERE email_id = %s", (self.email_id,))
            existing_data = self.mycursor.fetchall()

            if existing_data:
                # Email already exists, return an appropriate value (you can customize this)
                return 0
            else:
                # Email doesn't exist, insert the data
                sql_query = "INSERT INTO login (email_id, password, first_name, sur_name, gender, day, month, year) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                values = (self.email_id, self.password, self.first_name, self.sur_name, self.gender, self.day, self.month, self.year)
                self.mycursor.execute(sql_query, values)
                self.conn.commit()
                return 1

        except mysql.connector.Error as error:
            print(f"Error: {error}")
        finally:
            # Close the cursor in any case
            if self.mycursor:
                self.mycursor.close()

            # # Close the connection if it is open
            # if self.conn and self.conn.is_connected():
            #     self.conn.close()
    def search(self,email_id,password):
        try:
            self.email_id = email_id
            self.password = password
            self.mycursor.execute("SELECT * FROM login WHERE email_id = %s and password = %s", (self.email_id,self.password,))
            data = self.mycursor.fetchall()
            for i in data:
                if i[1] == self.email_id and i[2] == self.password:
                    return 1
                else:
                    return 0
        except mysql.connector.Error as error:
            print(f"Error: {error}")
        finally:
            # Close the cursor in any case
            if self.mycursor:
                self.mycursor.close()

            # # Close the connection if it is open
            # if self.conn and self.conn.is_connected():
            #     self.conn.close()

    def update(self,new_password,old_email):
        try:
            self.new_password = new_password
            self.old_email = old_email
            self.mycursor.execute("SELECT * FROM login WHERE email_id = %s",(self.old_email,))
            data = self.mycursor.fetchall()
            if not data:
                return 0
            else:
                for row in data:
                    user_id = row[0]
                    self.mycursor.execute("UPDATE login SET password = %s WHERE user_id = %s", (new_password, user_id))
                    self.conn.commit()
        except mysql.connector.Error as error:
            print(f"Error: {error}")
        finally:
            # Close the cursor in any case
            if self.mycursor:
                self.mycursor.close()

            # # Close the connection if it is open
            # if self.conn and self.conn.is_connected():
            #     self.conn.close()
    def delete_account(self,old_email):
        try:
            self.old_email = old_email
            self.mycursor.execute("SELECT * FROM login WHERE email_id = %s",(self.old_email,))
            data = self.mycursor.fetchall()
            self.mycursor.execute("SELECT user_id FROM login WHERE email_id = %s",(self.old_email,))
            user_id = self.mycursor.fetchone()
            if not data:
                return 0
            else:
                self.mycursor.execute("delete from login where user_id = %s",user_id)
                self.conn.commit()
                return 1
        except mysql.connector.Error as Error:
            print(f"Error:{Error}")     
        finally:
            if self.mycursor:
                self.mycursor.close()      





        

 


             



    