#use a+ for append text to file
arch = open("C:\\Users\\Paty\\Desktop\\link2.txt","a+")
for i in range(0,10):
    name = input("¿Cuál es tu nombre?: ") +"\n"
    arch.write(name)

arch.close()
    
