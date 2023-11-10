#LIST | ARRAYS

fruit_emojis:list = ["🍎", "🍌", "🍇", "🍊", "🍓", "🍍", "🍒"]

#print(fruit_emojis)

#Iteraciones
# fruit_emojis[3],fruit_emojis[0] = fruit_emojis[0],fruit_emojis[3] 
# print(fruit_emojis)

# apend, me permite agregar al ultimo elemento de la lista

fruit_emojis.append("🦊")
fruit_emojis.append("Hola mundo")
fruit_emojis.append("[True, False, 1,2,3]")

#pop borra de la lista
fruit_emojis.pop()
fruit_emojis.pop(2)
print(fruit_emojis)

#INSERT inserta en el indice que quiero
fruit_emojis.insert(2, "🍇")
fruit_emojis.pop()

print(fruit_emojis)
#for fruta in fruit_emojis:
    #print(fruta)
    

    #--- Verduleria Walter
#A)
index=1

for fruta in fruit_emojis:
    print(f"La fruta: {index:2} es -> {fruta:_^5}")
    index+=1
#B)
for index2,fruta in enumerate(fruit_emojis, start=1):
    print(f"La fruta: {index2:2} es -> {fruta:_^5}")

#A y B hacen lo mismo

#-------

#list comprehension
fruteria_limpia:list= [
    var_fruta #valor variable
    for var_fruta in fruit_emojis #lugar de iteracion
    if var_fruta not in ["🍍", "🍒"] #condicion

]
print(fruteria_limpia)

#Tuple Tuplas, datos no mutables que no permiten reasignacion

verduleria:tuple=("Walter", True, [])
for fruta in fruit_emojis:
    verduleria[2].append(fruta)
print (verduleria)



verduleria:list = list(verduleria)
verduleria[2] = [] 
verduleria:tuple = tuple(verduleria)
print (verduleria)