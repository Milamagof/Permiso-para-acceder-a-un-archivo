"""Función relacionada con el análisis de los intentos de inicio de sesión. Dependiendo de la información
 que recibe, calcula el porcentaje de intentos fallidos y devuelve un porcentaje.
 El programa podría usarse para determinar si se debe bloquear o no a una cuenta"""


def calcular_errores(intentos_totales, intentos_fallidos):
    porcentaje_errores = intentos_fallidos / intentos_totales
    return porcentaje_errores

porcentaje= calcular_errores(4,2)

if (porcentaje >= .5):
    print("Cuenta bloqueada")


print(porcentaje)

