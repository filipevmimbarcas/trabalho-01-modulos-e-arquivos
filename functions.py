import os
from prettytable import PrettyTable
from datetime import date

def Title(text, symbol = '-', quantity = 40):
  print()
  print(text)
  print(symbol*quantity)


def Create():
  Title('Insert a device','=')

  vendor = input('Vendor: ')
  model = input('Model: ')
  serial = input('Serial: ')
  quantity = int(input('Quantity: '))
  today = date.today()


  option = input('Do you want to continue? [yes/no]: ')
  if option.upper() == 'YES':
    file = open('devices.txt','a')
    file.write(f'{vendor};{model};{serial};{quantity};{today}\n')
    file.close
    print('\nAsset registered successfully\n')
  else:
    print('Abort')

def GetAll():

  os.system('clear')
  Title('List all devices','=',47)

  if not os.path.isfile('devices.txt'):
    print('There is no devices registered!')
    return
  
  file = open('devices.txt')
  lines = file.readlines()
  file.close()

  myTable = PrettyTable(['Vendor','Model','Serial','Quantity','Created at'])


  for i , line in enumerate(lines):
    parts = line.split(';')

    vendor = parts[0]
    model = parts[1]
    serial = parts[2]
    quantity = int(parts[3])
    createdAt = parts[4]

    myTable.add_row([vendor.capitalize(),model.upper(),serial,quantity,createdAt])

  print(myTable)
