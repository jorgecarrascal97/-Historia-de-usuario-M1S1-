# -Historia-de-usuario-M1S1-
      Registrar productos con su nombre, precio y cantidad en un programa simple.     Calcular operaciones básicas como total de unidades y costo aproximado.     Aplicar fundamentos de programación: entrada de datos, variables, operaciones matemáticas y salidas en consola.

      

Hello. My name is JORGE CARRASCAL 

Today I want to talk about my Python project.

This project is a basic ATM program.
It is a simple simulation of a bank ATM.

The name of the ATM is TechBank Riwi Digital.

First, the program shows a welcome message to the user.
Then, the program asks the user to enter a password.

The system gives the user three tries to enter the correct password.
If the password is correct, the program shows the main menu.

The menu has three options.

The first option is to check the balance.
The second option is to withdraw money.
The third option is to exit the program.

If the user chooses option one, the program shows the account balance.

If the user chooses option two, the program asks how much money the user wants to withdraw.

Then the system checks the balance.

If the user does not have enough money, the program shows a message that says "insufficient balance".

If the user has enough money, the program subtracts the money from the balance.

After that, the program shows the amount withdrawn and the new balance.

If the user chooses option three, the program ends and says thank you for using the ATM.

Right now, the program is simulating the process of an ATM system.


print("bienvenido a cajero automatico techbank riwi digital") 
tries = 0
maxtries = 3
password = "1234"
mount= 1000

while tries < maxtries:
    clave = input("ingrese su clave: ")
    if clave == password: 
        print("clave correcta, bienvenido")
        
        print("n---MENU PRINCIPAL---")  
        print("1. consultar saldo")
        print("2. retirar dinero")
        print("3. salir")

        action = int (input ("que desea hacer ?"))
       

    if action == 1:
        print("su saldo es de :", mount) 

    elif action == 2:
        withdraw = int (input("cuanto dinero desea retirar?"))

        if withdraw > mount:
            print(" saldo insufuciente")
        else:
            mount = mount - withdraw 
            print ("valor a retirar: ", withdraw)
            print ("su nuevo saldo es :", mount)

    elif action == 3: 
        print ( " gracias por usar nuestro cajero automatico, vuelva pronto")
        break 
