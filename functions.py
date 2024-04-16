import os
from prettytable import PrettyTable
from datetime import date

fileName = 'db_devices.txt'


def Title(text,symbol='-',quantity=50):
  print()
  print(f'\t\t\t[{text}]')
  print(symbol*quantity)


def ValidateFile(file)->bool:
  if os.path.exists(file):
    return True
  else:
    return False

#Gera um id para inserir no arquivo
def GenerateId()->int:
  if not ValidateFile(fileName):
    return 1
  else:
    file = open(fileName)
    lines = file.readlines()
    file.close()
    counter = int(lines[-1][0]) + 1
    return counter

#Insere um dispositivo
def Create():
  os.system('clear')
  Title('Insert a device')

  if not ValidateFile(fileName):
    print(f'file {fileName} does not exist, creating file... \n')
  
  id = GenerateId()
  name = input('Name: ')
  vendor = input('Vendor: ')
  model = input('Model: ')
  serial = input('serial: ')
  today = date.today()


  option = input('Do you want to continue? [y/n]: ')
  if option.upper() == 'Y':
    file = open(fileName,'a')
    file.write(f'{id};{name};{vendor};{model};{serial};{today}\n')
    file.close
    print('\nAsset registered successfully\n')
  else:
    print('Abort')

#Lista todos os ativos
def GetAll():

  if not ValidateFile(fileName):
    print(f'There are no registered devices, file {fileName} does not exist\n')
    return

  total = 0
  os.system('clear')
  Title('Displaying all devices')

  file = open(fileName)
  lines = file.readlines()
  file.close()

  myTable = PrettyTable(['Id','Name','Vendor','Model','Serial Number','Created at'])

  for line in lines:
    total = total + 1
    parts = line.split(';')

    id = parts[0]
    name = parts[1]
    vendor = parts[2]
    model = parts[3]
    serial = parts[4]
    createdAt = parts[5]

    myTable.add_row([id,name.capitalize(),vendor.capitalize(),model.upper(),serial,createdAt])

  print(myTable)
  print(f'Total: {total}')


def GetDevice():

  if not ValidateFile(fileName):
    print(f'There are no registered devices, file {fileName} does not exist\n')
    return

  Title('Looking up for a device')
  word = input('Enter search term: ')

  file = open(fileName)
  lines = file.readlines()
  file.close()

  myTable = PrettyTable(['Id','Name','Vendor','Model','Serial Number','Created at'])
  for line in lines:
    if word in line:
      parts = line.split(';')
      id = parts[0]
      name = parts[1]
      vendor = parts[2]
      model = parts[3]
      serial = parts[4]
      createdAt = parts[5]
      myTable.add_row([id,name.capitalize(),vendor.capitalize(),model.upper(),serial,createdAt])
  
  print(myTable)      

def deleteByLine():

  Title('Deleting a device')

  if  not ValidateFile(fileName):
    print(f'There are no registered devices, file {fileName} does not exist\n')
    return

  GetAll()

  id = int(input('Enter de ID: '))

  file = open(fileName)
  lines = file.readlines()
  file.close()
  
  choice = input('Do you want to continue? [y/n]: ')
  if choice.upper() == 'Y':
    index = 0
    for i, line in enumerate(lines):
      if int(line[0]) == id:
        index = i
  
    lines.pop(index)
    file = open(fileName,'w')
    file.write(''.join(lines))
    file.close()
    print('Device deleted')
  else:
    print('Id not found')
  
  if len(lines) == 0:
    os.remove(fileName)
  

