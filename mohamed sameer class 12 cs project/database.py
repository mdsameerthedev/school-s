import mysql.connector as mysql

class database:
    def __init__(self,username,password):
            self.usname = username
            self.psswd = password
            self.con = mysql.connect(host='localhost',username=self.usname,password=self.psswd)
            self.cursor = self.con.cursor()
    def connected(self):
        con = self.con
        if con.is_connected():
             print('DataBase Connected Successfully!')
        else:
            print('DataBase Connection Failed!')



