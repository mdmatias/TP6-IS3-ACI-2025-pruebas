
def suma(a, b):
    """ Función que realiza una suma de dos argumentos

    Args:
        a (int/float): argumento a
        b (int/float): argumento b

    Returns:
        int/float: resultado de la suma
    """
    try:
        num_a = int(a)
        num_b = int(b)
        return num_a + num_b
    except (TypeError, ValueError):
        return  None
    
def cuadrado(n):
    """ Calcula el cuadrado de un número entero 
    Args:
        n (int/float): número a elevar al cuadrado
    Returns:
        int/float: resultado del cuadrado del número
    """
    try:
        num = int(n)
        return num * num
    except (TypeError, ValueError):
        return None
    
def cuadrado_binomio(a, b):
    """Calcula el cuadrado de un binomio (a + b)^2

    Args:
        a (int/float): primer término
        b (int/float): segundo término

    Returns:
        int/float: resultado de a^2 + 2ab + b^2
    """
    try:
        num_a = int(a)
        num_b = int(b)
        return cuadrado(num_a) + 2 * num_a * num_b + cuadrado(num_b)
    except (TypeError, ValueError):
        return None
