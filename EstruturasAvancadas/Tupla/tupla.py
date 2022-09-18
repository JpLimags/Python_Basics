#Tupla

#A diferença entre um tupla e uma lista está ligada a sua flexibilidade, pois na tupla uma vez criada os valores contidos 
#não poderam ser modificados.

#Primeira forma de implementação

nome_paises = ('Brasil', 'Argentina', 'China', 'Suíça', 'Japão')

#Segunda forma de impementação
#nome_paises = 'Brasil', 'Argentina', 'China', 'Suíça', 'Japão'

#Operações com uma tupla

#Trabalhndo com índices
print(nome_paises[0])

#Abaixo veremos um operação típica de uma tupla

#Package
a,b,c,d,e = nome_paises
print(a,d,e)
