import connect.connect1 as cc

class user2:
    def user_validate(self):
        accno= int(input("Enter Account No: "))
        Password=input("Enter Password: ")
        ob=cc.connect2()
        con=ob.conn()
        q="select * from cust_info where accno='%d' and Password='%s'"\
           %(accno,Password)
        stm=con.cursor()
        stm.execute(q)
        results=stm.fetchall()
        '''
        if your accno and password match then result store row wise empty
        '''
        t=0
        for r in results:
            t=1
            con.close()
            return t,accno
    def password_change(self, accno):
        opass=input("Enter old password: ")
        npass=input("Enter new password: ")
        ob=cc.connect2()
        con=ob.conn()
        q="update cust_info set password='%s' where accno='%d' and password='%s'"\
           %(npass,accno,opass)
        stm=con.cursor()
        stm.execute(q)
        con.commit()
        print("Password updated successfully.")
        con.close()
    def balance_check(self,accno):
         ob=cc.connect2()
         con=ob.conn()
         q="select bal from transaction where accno='%d' and tid=(select max(tid)from transaction where accno='%d')"%(accno,accno)
         stm=con.cursor()
         stm.execute(q)
         results=stm.fetchall()
         bal=0
         for r in results:
             bal=r[0]
         print("Yor balance is ",bal)
         con.close()
    def mini_stmt(self,accno):
         ob=cc.connect2()
         con=ob.conn()
         q="select * from transaction where accno='%d'"%(accno)
         stm=con.cursor()
         stm.execute(q)
         results=stm.fetchall()
         for r in results:
             print(r[2],r[3],r[4],r[5])
         con.close()
    def profile_view(self,accno):
         ob=cc.connect2()
         con=ob.conn()
         q="select * from cust_info where accno='%d'"%(accno)
         stm=con.cursor()
         stm.execute(q)
         results=stm.fetchall()
         for r in results:
             print("Name: ",r[1])
             print("Address: ",r[2])
             print("Phone Number: ",r[3])
             print("Email: ",r[4])
             print("Aadhar Id: ",r[5])
         con.close()   
    def user_menu(self):
         (t,accno)=self.user_validate()
         if t==0:
             print("Invalid Account No. or Password:")
         else:
             while True:
                 print("Welcome ",accno)
                 print("Press 1 for Password Change")
                 print("Press 2 for Balance Check")
                 print("Press 3 for Ministatement")
                 print("Press 4 to View Profile")
                 print("Press 5 to Exit")
                 ch=int(input("Enter your choice: "))
                 if ch==1:
                     self.password_change(accno)
                 elif ch==2:
                     self.balance_check(accno)
                 elif ch==3:
                     self.mini_stmt(accno)
                 elif ch==4:
                     self.profile_view(accno)
                 else:
                     break
                 
             
                         

    
