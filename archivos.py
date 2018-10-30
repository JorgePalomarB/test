#(1)'r'	This is the default mode. It Opens file for reading.
#(2)'w'	This Mode Opens file for writing.
#       If file does not exist, it creates a new file.
#       If file exists it truncates the file.
#(3)'x'	Creates a new file. If file already exists, the operation fails.
#(4)'a'	Open file in append mode. 
#       If file does not exist, it creates a new file.
#(5)'t'	This is the default mode. It opens in text mode.
#(6)'b'	This opens in binary mode.
#(7)'+'	This will open a file for reading and writing (updating)

#Abrir un archivo
arch = open("C:\\Users\\Paty\\Desktop\\link2.txt","r")

#Lectura
cad1 = arch.read(10)
arch.seek(0)
cad2 = arch.read()
arch.seek(0)
cad3 = arch.readline()
arch.seek(0)
lista = arch.readlines()


print("*Cadena 1:",cad1)
print("*Cadena 2:",cad2)
print("*Cadena 3:",cad3)
print("*Lista:\n")
for i in lista:
    print(i)

#Escritura
#arch.write("cadena")
#arch.writelines([cadenas])
#abrir flujo
#arch.flush()
#cerrar archivo
arch.close



