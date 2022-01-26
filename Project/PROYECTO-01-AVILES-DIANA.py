import os
import getpass


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def enter():
  input('\n[Presiona Enter para continuar]')

#Count
validation_Count = 0
#Login
user_Login = 'admin'
password_Login = '1234'


while validation_Count == 0:
  user_Access = input('USUARIO: ')
  if user_Access == user_Login:
    password_Access = getpass.getpass('CONTRASEÑA: ')
    if password_Access == password_Login:
      print('\nACCESO OTORGADO')
      break
    else:
      clearConsole()
      print('\nCONTRASEÑA INCORRECTA')
      enter()
      validation_Count == 1
      clearConsole()
  else:
    print('\nUSUARIO INCORRECTO')
    enter()
    validation_Count == 1
    clearConsole()

    