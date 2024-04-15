import functions

while True:
  print('\t\t\t[Asset Manager]')
  print('[1] Add a device')
  print('[2] Display devices')
  print('[3] Lookup a device')
  print('[4] Delete a device')
  print('[5] Quit')
  option = int(input('Option >> '))
  if option == 1:
    functions.Create()
  elif option == 2:
    functions.GetAll()
  elif option == 3:
    functions.GetDevice()
  else:
    print('Program terminated')
    break