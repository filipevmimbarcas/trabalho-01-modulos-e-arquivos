import os
from prettytable import PrettyTable
from datetime import date

fileName = 'db_devices.txt'


def Title(text, symbol = '-', quantity = 40):
  print()
  print(text)
  print(symbol*quantity)

#Gera um id para inserir no arquivo
def GenerateId()->int:

  if not os.path.isfile(fileName):
    print('There is no devices registered!')
    counter = 1
    return counter
  else:
      file = open(fileName)
      lines = file.readlines()
      file.close()
      counter = 1

      for line in lines:
        line = line.split(';')
        if int(line[0]) == counter:
          counter = counter + 1
      
      return counter

#Insere um dispositivo
def Create():
  Title('Insert a device','=')

  id = GenerateId()
  vendor = input('Vendor: ')
  model = input('Model: ')
  quantity = int(input('Quantity: '))
  today = date.today()


  option = input('Do you want to continue? [yes/no]: ')
  if option.upper() == 'YES':
    file = open(fileName,'a')
    file.write(f'{id};{vendor};{model};{quantity};{today}\n')
    file.close
    print('\nAsset registered successfully\n')
  else:
    print('Abort')

#Lista todos os ativos
def GetAll():

  os.system('clear')
  Title('List all devices','=',47)

  if not os.path.isfile(fileName):
    print('There is no devices registered!')
    return
  
  file = open(fileName)
  lines = file.readlines()
  file.close()

  myTable = PrettyTable(['Id','Vendor','Model','Quantity','Created at'])


  for line in lines:
    parts = line.split(';')

    id = parts[0]
    vendor = parts[1]
    model = parts[2]
    quantity = int(parts[3])
    createdAt = parts[4]

    myTable.add_row([id,vendor.capitalize(),model.upper(),quantity,createdAt])

  print(myTable)
