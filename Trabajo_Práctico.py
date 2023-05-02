import getpass

Usuario_adm = "1"
Contraseña_adm = "12"

Contador = 0
Usuario = 0
Contraseña = 0 
while ((Usuario != Usuario_adm) and (Contraseña != Contraseña_adm)) and Contador < 3: 
   Usuario = input("Escriba su usuario: ")
   Contraseña = getpass.getpass("Escriba su contraseña: ")
   Contador = Contador + 1
   if Usuario == Usuario_adm and Contraseña == Contraseña_adm:
      print ("Hola, has ingresado correctamente")
   elif Contador < 3: 
      print ("Compruebe si su Usuario o Contraseña estan correctos, vuelva a intentarlo")
   else:
      print("Su numero de intentos ha finalizado")



