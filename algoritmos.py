import math

def distancia_euclidiana(x_1, y_1, x_2, y_2):
    """ Calcula la distancia euclidiana

    Devuelve el resultado de la formula

    También se le conoe a la fórmula como:
    distancia entre dos puntos

    Parámetros:
    x_1 -- origen_x
    y_1 -- origen_y
    x_2 -- destino_x
    y_2 -- destino_y

    """
    return math.sqrt(math.pow(x_2-x_1,2)+math.pow(y_2-y_1,2))