import constantes
def imprimir_menu():
    for fila in zip(*([k]+(v) for k, v in constantes.menu.items())):
       print(*fila)
       
def imprimir_menu2():
    for fila in zip(*([k]+(v) for k, v in constantes.menu.items())):       
       print("\t" + fila[0] + " " + fila[1])

def imprimir_menu3(menu, desde =0, hasta =2):
    """Imprime el menu de opciones del juego ; el índice y el texto
        Returns:
        None
    """
    # Extraer las claves y los valores como listas. Acceder a todos los elementos menos el último
    print (len(menu.keys()))
    claves = list(menu.keys())[desde:hasta]
    filas = len(menu[claves[0]])  # Número total de filas


    # Iterar desde la segunda fila
    for i in  range(0, filas):
        fila = [menu[clave][i] for clave in claves]  # Obtener valores de cada clave en la fila y se mete en una lista
        
        print( "\t" + (" ".join(fila)))  # Formato de salida. Join une los elementos de fila con el separador indicado entre "", en esta caso espacio.         
    return