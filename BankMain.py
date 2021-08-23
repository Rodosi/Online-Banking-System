import Admin.Admin1 as aa
import user.user1 as uu


print("Welcome to ABCD Bank")
while True:
    print("\nPress 1 for Admin\nPress 2 for Customer\nPress 3 to Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        ob=aa.Adminf()
        ob.admin_menu()
    elif ch==2:
        ob1=uu.user2()
        ob1.user_menu()
    else:
        break
