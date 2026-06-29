import datetime

def edad(anio_nac):
    """
    Esta función calcula los años que cumples en el
    año actual
    """
    hoy = datetime.datetime.today()
    return hoy.year - anio_nac

mi_edad = edad(2008)

# Mostramos el resultado en pantalla

print("Este año cumples", mi_edad, "años")