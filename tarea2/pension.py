# PENSION JK & D10S

# Función que devuelva como resultado si una persona cumple con
# los requisitos legales para recibir una pensión de vejez del
# Instituto Venezolano de los Seguros Sociales (IVSS).

# AUTORES:

# David Segura #13-11341
# Jesus Kauze #12-10273

# Manejo de fechas mediante liberia de python
# Imports
import datetime

# Funcion para calcular la edad, Parametros: Fecha de nacimiento
# Parametros: nacimiento : datetime (datetime.date(year,month,day))

import datetime

# Funcion para calcular la edad, Parametros: Fecha de nacimiento
# Parametros: nacimiento : datetime (datetime.date(year,month,day))

def CalcularEdad(nacimiento):
    hoy = datetime.date.today()

    # CASO 1: edad mayor de 140 anos
    if (hoy.year - nacimiento.year)  > 140:
        print('La Fecha proporcionada supera los 140 anos de edad, Por favor verifique e ingrese nuevamente')
        return False
    elif hoy < nacimiento:
        print('Fecha de nacimiento Invalida')
        return False
    else:
        ano = nacimiento.year
        mes = nacimiento.month
        dia = nacimiento.day
        fecha = nacimiento
        edad = 0
        while fecha < hoy:
            edad += 1
            fecha = datetime.date(ano+edad, mes, dia)

        print('Mi edad es: %s' % (edad-1))
        return True