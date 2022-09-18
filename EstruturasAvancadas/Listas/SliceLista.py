from cgi import print_environ


nome_paises = ['Brasil', 'Argentina', 'China', 'Suíça', 'Japão']


#Slice em listas

#Índices positivos
print(nome_paises[1:3])

#Índices negativos

print(nome_paises[1:-1])

#Se caso utilizarmos omitirmos após o ponto vai do índice infomrado até o final
print(nome_paises[1:])

#O mesmo serve para índice inical como abaixo
print(nome_paises[:4])

#Step, serve para esfecificarmos de quanto em quanto números queremos "pular"

print(nome_paises[::-1])

#Operador serve para verficarmos se determinado itema está na lista
print("Suíça" in nome_paises)