def fecha_es_tupla(_fecha):
    result = True
    if not isinstance(_fecha, tuple):
        result = False

    anho = _fecha[0]
    mes = _fecha[1]
    dia = _fecha[2]

    if not are_integers(anho,mes,dia):
        result = False
    return result


def are_integers(_var1,_var2,_var3):
    return  isinstance(_var1,int) and  isinstance(_var2,int) and  isinstance(_var3,int)



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


fecha_es_tupla(1)