import connect.connect1 as cc


class Adminf:
    def validate(self):
        userid=input("Enter User ID: ")
        passwd=input("Enter Password: ")
        if userid=="admin" and passwd=="123456":
            return 1
        else:
            return 0
    def create_newaccount(self):
        accno=int(input("Enter New Account No: "))
        name=input("Enter Name: ")
        address=input("Enter Address: ")
        phno=input("Enter Phone Number: ")
        email=input("Enter Email ID: ")
        aadhaar=input("Enter Aadhaar ID: ")
        password=input("Enter Password: ")
        amt=int(input("Enter Initial Amount: "))
        dt=input("Enter Date: ")
        ob=cc.connect2() #create an object of connect2 class
        con=ob.conn()     #call conn() method for connection
        q="insert into cust_info values('%d','%s','%s','%s','%s','%s','%s')"\
           %(accno,name,address,phno,email,aadhaar,password)#to create a query
        stm=con.cursor()#cursor() is a predefined method used as carrier
                        #between python and mysql
        stm.execute(q) #execute a query
        con.commit()   #save the data into the database

        tid=1
        deposit=amt
        withdrawl=0
        bal=amt
        q1="insert into transaction values('%d','%d','%s','%d','%d','%d')"\
           %(accno,tid,dt,deposit,withdrawl,bal)
        stm.execute(q1)
        con.commit()
        print("Acoount created successfully.")
        con.close()#close the connection
        
    def deposit(self):
        accno=int(input("Enter Account No: "))
        damt=int(input("Enter Deposit Amount: "))
        dt=input("Enter Date: ")
        ob=cc.connect2()
        con=ob.conn()
        q="select tid,bal from transaction where accno='%d' and tid=(select max(tid) from transaction where accno='%d')"\
           %(accno,accno)
        stm=con.cursor()
        stm.execute(q)
        '''
        results=
        tid  bal
         1    8000
        '''
        results=stm.fetchall() #fetchAll() is predefined method used to
                               #fetch the data from database and
                               #store it in results variable
        (tid,bal)=(0,0)
        for r in results:
            tid=r[0]
            bal=r[1]
        tid=tid+1
        deposit=damt
        withdrawl=0
        bal=bal+damt

        q1="insert into transaction values('%d','%d','%s','%d','%d','%d')"\
            %(accno,tid,dt,deposit,withdrawl,bal)
        stm.execute(q1)
        con.commit()
        print("Deposited successfully! Your current balance is: ",bal)
        con.close()
    def withdrawl(self):
        accno=int(input("Enter Account No: "))
        wamt=int(input("Enter Withdrawl Amount: "))
        dt=input("Enter Date: ")
        ob=cc.connect2()
        con=ob.conn()
        q="select tid,bal from transaction where accno='%d' and tid=(select max(tid) from transaction where accno='%d')"\
           %(accno,accno)
        stm=con.cursor()
        stm.execute(q)
        '''
        results=
        tid  bal
      r=[ 1    8000]
        '''
        results=stm.fetchall() #fetchAll() is predefined method used to
                               #fetch the data from database and
                               #store it in results variable
        (tid,bal)=(0,0)
        for r in results:
            tid=r[0]
            bal=r[1]
        tid=tid+1
        deposit=0
        if wamt>bal:
            print("Sorry, withdrawl not possible. You do not have enough balance in your account.")
        else:
            withdrawl=wamt
            bal=bal-wamt
            q1="insert into transaction values('%d','%d','%s','%d','%d','%d')"\
            %(accno,tid,dt,deposit,withdrawl,bal)
            stm.execute(q1)
            con.commit()
            print("Withdrawl successfully! Your current balance is: ",bal)
        con.close()
    def balance_check(self):
        accno=int(input("Enter Account No: "))
        ob=cc.connect2()
        con=ob.conn()
        q="select tid,bal from transaction where accno='%d' and tid=(select max(tid) from transaction where accno='%d')"\
           %(accno,accno)
        stm=con.cursor()
        stm.execute(q)
        '''
        results=
        tid  bal
      r=[ 1    8000]
        '''
        results=stm.fetchall() #fetchAll() is predefined method used to
                               #fetch the data from database and
                               #store it in results variable
        (tid,bal)=(0,0)
        for r in results:
            tid=r[0]
            bal=r[1]
        print("Your Balance is: ",bal)
        con.close()
    def ministmt(self):
        accno=int(input("Enter Account No: "))
        ob=cc.connect2()
        con=ob.conn()
        q="select * from transaction where accno='%d'"%(accno)
        stm=con.cursor()
        stm.execute(q)
        results=stm.fetchall()
        '''
        accno      tid        dt    deposit    withdrwal   bal
     r=   1              1     4/7    8000        0         8000
        1              2         .. 2000       0        10000
        ....
        
         '''
        for r in results:
            print(r[1],r[2],r[3],r[4],r[5])
        con.close()
    def admin_menu(self):
        t=self.validate()
        if t==0:
            print("Invalid User ID or Password.")
        else:
            while True:
                print("Press 1 to Create New Account")
                print("Press 2 to Deposit")
                print("Press 3 for Withdrawl")
                print("Press 4 to Check Balance")
                print("Press 5 for Ministatement")
                print("Press 6 to Exit")
                ch=int(input("Enter your choice: "))
                if ch==1:
                    self.create_newaccount()
                elif ch==2:
                    self.deposit()
                elif ch==3:
                    self.withdrawl()
                elif ch==4:
                    self.balance_check()
                elif ch==5:
                    self.ministmt()
                elif ch==6:
                    break







                
                
                
