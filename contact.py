cbook={}
while(True):
 print()
 print("welcome to contact management system")
 print("choose from the following options")
 print("1.Add Contact")
 print("2.Search Contact")
 print("3.Update Contact")
 print("4.Delete Contact")
 print("5.Display Contacts")
 print("6.Exit")
 choice=int(input("Enter your choice"))
 if choice==1:
     name=input("Name")
     phone=int(input("Number"))
     cbook[name]=phone
     print("added")
 elif choice==2:
     name=input("search name")
     if name in cbook:
         print("found",cbook[name])
     else:
         print("Not found")
 elif choice==3:
     name=input("Updated")
     phone=int(input("number"))
     if name in cbook:
         cbook[name]=phone
         print("Updated")
     else:
             print("Not found")
 elif choice==4:
     name=input("Deleted name")
     if name in cbook:
         delcbook[name]
         print("deleted")
     else:
         print("Not Found")
 elif choice==5:
     for key,value in cbook.items():
         print(key,value)
 elif choice==6:
     print("exiting.....")
     break
 else:
     print("Invalid choice")
    
    
