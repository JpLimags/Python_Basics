import time
cont = 0

while(cont <10):
    
    cont+=1
    time.sleep(0.5)
    if(cont==1):
        print(cont, "Item limpo")
    else:
        print(cont,"Itens limpos")

print("Acabou a louça !")