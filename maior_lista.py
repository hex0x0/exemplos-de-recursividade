def maior_lista(lista):
    if len(lista) == 1:
        return lista[0]
    
    else:
        #maior é o último
        aux = maior_lista(lista[:-1])
        
        if aux > lista[-1]:
            return aux
        else:
            return lista[-1]
        
        
        
print(maior_lista([2, 4, 6]))