nomes_cidades = "Fortaleza, João Pessoa, Curitiba, São Paulo"

#Método slice
#Quebra todos o valores da string guardando os em uma lista

nomes_cidades = nomes_cidades.split(', ')
print(nomes_cidades)

#Método strip
#Serve para retirarmos espaços do começo e final

cabecalho = "          Menu Principal        "
print(cabecalho.strip())

FortaCity = "ForTAlezA é BeLA"

#Geralmente ultilizado para título, coloca cada letra inicial da palavra em maiúsculo
print(FortaCity.title())

#O captlize coloca apenas a primeira letra da frase em maúsculo o resto fica tudo minúsculo
print(FortaCity.capitalize())

#Deixa todas a lêtras maiúsculo
print(FortaCity.upper())

#Deixa todas a lêtras minúscula
print(FortaCity.lower())

#O método in também pode ser ultilizado aqui

note = "Jp entrou no Nds"
print("Jp" in note)