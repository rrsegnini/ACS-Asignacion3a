'''

Asignacion #3b


CALENDARIO GREGORIANO

Daniel Alvarado Bonilla
Roberto Rojas Segnini



04/08/2019
Update 
20/04/2019
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


def dias_desde_primero_enero(_fecha):
    if not fecha_es_valida(_fecha):
        return -1
    d1 = 1
    mes1 = 1
    anho = _fecha[0]

    diasMes = [31, 28, 31, 30, 31, 30,
                 31, 31, 30, 31, 30, 31]

    if bisiesto(anho):
        diasMes[1] = 29

    mesDado =_fecha[1]
    diaDado = _fecha[2]


    diferencia = 0

    for i in range(mesDado-1):
        diferencia += diasMes[i]
        print(i)

    diferencia = (diaDado + diferencia) -1


    return diferencia


#Fuente: https://cs.uwaterloo.ca/~alopez-o/math-faq/node73.html
def dia_primero_enero(_anho):
    k = 1
    m = 11
    C = float((_anho//100) + 1)
    Y = float((_anho-1)%100)


    W = (k + math.floor(2.6 * 1 - 0.2) - 2*C + Y + math.floor(Y/4) + math.floor(C/4))%7
    return int(W)

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
    meses = [[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]] for x in range(0, 12)]
    #print(meses)
    fecha_actual = (_anho,1,1)
    cont_mes = 0
    cont_sem = 0
    cont_dia = dia_primero_enero(_anho)
    mes_actual = 1
    while fecha_actual[0] != _anho+1:
        #print(fecha_actual)
        #fecha_actual[1] != cont_mes:
        if cont_dia>6:
            cont_dia = 0
            cont_sem += 1
        #print(fecha_actual)
        if mes_actual != fecha_actual[1]:
            mes_actual = fecha_actual[1]
            cont_sem = 0

        #[print(meses[fecha_actual[1]-1])#,cont_sem,cont_dia)

        meses[fecha_actual[1]-1][cont_sem][cont_dia] = fecha_actual[2]
        fecha_actual = dia_siguiente(fecha_actual)
        cont_mes+=1
        cont_dia+=1

    print("Calendario del año " + str(_anho) + " D.C.")
    print("             Enero             |             Febrero           |             Marzo             |             Abril             |")
    print("   D   L   K   M   J   V   S   |   D   L   K   M   J   V   S   |   D   L   K   M   J   V   S   |   D   L   K   M   J   V   S   |")
    imprimir(meses, 0)

    print("              Mayo             |              Junio            |             Julio             |            Agosto             |")
    print("   D   L   K   M   J   V   S   |   D   L   K   M   J   V   S   |   D   L   K   M   J   V   S   |   D   L   K   M   J   V   S   |")
    imprimir(meses, 4)

    print("            Setiembre          |             Octubre           |          Noviembre            |          Diciembre            |")
    print("   D   L   K   M   J   V   S   |   D   L   K   M   J   V   S   |   D   L   K   M   J   V   S   |   D   L   K   M   J   V   S   |")
    imprimir(meses, 7)


def imprimir(_meses,_mes_inicial):
    cont_meses = 0

    #for i in range(mes_inicial,mes_final):

    for j in range(0,6):
        w = (_meses[_mes_inicial][j] + _meses[_mes_inicial+2][j] + _meses[_mes_inicial+3][j] + _meses[_mes_inicial+4][j])
        result = ""
        for dia in w:
            if dia == 0:
                result += "   "
            else:
                result += str(dia) + "    "
        print (result + "|")
        #print  ('{:>4}'.format(result))




def fecha_futura(_fecha,_dias):
    '''
    Dados una fecha válida f y un número entero no-negativo n, 
    determinar la fecha que está n días naturales en el futuro. 
    El resultado debe ser una fecha válida.
    '''
    nuevaFecha = _fecha;

    if not fecha_es_valida(_fecha) or _dias <= 0:
        return -1

    while (_dias!= 0):
        nuevaFecha = dia_siguiente(nuevaFecha);
        _dias-=1;

    return nuevaFecha;


def obtener_fecha_mayor(_fecha1,_fecha2):
    anho1 = _fecha1[0]
    mes1 = _fecha1[1]
    dia1 = _fecha1[2]

    anho2 = _fecha2[0]
    mes2 = _fecha2[1]
    dia2 = _fecha2[2]

    mayor = _fecha1
    if (anho1 < anho2):
        mayor = _fecha2
    elif (anho1== anho2):
        if (mes1 <mes2):
            mayor = _fecha2
        elif(mes1 == mes2):
            if (dia1 < dia2):
                mayor = _fecha2
    return mayor


def dias_entre(_fecha1,_fecha2):
    '''
    Dadas dos fechas válidas, f1 y f2, sin importar si f1 ≤ f2 o 
    f2 ≤ f1, determinar el número de días naturales entre las dos fechas. 
    Si f1 = f2, entonces días_entre(f1, f2) = 0. El resultado debe ser un 
    número entero no negativo.
    '''

    if not fecha_es_valida(_fecha1) or not fecha_es_valida(_fecha2):
        return -1

    fechaLimite = obtener_fecha_mayor(_fecha1,_fecha2)
    if (fechaLimite == _fecha2):
        fechaBase = _fecha1
    else:
        fechaBase = _fecha2

    dias = 0

    while (fechaBase != fechaLimite):
        fechaBase = dia_siguiente(fechaBase)
        dias += 1


    return dias



def dia_semana(_fecha):
    ''' 
    Dada una fecha válida, determinar el día de la semana que le corresponde 
    en el calendario gregoriano, con la siguiente codificación: 0 = domingo, 
    1 = lunes, 2 = martes, 3 = miércoles, 4 = jueves, 5 = viernes, 6 = sábado. 
    El resultado debe ser un número entero, conforme a la codificación indicada.
    '''
    if not fecha_es_valida(_fecha):
        return -1

    anho = _fecha[0]
    mes = _fecha[1]
    dia = _fecha[2]

    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    anho -= mes < 3
    return (anho + int(anho/4) - int(anho/100) + int(anho/400) + t[mes-1] + dia) % 7
#Fuente https://www.hackerearth.com/blog/algorithms/how-to-find-the-day-of-a-week/


''' 
def day_of_week(year, month, day):
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= month < 3
    return (year + int(year/4) - int(year/100) + int(year/400) + t[month-1] + day) % 7

'''



#Esta funcion es casi identica a la funcion dia_primero_enero(anho)
#de la Asignacion3a. La diferencia radica en que dia_primero_enero(anho)
#tenia ciertos valores "hardcoded" especificos para el mes de enero.
#En esta nueva funcion, dia_inicio_mes(anho, mes), se generalizo
#el algoritmo
def dia_inicio_mes(anho, mes):
#Fuente: https://cs.uwaterloo.ca/~alopez-o/math-faq/node73.html
    m_offset = [0,11,12,1,2,3,4,5,6,7,8,9,10]
    anho -= mes < 3
    
    k = 1   #dia
    m = m_offset[mes]  #mes
    C = float((anho//100) + 0)  #siglo - 1
    #if mes == 1 or mes == 2:
    #    Y -= 1
    Y = float((anho)%100)     #anho
    
    W = (k + math.floor(2.6 * m - 0.2) - 2*C + Y + math.floor(Y/4) + math.floor(C/4))%7
    return int(W)






#########################################################
#Pruebas para dia_semana(_fecha)
print("dia_semana")
####Sabado
print(dia_semana((2019,4,27)))


####Domingo en enero
print(dia_semana((2019,1,6)))

####Lunes en febrero
print(dia_semana((2019,2,25)))

####Miercoles
print(dia_semana((2019,12,25)))

print("------------------------------------")


#########################################################
#Pruebas para fecha_futura(_fecha,_dias)
print("fecha_futura")

####Dentro del mismo mes
print(fecha_futura((2019,4,27),3))

###Cambio de mes
print(fecha_futura((2018,3,30),5))

####Cambio de año
print(fecha_futura((2000,12,31),1))



#########################################################
print("------------------------------------")

#Pruebas para obtener_fecha_mayor(_fecha1,_fecha2)
print("obtener_fecha_mayor")

####Primera fecha anterior a la segunda
f1 = (2012,11,5)
f2 = (2018,11,2)
print(obtener_fecha_mayor(f2,f1))


####Segunda fecha anterior a la primera
f1 = (2019,10,5)
f2 = (1998,3,31)
print(obtener_fecha_mayor(f2,f1))

####Fechas iguales
f1 = (2018,11,5)
f2 = (2018,11,5)
print(obtener_fecha_mayor(f2,f1))

print("------------------------------------")



#########################################################
#Pruebas para dias_entre(_fecha1,_fecha2)
print("dias_entre")

####Primera fecha anterior a la segunda
f1 = (2012,11,5)
f2 = (2018,11,2);
print(dias_entre(f1,f2))


####Primera fecha mayor a la segunda
f1 = (2020,11,5)
f2 = (2018,11,2);
print(dias_entre(f1,f2))

####Fechas iguales
f1 = (2018,11,2)
f2 = (2018,11,2);
print(dias_entre(f1,f2))

####Año no-bisiesto
f1 = (2017,12,31)
f2 = (2017,1,1);
print(dias_entre(f1,f2))

####Año bisiesto
f1 = (2016,1,1)
f2 = (2016,12,31);
print(dias_entre(f1,f2))

print("------------------------------------")

#########################################################

#Pruebas para dia_inicio_mes(anho, mes)
print("dia_inicio_mes")
print(dia_inicio_mes(2000,1))
print(dia_inicio_mes(2019,5))
print(dia_inicio_mes(2019,4))
print(dia_inicio_mes(2019,1))
print(dia_inicio_mes(2018,5))
print(dia_inicio_mes(2018,1))
print("------------------------------------")



