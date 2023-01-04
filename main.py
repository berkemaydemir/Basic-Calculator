from art import logo

def add(n1,n2):
  return n1+n2
def subtract(n1,n2):
  return n1-n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2

operations={"+" : add,
            "-" : subtract,
            "*" : multiply,
            "/" : divide,           
           }

def calculator():
  print(logo)
  return_calculate=True
  n1=float(input("What is first number: "))
  
  while return_calculate==True:
    for i in operations:
      print(i)
    operation_symbol=(input("Pick an operation: "))
    n2=float(input("What is the next number: "))
    calculation_fuction = operations[operation_symbol]
    answer=calculation_fuction(n1,n2)
    print(f"{n1} {operation_symbol} {n2} = {answer}")
    
    ask_continue=input(f"Type 'y' to continue calculating with {answer} or type a 'new' for new calculation or type 'n' to exit: ").lower()
    if ask_continue=="y":
      n1=answer
    elif ask_continue=="new":
      return_calculate=False
      calculator()
    else :
      return_calculate=False
  
calculator()








