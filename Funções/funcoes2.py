#Utilização do parametro args

def calcula_media(*args):
    soma = sum(args)
    media = soma/len(args)
    return media

print(calcula_media(10,7,10))

#Utilização do cords

def print_info(**kwargs):
    print(kwargs, type(kwargs))

print_info(nome = "Jp")

#Acima vemos que como utilizar uma função que recebe como parâmetros kwargs, e todos os parâmetros são enviados em um dicionários