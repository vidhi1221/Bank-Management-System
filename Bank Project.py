class Customer():
    def __init__(s,name,email,contact,adhar,password):
        s.name=name
        s.email=email
        s.contact=contact
        s.adhar=adhar
        s.balance=0
        s.accno=adhar*3-2
        s.password=password
        print('Your Account No : ',s.accno)
        
    def __str__(s):
        
        return s.name+"    "+s.email+'    '+s.contact+'    '+str(s.adhar)+'  '+str(s.balance)+'  '+str(s.accno)

class Bank():
    blist=[]
    def __init__(s):
        
        s.execute()
        
    def login(s):
        print('____________________________________XXX_________________________________')
        acc=int(input("Enter Your Account Number : "))
        password=input("Enter Your  Pasword : ")
        for i in s.blist:
            if i.accno==acc and i.password==password:
                print("Loged In Successfully")
                print('____________________________________XXX_________________________________')
                b=1
                while(b>0):
                    print('Enter 1 For Customer Details : ')
                    print('Enter 2 For Deposit : ')
                    print('Enter 3 For Withdraw : ')
                    print('Enter 4 For Balance : ')
                    print('Enter 5 For Exit : ')
                    print('____________________________________XXX_________________________________')
                    num=int(input('Enter Number :'))
                    if num==1:
                        print(i)
                        print('=====================================================')
                    elif num==2:
                        print('=====================================================')
                        depoamt=int(input('Enter Amount For Deposit :'))
            
                        i.balance=i.balance+depoamt
                        print('=====================================================')
                        print(depoamt,'Deposited Successfully')
                        print('=====================================================')
                    elif num==3:
                        widamt=int(input('Enter Amount For Withdraw :'))
                        i.balance=i.balance-widamt
                        print('=====================================================')
                        print(widamt,'Withdrawed Successfully')
                        print('=====================================================')
                    elif num==4:
                        print('=====================================================')
                        if i.balance>0:
                            print('Your Balance :', i.balance)
                        else:
                            i.balance=0
                            print("Your Balance:",i.balance)
                                
                    elif num==5:
                        b=0
                    



        else:
            print('Please Enter Valid Credentials')
            

        
    def execute(s):
        a=1
        
        while(a>0):
            print('Enter 1 For Add Customer :')
            print('Enter 2 For Log in :')
            print('Enter 3 Exit :')
            print('=====================================================')
            z=int(input('Enter Number :'))
            print('=====================================================')
            if z==1:
                name=input('Enter Name :')
                email=input('Enter Email :')
                contact=input('Enter Contact :')
                adhar=int(input('Enter Adhar Number :'))
                password=input('Enter Password :')
                c=Customer(name,email,contact,adhar,password)
                s.blist.append(c)
                print('Customer Details Added Successfully')
                print('=====================================================')


            elif z==2:
                s.login()

            elif z==3:
                a=0

            

b=Bank()









    
        
