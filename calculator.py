class calculator:
    #where class attributes are found
    def __init__(self):#empty class
        pass#can also use None(data type)
    
    def values(self):
        no1 = int(input("input the first number  "))
        no2 = int(input("input second number  "))
        self.add_result = no1 + no2
        print (self.add_result)

    def values2(self):
        n1 = int(input("input the first number  "))
        n2 = int(input("input second number  "))
        self.sub_result = n1-n2
        return self.sub_result

    def menu(self):
        choice_1 = "add"
        choice_2 ="subtract"
        choice_3 = "exit"
        while True:
          print(f"calcultor menu \n"
                f"select {choice_1}\n"
                f'select {choice_2}\n'
                f'select {choice_3}\n'
              )
          choice = input ("enter choice ")
          if choice == "add":
            calc = calculator()
            print (calc.values())

          elif choice == "subtract":
            calc2 = calculator()
            print(calc2.values2())
          elif choice == "exit":#error prone doesnt exit loop
            return 0#terminates function
            break

          else:
             print("invalid choice")
calculations = calculator()

print(calculations.menu())
   




    


       
    





    


        

            



    


    




    
    

    
    