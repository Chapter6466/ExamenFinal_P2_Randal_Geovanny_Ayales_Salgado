
# Randal Geovanny Ayales Salgado
# 2024-12-16 Programación 2 - Universidad Politécnica 

# Examen Final 

    # Instrucciones: Este es un examen acumulativo por lo cual puede tener preguntas de cualquiera de los temas vistos en clases, además se debe entregar un archivo .py donde venga las repuestas de las pregunta. Las preguntas que no sean crear código deberán venir en el mismo archivo con el numero de pregunta y la respuesta en un comentario (# 1. Respuesta). El examen debe ser entregado antes de media noche del 16 de diciembre del 2024.

# Parte 2.

# 5. Function to remove empty lists from a list
def aplanar(lista):
    """
    Removes empty sublists from the given list.
    
    Parameters:
        lista (list): A list containing sublists.
    
    Returns:
        list: A new list with empty sublists removed.
    """
    return [sublista for sublista in lista if sublista]

# 6. Function to generate all permutations of a list using recursion
def permutaciones(lista):
    """
    Generates all possible permutations of the given list using recursion.
    
    Parameters:
        lista (list): A list of elements to permute.
    
    Returns:
        list: A list containing all permutations of the input list.
    """
    if len(lista) == 0:
        return [[]]
    if len(lista) == 1:
        return [lista]

    resultado = []
    for i in range(len(lista)):
        elemento = lista[i]
        # Generate permutations of the remaining elements
        resto = lista[:i] + lista[i+1:]
        for p in permutaciones(resto):
            resultado.append([elemento] + p)
    return resultado

# 7. Function to create a nested dictionary from a list and dictionary
def diccionario_anidado(lista, diccionario):
    """
    Creates a nested dictionary using the values of the list as keys and the original 
    dictionary's key-value pairs as values.
    
    Parameters:
        lista (list): A list of keys for the new dictionary.
        diccionario (dict): A dictionary to be used as values in the new dictionary.
    
    Returns:
        dict: A nested dictionary mapping elements of the list to key-value pairs of the input dictionary.
    """
    return {lista[i]: {k: v} for i, (k, v) in enumerate(diccionario.items())}

# Example usage
if __name__ == "__main__":
    # Test aplanar
    print("Aplanar:")
    print(aplanar([[1, 2, 3], [], [3], [5, 6]]))  # Output: [[1, 2, 3], [3], [5, 6]]
    print(aplanar([[], [], [1]]))  # Output: [[1]]
    
    # Test permutaciones
    print("\nPermutaciones:")
    print(permutaciones([1, 2, 3]))
    # Output: All permutations of [1, 2, 3]

    # Test diccionario_anidado
    print("\nDiccionario Anidado:")
    print(diccionario_anidado([8, 3, 2], {'python': 4, 'is': 5, 'best': 9}))
    # Output: {8: {'python': 4}, 3: {'is': 5}, 2: {'best': 9}}