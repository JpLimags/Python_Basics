#Utilizando o loop for em uma lista

nomes_cidades = ['Fortaleza', 'Tóquio', 'Amsterdam', 'Zurich']

for nome in  nomes_cidades:
    print(nome)


print('---'*30)

#Utilizando o loop for em um dicionário

cidade = {

    'nome': "Fortaleza", 
    'Estado': 'Ceará',
    'Area_km2': 313.8,
    'Populacao': 2.687,
}

for chave in cidade:
    print(f"{chave}: {cidade[chave]}")


#Utilizando a função range

for position in range(len(nomes_cidades)):
    print(position)

print('---'*30)

#Outro exmplos da utilização da funcao range

print(list(range(10)))
print(list(range(2,10)))
print(list(range(2,10,2)))