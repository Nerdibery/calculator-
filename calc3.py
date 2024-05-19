class calculator:
    def __init__(self) -> None:
        pass

    def prompt(self):
        self.no1=int(input("enter number  "))
        self.no2=int(input("enter number  "))

    def addition(self):
        self.result = self.no1 + self.no2#instance variable
        return self.result
    
    def subtraction(self):
        self.result = self.no1-self.no2#instance variable
        return self.result
calc = calculator()
while True:
    print(f"calculator menu \n"#new line character
          f'1.add \n'
          f'2.subtract\n '
          f'3.exit\n'
          )
    choice = int(input("enter choice  "))
    if choice == 1:
        print(calc.prompt())
        print (calc.addition())
    elif choice == 2:
        print(calc.prompt())
        print(calc.subtraction())

    elif choice == 3:
        break
    else:
        print("please enter valid choice")


        
    
 