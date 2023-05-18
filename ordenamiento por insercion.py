#Ordenamiento por inserción

def ordenamiento_insercion(lista):
    
    for indice in range(1, len(lista)): # Crea un contador segun el largo de la lista para usar el indice como cursor
        
        valor_actual = lista[indice] # Guarda el valor actual del cursor en una variable
# ej: (5)
        while indice > 0 and lista[indice - 1] > valor_actual: # Si el cursor es mayor que cero y el numero anterior al cursor es mayor que el valor actual
# ej: 7 > (5)?
            lista[indice] = lista[indice -1] # El valor actual pasa a ser igual al numero anterior al cursor
# ej: [...7,(5)...] => [...7,(7)...]
            indice -= 1 # Se resta 1 al indice para posarnos en el numero anterior al cursor
# ej: [...(7),7...]
        lista[indice] = valor_actual # Insertamos en la posicion del numero anterior, el valor que teniamos guardado y seguimos con el siguiente indice
# ej: [...(7),7...] => [...(5),7...]
        
    return lista

    
if __name__=='__main__':
    lista = [7,5,3,8,1,9,8,2]
    lista_ordenada = ordenamiento_insercion(lista)
    print(lista_ordenada)
