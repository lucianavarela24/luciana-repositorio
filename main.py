from lifestore_file import lifestore_products , lifestore_sales, lifestore_searches


registeredUser = ('Administrador1')
registeredPW = ('luciana24')
 
#declaracion de funciones
def login(usuario,passw):
    if usuario in registeredUser:
        if passw in registeredPW:
            return 1
        else:
            print("\n\tPassword does not match...\n")
    else:
        return 2
 
 #inicializacion de procesos
usuario=input('User: ')
passw = input ('Password: ')
 
if login(usuario,passw)==1:
    print('Welcome ',usuario)
else:
    print('ERROR! User is not registered.')

     #VENTAS  
### Productos más vendidos y productos rezagados a partir del análisis de las categorías con menores ventas y categorias 
# con menores búsquedas

# 5 productos con mayores ventas: 
# lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]

x = [] # lista vacía, para rellenarse con el id_product
x = [i[1] for i in lifestore_sales] # lista de unicamente el segundo indice de lifestore_sales

def contar(datos): # definir función para crear un diccionario de cuantas veces aparece cada dato
    result = {}
    for dato in datos: 
        if dato not in result: 
            result[dato] = 0 # meter contador 0 
        result[dato] += 1 # incrementar el contador de ese dato
    return result 

dicc = contar(x) # almacenamos el diccionario
respuesta = sorted(dicc.items(), key = lambda x: x[1], reverse = True) # lo ordenamos en función del valor con ayuda de una función lambda
print(f"Los cinco productos con mayores ventas, ordenados por (id, número de ventas), son: {respuesta[0:4]}") # con un slicing seleccionamos el top 5


# 10 productos con mayores búsquedas
# lifestore_searches = [id_search, id product]
busquedas = [] # creo lista vacia para rellenarla con el id de producto
for i in lifestore_searches: # se rellena la lista busquedas con todos los id producto 
     busquedas.append(i[1])

aux = contar(busquedas) ; print(aux) # hago un diccionario sobre el número de veces que aparece cada producto
respuesta_2 = sorted(aux.items(), key = lambda x: x[1], reverse = True ) 
respuesta_2 = respuesta_2[0:9]
print (f"Los 10 productos con mayores búsquedas, ordenados por (id_search, id_product), son: {respuesta_2}")

# por categoria, uno con los 5 productos con menores ventas y uno con los 10 productos con menores búsquedas
# listado de los 5 productos con menores ventas: 
respuesta_3 = sorted(dicc.items(), key = lambda x: x[1], reverse = False)
respuesta_3 = respuesta_3[0:15] 
print(f"los productos que sólo se han vendido una vez, ordenados por (id, numero de ventas), son: {respuesta_3}")

# listado de los 10 productos con menores búsquedas: 
respuesta_4 = sorted(aux.items(), key = lambda x: x[1], reverse = False) 
respuesta_4 = respuesta_4[0:9] ; print(respuesta_4)
print (f"Los productos que sólo fueron buscados una vez, ordenados por (id_search, id_product), son: {respuesta_4}")
