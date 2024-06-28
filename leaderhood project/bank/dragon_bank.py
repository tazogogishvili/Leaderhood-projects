print("enter your informacion for register")
print()

age = int(input("enter youre age: "))
personal_number = int(input("enter youre personal number: "))




if age > 18:
        print("you are adult")

        name = input("enter youre name: ")
        print("name:", name)
        print()

        lastname = input("enter your lastname: ")
        print("lastname:", lastname)
        print()

        mail = input("enter maill: ")
        print("mail:", mail)
        print()

        password = input("enter password: ")
        print("password:",password)
        print()

        print("You have successfully registered!")

else:
        print("You could not register because you are underage")



def update_card_informacion():
    choice_card = int(input("which card do you have (1.TBC or 2.Bank Of Georgian) : "))

    if choice_card == 1:

        print("you choice TBC card")
        card_number = int(input("enter card number: "))
        personal_number = int(input("enter youre personal number: "))
        card_expiry_date = int(input("enter card expiry date (day/month/year): "))
        card_cvv_cvc = int(input("enter card (cvc or ccv): "))
        print("You have successfully registered your card")
        
    elif choice_card == 2:

        print("you choice Bank Of Georgian card")
        card_number = int(input("enter card number: "))
        personal_number = int(input("enter youre personal number: "))
        card_expiry_date = int(input("enter card expiry date (day/month/year): "))
        card_cvv_cvc = int(input("enter card (cvc or ccv): "))
        print("You have successfully registered your card")

    else:
        print("invalid information")

    

def perform_transaction():
    balance = int(input("enter youre balance: "))
        
    operacion = int(input("which one operacion do you wont (1.withdraw or 2.deposit)"))

    if operacion == 1:
        withdraw = int(input("What amount do you want to withdraw?: "))
        balance = balance - withdraw
        print("Your balance is:", balance)

    elif operacion == 2:
        deposit = int(input("How much do you want to deposit?: "))
        balance = balance - deposit

        print("youre balance is:", balance)

    
def delete_acc():
    
    print("Do you want to delete your account?  1) yes   2) no")
    choice = int(input("enter number"))

    if choice == 1:
        print("The operation was performed succesfully")
    elif choice == 2:
        print("The account has not been deleted")
    else :
        print("Wrong informacion")

def search_account_info():

    print("enter personal number: ")
    search_acc = int(input("personal number: "))
    if personal_number == search_acc:
        print(name,lastname,mail,password)


def exit_system():
    print("are you sure you wannt to log out?   1) yes  2) no ")

    choice = int(input("enter number"))

    if choice == 1:
        print("The following request was succesfull comlpated")

print("1) update card informacion")
print("2) perform_transaction")
print("3) delete_acc")
print("4) search_account_info")
print("5) exit_system")

choice = int(input("enter number"))

if choice == 1:
    update_card_informacion()
elif choice == 2:
    perform_transaction()
elif choice == 3:
    delete_acc()
elif choice == 4:
    search_account_info()
else :
    exit_system()


