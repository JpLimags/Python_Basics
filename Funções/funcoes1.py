#Funcão básica que não recebe parâmetros

def hello():
    print("Hello world")

hello()


#Função para calculo de média
def calcula_media(valor1, valor2, valor3):

    soma = valor1+valor2+valor3
    media = soma/3

    return media


resultado = calcula_media(10, 20, 80)
print(f"{resultado:.2f}")


