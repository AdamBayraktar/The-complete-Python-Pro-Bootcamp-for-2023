from art import logo
import os


def main(first='first'):
  print(logo)
  # operations that user should choose between
  operations = '+-*/'
  # first number of user input, must be a number
  if first == 'first':
    first_num = take_number("first")
  else:
    # if user is using the result of previous then result is passed to first number
    first_num = first
  # print operations avaible
  for operation in operations:
    print(operation)
  # user choose operations, must be one of avaible operations
  while True:
    operation = input("Pick an operation: ")
    if operation in operations and len(operation) == 1:
      break
    else:
      print("Choose valid operation.")
  # users second number
  second_num = take_number("second")
  # calculation function prints out the calculation and return result
  # continue or end function ask user whether to continue calcution with result of calculation, to restart the program or to quit the program
  continue_or_end(calculation(first_num, second_num, operation))
        
        
def take_number(which_number):
  # return user input that is float
  """
  Which users number input it is
  Function that takes user input which then converts to float
  """
  while True:
    num = input(f"What's the {which_number} number? ")
    try:
      num = float(num)
      break
    except:
      print('It must be a number') 
  return num


def calculation(first_num, second_num, operation):
  if operation == '/':
    result = round((first_num / second_num), 2)
    print(f'{first_num} {operation} {second_num} = {result}')
    return result
  elif operation == '*':
    result = round((first_num * second_num), 2)
    print(f'{first_num} {operation} {second_num} = {result}')
    return result
  elif operation == '+':
    result = round((first_num + second_num), 2)
    print(f'{first_num} {operation} {second_num} = {result}')
    return result
  elif operation == '-':
    result = round((first_num - second_num), 2)
    print(f'{first_num} {operation} {second_num} = {result}')
    return result

  print("upsss an error occured")
  os._exit(0)
  

# asks user to continue, restart or quit
def continue_or_end(result):
  decision = input(f"Type 'y' to continue calculating with {result}, 'r' to restart calculator or 'q' to quit program: ")
  if decision == 'y':
    os.system('clear')
    main(result)
  elif decision == 'r':
    os.system('clear')
    main()
  elif decision == 'q':
    return 0
  else:
    continue_or_end(result)





main()