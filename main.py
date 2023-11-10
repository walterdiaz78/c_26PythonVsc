"""
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
#print(fruit_emojis)

#INSERT inserta en el indice que quiero
fruit_emojis.insert(2, "🍇")
fruit_emojis.pop()

#print(fruit_emojis)
#for fruta in fruit_emojis:
    #print(fruta)
    

    #--- Verduleria Walter
#A)
index=1

for fruta in fruit_emojis:
    #print(f"La fruta: {index:2} es -> {fruta:_^5}")
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
#print(fruteria_limpia)

#Tuple Tuplas, datos no mutables que no permiten reasignacion

verduleria:tuple=("Walter", True, [])
for fruta in fruit_emojis:
    verduleria[2].append(fruta)
#print (verduleria)



verduleria:list = list(verduleria)
verduleria[2] = [] 
verduleria:tuple = tuple(verduleria)
#print (verduleria)

nueva_mercaderia:list=  fruit_emojis + ["🍎", "🍌", "🍇", "🍊", "🍓", "🍍", "🍒"] *3
#print(nueva_mercaderia)

#SET | CONJUNTOS

frutas_unicas:set = set(nueva_mercaderia)
#print(f"trutas unicas  ==>", frutas_unicas)

conteo_frutas=[]
for fruta_unica in list(frutas_unicas):
    counter = 0
    for f in nueva_mercaderia:
        if fruta_unica == f:
            counter +=1
    conteo_frutas.append((fruta_unica, counter))
    print(conteo_frutas)




# DESAFIO ==> FIZZ BUZZ-------------------------
#Escribe un programa que imprima los números del 1 al 100 (con salto de linea). 
#Pero para los múltiplos de 3, imprime "Fizz" en lugar del número 
# para los múltiplos de 5, imprime "Buzz". 
# Para los números que son múltiplos de ambos 3 y 5, imprime "FizzBuzz".

for numeros in range(1,101):
  
    if numeros % 3 ==0 and numeros % 5 ==0:
        print("FizzBuzz")

    elif numeros%3 == 0:
        print ("Fizz")
    
    elif numeros%5==0:
          print ("Buzz")
    else:
        print(numeros)      
   
   #DICT | Diccionarios
"""
# DICT | Diccionarios

german:dict = {
    "nombre": "German",
    "dni": "96987789",
    "email": "german@mail.com",
    "Lenguajes": ["python", "java", "js"],
    10: "Messi",
    ("german_123", "1234"): 1_000_000
}

print(german)
lg= 'Los lenguajes que maneja el usuario son: '
print(lg, german["Lenguajes"])

for k,v in german.items():
    print (k,": ", v)

#user:str=input("Ingrese user: \t")
#pwd:str=input("Ingrese password: \t")

#print (german[(user,pwd)])

#-----------------
import random
import string


user:list ="belen, walter, melina, susana".split(",")
pwd:list = [
    ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    for pwd in range(4)


]
print(user,pwd)

usuarios_unicos:list = [
    {
        "nombre":u,
        "password":p,
        "status" : True,
        "mail" :f"{u}_underco@mail.com"
    }
    for u,p in zip(user,pwd)
]
print(usuarios_unicos)

for usuario in usuarios_unicos:
    with open (f"{usuario['nombre']}.txt", "w" , encoding="utf8") as f:
        mensaje_:str = f"""

            Bienvenido, {usuario['nombre']}
            Tu email es, {usuario['mail']}
            Tu contraseña es, {usuario['password']}
        """
        f.write(mensaje_)
        
        
       
  


