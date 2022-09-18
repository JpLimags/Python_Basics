#Método append
#Esse método adicionará itens ao final da lista

lista_capitais = []

lista_capitais.append("Fortaleza")
lista_capitais.append("Seoul")
lista_capitais.append("Los Angeles")
lista_capitais.append("Tokio")

print(lista_capitais)

#Método insert
#É aconselhado o uso quando queremos adicionar um item em uma posição especifica

lista_capitais.insert(1, "Porto Alegre")
print(lista_capitais)

#Mètodos para remoção de valores da lista

#Método Remove
#Esse método remove o item a partir de seu valor

lista_capitais.remove("Porto Alegre")
print(lista_capitais)

#Método pop 
#Retira o item apartir de sua posição 
#Uma curiosidade é que ele retornará o item removido

item_removido = lista_capitais.pop(0)
print(lista_capitais)
print(f"O item removido da posição 0 foi {item_removido}")



