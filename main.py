'''

Asignacion #3


CALENDARIO GREGORIANO

Daniel Alvarado Bonilla
Roberto Rojas Segnini



04/08/2019
'''
import math


def fecha_es_tupla(_fecha):
    result = True
    if  isinstance(_fecha, tuple) and len(_fecha) == 3:

        anho = _fecha[0]
        mes = _fecha[1]
        dia = _fecha[2]

        if not enteros(anho,mes,dia):
            result = False

    else:
        result = False
    return result


def enteros(_var1,_var2,_var3):
    return  isinstance(_var1,int) and  isinstance(_var2,int) and  isinstance(_var3,int)


def bisiesto(_anho):
    result = False

    if _anho%4 == 0:
        result = True
    if _anho%100 == 0:
        if _anho%400==0:
            result = True
        else:
            result = False

    return result


def fecha_es_valida(_fecha):

    valida = False
    if fecha_es_tupla(_fecha):
        anho = _fecha[0]
        mes = _fecha[1]
        dia = _fecha[2]

        if anho >= 1582 and anho <= 9999:
            if mes >= 1 and mes <= 12:
                if (dia >= 1 and dia <= 31) and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes ==12):
                    valida = True
                elif (dia >= 1 and dia <= 30) and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
                    valida = True
                elif (dia >= 1 and dia <= 28) and (mes == 2):
                    valida = True
                elif (dia >= 1 and dia <= 29) and (mes == 2):
                    if bisiesto(anho):
                        valida = True

    return valida

#Fuente: https://cs.uwaterloo.ca/~alopez-o/math-faq/node73.html
def dia_primero_enero(_anho):
    k = 1
    m = 11
    C = float((_anho//100) + 1)
    Y = float((_anho-1)%100)


    W = (k + math.floor(2.6 * 1 - 0.2) - 2*C + Y + math.floor(Y/4) + math.floor(C/4))%7
    return W

def dia_siguiente(_fecha):
    #Lista que contiene los meses con 31 dias
    mes_31 = [1,3,5,7,8,10,12]

    #Lista que contiene los meses con 30 dias
    mes_30 = [4,6,9,11]

    #if fecha_es_valida(_fecha):
    anho = _fecha[0]
    mes = _fecha[1]
    dia = _fecha[2]

    sig_anho = anho
    sig_mes = mes
    sig_dia = dia

    if dia == 31 and mes == 12:
        sig_anho = anho + 1
        sig_mes = 1
        sig_dia = 1
    elif mes == 2:
        if bisiesto(anho) and dia == 29:
            sig_mes = 3
            sig_dia = 1
        elif bisiesto(anho) and dia <= 29:
            sig_dia = dia + 1
        elif dia == 28:
            sig_mes = 3
            sig_dia = 1
        else:
            sig_dia = dia + 1

    elif mes in mes_31 and dia == 31:
        sig_dia = 1
        sig_mes = mes + 1
    elif mes in mes_30 and dia == 30:
        sig_dia = 1
        sig_mes = mes + 1
    else:
        sig_dia = dia + 1

    return (sig_anho,sig_mes,sig_dia)



def imprimir_3x4(_anho):
    return imprimir_3x4_aux(_anho,(_anho,1,1))

def imprimir_3x4_aux(_anho, _fecha):
    if _fecha[0] != _anho:
        return (0,0,0)
    print (_fecha)
    return imprimir_3x4_aux(_anho, dia_siguiente(_fecha))

imprimir_3x4(2013)
print(dia_primero_enero(2016))