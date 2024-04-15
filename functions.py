import os
from prettytable import PrettyTable
from datetime import date

fileName = 'db_devices.txt'


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
  os.system('clear')
  print('\t\t\t[Insert a device]')

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

  os.system('clear')
  print('\t\t\t[Displaying all devices]')

  if not os.path.isfile(fileName):
    print('There is no devices registered!')
    return
  
  file = open(fileName)
  lines = file.readlines()
  file.close()

  myTable = PrettyTable(['Id','Name','Vendor','Model','Serial Number','Created at'])


  for line in lines:
    parts = line.split(';')

    id = parts[0]
    name = parts[1]
    vendor = parts[2]
    model = parts[3]
    serial = parts[4]
    createdAt = parts[5]

    myTable.add_row([id,name.capitalize(),vendor.capitalize(),model.upper(),serial,createdAt])

  print(myTable)


def GetDevice():

  print('\t\t\t[Looking up for a device]')
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