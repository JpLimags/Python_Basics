#Declaração de um dicionário cidade

dados_cidades = {

    'nome': "Fortaleza", 
    'Estado': 'Ceará',
    'Area_km2': 313.8,
    'Populacao': 2.687,
}

print(type(dados_cidades))
print(dados_cidades)

#Adicionando novo valor a um dicionário

dados_cidades['pais'] = 'Brasil'
print(dados_cidades)

#Acessando o valor de um dicionário
print(dados_cidades['nome'])

#Modificando o valor do dicionário

dados_cidades['Area_km2']= 315
print(dados_cidades)

#Copiando o valor de um dicionário em uma nova variável e modificando

#dados_cidades2 = dados_cidades
#dados_cidades2['nome']= "Porto Alegre"

#print(dados_cidades)
#print(dados_cidades2)

#Como podemos ver, se fizermos da forma acima o valor dos dois dicinários será alterado
#Para evitar esse problema utilizaremos o método copy

dados_cidades2 = dados_cidades.copy()
dados_cidades2['nome'] = 'Curitiba'

print(dados_cidades)
print(dados_cidades2)

#Método update
#Tem a função de adionar a um dicionário original novos dados apartir de um dic mais novo

new_data = {

    'populaca': 5,
    'fundacao': "13 de abril de 1726"

}

dados_cidades.update(new_data)
print(dados_cidades)

#Método get
#A diferença do acesso com o get, é que caso determinada chave não exista ao invés de retornar um erro ele retornará 'none'

print(dados_cidades.get('Prefito'))