"""Function related to the analysis of login attempts. Depending on the information
 that it receives, calculates the percentage of failed attempts and returns a percentage.
 The program could be used to determine whether or not to block an account"""


def calcular_errores(intentos_totales, intentos_fallidos):
    porcentaje_errores = intentos_fallidos / intentos_totales
    return porcentaje_errores

porcentaje= calcular_errores(4,2)

if (porcentaje >= .5):
    print("Cuenta bloqueada")


print(porcentaje)

