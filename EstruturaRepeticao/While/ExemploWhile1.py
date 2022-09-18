import time

#Evitar fazer a aplicação a baico
cont = 0

while True:
    
    time.sleep(0.5)
    if(cont < 10):
    
        cont+=1
        if(cont==1):
            print(cont, "Item limpo")
        else:
            print(cont,"Itens limpos")
    
    else:
        break

print("Louça limpa !")
