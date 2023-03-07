

print("=" * 30)

CustomerNames = ["john", "json", "robo", "lobo", "don", "sunny", "jordan", "smith"]
CustomerPins = ["2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013"]
CustomerBalances = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]
deposition = 0
Withdrawal = 0
Balance = 0
CheckbookNames = [CustomerNames]
AtmCardPins =[CustomerPins]
Counter_1 = 0
Counter_2 = 0
i = 0
while True:
    print("-----------------------------------------")
    print("  --- WELCOME TO STATE BANK OF INDIA ---  ")
    print("*****************************************")
    print(" =<< 1. Open an Account >>=")
    print(" =<< 2. Withdrawal Money >>=")
    print(" =<< 3. Deposit Money >>=")
    print(" =<< 4. Check Balance >>=")
    print(" =<< 5. Check Book >>=")
    print(" =<< 6. Atm Card >>=")
    print(" =<< 7. Exit >>=")
    print("*****************************************")
    
    option = input("select your option:")
    if option == "1":
        #The customers will select the options from the above where given.
        print("option 1 is selected by the customers")
        #The option 1 is used to create an account.
        NOC = int(input("number of customers"))
        i = i + NOC
        #the if condition will restrict the number of customers to 10.
        if i > 10 :
            print("/n")
            print("customer registration reached ")
            i = i - NOC
        else:
            #The while loop will run according to no.of customers.
            while Counter_1 <= i :
                    name = input("Input Fullname:")
                    CustomerNames.append(name)
                    pin = str(input("Please input a pin of your option : "))
                    CustomerPins.append(pin)
                    Balance = 0
                    deposition = eval(input("please deposit the amount to start account:" ))
                    Balance=Balance + deposition
                    CustomerBalances.append(Balance)
                    print("/nname= ",end=" ")
                    print(CustomerNames[Counter_1])
                    print("pin= ",end=" ")
                    print(CustomerPins[Counter_2])
                    print("balance= ",end=" ")
                    print(CustomerBalances[Counter_2],end =" ")
                    print("-/Rs")
                    Counter_1 = Counter_1 + 1
                    Counter_2 = Counter_2 + 1
                    print("/nyour name is added to customer system")
                    print("/nyour pin is added to customer system")
                    print("your balance is added to customer system")
                    print("--New account is created successfully!--")
                    print("your name is available on the customers list now")
                    print(CustomerNames)
                    print("/n")
                    print("Note! please remember your name and pin")
                    print("=======================================")
                    #this statement below helps the user to go back to start of the program(main menu).
            mainmenu = input("please press enter key to perform next step:")
    elif option == "2":
        j=0
        print("option is selected by the customer")
        #this while loop will prevent the user using account if username and pin is wrong.
        while j < 1 :
            s = -1
            name =input("please input name:")
            pin =input("please input pin:")  
            # This while loop will keep the function running when variable k is smaller than length of the
            # customerNames list.
                     
            while s < len(CustomerNames) - 1 :
                s = s + 1
                 # These two if conditions find where both the name and pin matches.
                if name == CustomerNames[s]:
                    if pin == CustomerPins[s]:
                        j = j + 1
                        # These few statement would show the balance taken from the list.
                        
                        print("your current balance:",end=" ")
                        print(CustomerBalances[s],end=" ")
                        print("-/Rs/n")
                        Balance = (CustomerBalances[s])
                        # Statement below would take the amount to withdraw from user.
                        Withdrawal = int(input("input value to withdraw:"))
                        # The if condition below would look whether the withdraw is greater than the balance.
                        if Withdrawal > Balance :
                            # This statement below would take a deposition from the customer.
                            deposition = int(input("please deposit higher amount beacuse your balance mentioned is not enough:"))
                             # These few statements would update the value and show the balance to user.
                            
                            Balance =Balance + deposition
                            print("your current balance:" ,end =" ")
                            print(Balance, end=" ")
                            print("-/Rs/n")
                            Balance = Balance - Withdrawal
                            print("-/n")
                            print("---withdraw successfull!")
                            CustomerBalances[s] = Balance
                            print("your new balance: ",Balance,end=" ")
                            print("-/Rs/n/n")
                        else:
                              # Else condition mentioned above is to do withdrawal if the balance is greater than the
                            # withdraw amount
                            
                           Balance = Balance - Withdrawal
                             # These few statement would update the values in the list and show it to the customer.
                           print("/n")
                           print("---withdraw successful!---")
                           CustomerBalances[s] = Balance
                           print("your new balance",Balance,end =" ")
                           print("-/Rs/n/n")
            if j < 1 :
                   # The if condition above would work when the pin or the name is wrong.
                print("your name and pin does match!/n")
                break
             # This statement below helps the user to go back to the start of the program (main menu).
        mainmenu = ("please press enter key to perform next step")
    elif option == "3":
        print("option 3 is selected by the customer")
        n = 0
       # The while loop below would work when the pin or the username is wrong.
        
        while n < 1:
            s = -1
            name = input("please input name:")
            pin = input("please input pin :")
             # The while loop below will keep the function running to find the correct user.
            while s < len(CustomerNames) - 1:
                s = s + 1
                  # The two if conditions below would find whether both the pin and the name is correct.
                if name == CustomerNames[s] :
                    if pin == CustomerPins[s]:
                        n = n +1
                        # These statements below would show the customer balance and update list values according to
                        # the deposition made.
                        
                        print("your current balance",Balance,end=" ")
                        print(CustomerBalances[s],end=" ")
                        print("-/Rs")
                        Balance = (CustomerBalances[s])
                           # This statement below takes the deposition from the customer.
                        deposition = int(input("enter the value to deposit:"))
                        Balance = Balance + deposition
                        CustomerBalances[s] = Balance
                        print("/n")
                        print("---Deposition successful---")
                        print("your new balance:",Balance,end=" ")
                        print("-/Rs/n/n")
            if n < 1 :
                print("your name and pin does not match!/n")
                break
             # This statement below helps the user to go back to the start of the program (main menu).
        mainmenu = input("please press enter key to perform next step")
    elif option == "4":
        print("option 4 is selected by the customer")
        s = 0
        print("Customer name list and balances mentioned below:")
        print("/n")
         # The while loop below will keeping running until all the customers and balances are shown.
        while s <= len(CustomerNames) -1:
             print("->. Customer = ",CustomerNames[s])
             print("->. Balance= ",CustomerBalances[s],end=" ")
             print("-/Rs")
             print("/n")
             s = s + 1
             # This statement below helps the user to go back to the start of the program (main menu).
        mainmenu = input("please press enter key to perform next step:")
        
    elif option == "5":
        # These statements would be just showed to the customer.
        print("option 5 is selected by the customer")
        n = 0
        if  n < 1:
            s = -1
            name=input("Input Check book Name:")
        
            pin=str(input("Input  check book Pin:"))
             # The while loop below will keeping running until all the customers and balances are shown.    
            while s < len(CustomerNames) - 1:
                s = s + 1
                 # The two if conditions below would find whether both the pin and the name is correct.
                if name == CustomerNames[s]:
                    if pin == CustomerPins[s]:
                        n = n + 1
                        print("your Check book Name is added to customer system")
                        print("Note! please remember your name and pin")
                        print("=======================================")
                        print("---your Check book is granted!---")
            if n < 1:
               print("your CheckbookName and CheckbookPin does not match!/n")    
                # This statement below helps the user to go back to the start of the program (main menu).        
        mainmenu = input("please press enter key to perform next step:")                
                        
        
    elif option == "6":
        # These statements would be just showed to the customer.
        print("option 6 is selected by the customer")
        n = 0
        if  n < 1:
            s = -1
            name=input("Input Atm card Name:")
        
            pin=str(input("Input  Atm card Pin:"))
             # The while loop below will keeping running until all the customers
            while s < len(CustomerNames) - 1:
                s = s + 1
                 # The two if conditions below would find whether both the pin and the name is correct.
                if name == CustomerNames[s]:
                    if pin == CustomerPins[s]:
                        n = n + 1
                        print("your Atm Card Name is added to customer system")
                        print("Note! please remember your name and pin")
                        print("=======================================")
                        print("---your Atm card is granted!---")       
                        
            if n < 1:
               print("your Atm card Name and Atm card Pin does not match!/n")
                # This statement below helps the user to go back to the start of the program (main menu).
        mainmenu = input("please press enter key to perform next step:")
    elif option == "7":
           print("option 7 is selected by the customer")
           print("Thank you for using our banking system")
           print("/n")
           print("come again")
           print("bye bye")
    else:
        # This else function above would work when a wrong function is chosen
        print("Invaild option selected by the customer")
        print("please try again!")
         # This statement below helps the user to go back to the start of the program (main menu).
        mainmenu = input("please press enter key to perform next step")                            
                        
                                           
                          
                    
                    