valor_passagem = 3.60

valor_corrida = float(input("Qual é o valor da corrida ?\nR$ "))

if(valor_corrida <= valor_passagem*5):
    print("Pague a corrida")
elif(valor_corrida <= valor_passagem*6):
        print("Espere um pouco mais")
else:
    print("Corrida muito cara não vale a pena !")