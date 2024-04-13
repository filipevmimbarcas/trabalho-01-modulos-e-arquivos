

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


  option = input('Do you want to continue? [yes/no]: ')
  if option.upper() == 'YES':
    file = open('devices.txt','a')
    file.write(f'{vendor};{model};{serial};{quantity}\n')
    file.close
    print('\nAsset registered successfully\n')
  else:
    print('Abort')

