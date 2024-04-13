import functions


while True:
  functions.Title('Devices')
  print('1. Insert a device')
  print('2. List all devices')
  print('3. Delete a device')
  print('4. Delete a device')
  print('5. Quit')
  option = int(input('Option: '))

  if option == 1:
    functions.Create()
  else:
    break