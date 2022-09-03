import datetime
import platform
import time

fecha = datetime.datetime.today()
año = fecha.year
mes = fecha.month
dia = fecha.day
print ("Hoy es: " + str(dia) + "/" + str(mes) + "/" + str(año) + ".")

myHostname = platform.uname()[1]
print ("Mi nombre de host es " + myHostname + ".")

print ("Voy a Iterar 10 veces")
for i in iter("0123456789"):
    print("Iteracion: "  + i + ". ")

print ("FIN")


exit()

