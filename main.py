'''

Asignacion #3


CALENDARIO GREGORIANO

Daniel Alvarado Bonilla
Roberto Rojas Segnini



04/08/2019
'''

def fecha_es_tupla(_fecha):
    result = True
    if  isinstance(_fecha, tuple) and len(_fecha) == 3:

        anho = _fecha[0]
        mes = _fecha[1]
        dia = _fecha[2]

        if not are_integers(anho,mes,dia):
            result = False

    else:
        result = False
    return result


def are_integers(_var1,_var2,_var3):
    return  isinstance(_var1,int) and  isinstance(_var2,int) and  isinstance(_var3,int)


def bisiesto(_anho):
    result = False

    if _anho%4 == 0:
        if _anho%100 ==0 and _anho%400 != 0:
            return True
    return result




def anho_valido(_anho):
    result = True

    if not isinstance(_anho, int):
        result = False

    elif (_anho < 1582):
        result = False

    return result

def dia_valido(_dia, _anho):
    valido = True
    if (_dia <= 0):
        valido = False
    #elif (_dia)


var = (2,2,2)

print(fecha_es_tupla(var))