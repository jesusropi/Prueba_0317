#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import choice
from itertools import combinations
from operator import itemgetter, truediv


def amigo_invisible(amigos):
    """Dada una lista de nombres, selecciona 1000 parejas de forma aleatoria,
    calculando las ocurrencias de cada una, imprimiendo finalmente por pantalla
    los porcentajes de las 5 mas frecuentes.
    Entradas: (list) lista de nombres
    Salidas: 5 parejas mas frecuentes. Por salida estandar los porcentajes.
    """
    try:
        if len(amigos) > 2:
            ocurrencias = {pareja: 0 for pareja in combinations(amigos, 2)}
            for i in range(1000):
                while True:  # Aleatoriamente, se toman dos nombres
                    sel_1 = choice(amigos)
                    sel_2 = choice(amigos)
                    if sel_1 != sel_2:
                        break
                if (sel_1, sel_2) in ocurrencias:  # A,B = B,A
                    ocurrencias[(sel_1, sel_2)] = (
                        ocurrencias[(sel_1, sel_2)] + 1)
                else:
                    ocurrencias[(sel_2, sel_1)] = (
                        ocurrencias[(sel_2, sel_1)] + 1)
            ocurrencias_ord = sorted(ocurrencias.items(), key=itemgetter(1),
                                     reverse=True)
            for o in ocurrencias_ord[0:5]:  # Calculo %
                print "Amigos: {}, {}. Porcentaje: {} %".format(
                    o[0][0], o[0][1], str(truediv(o[1], 10)))
        else:
            raise DatosInvalidos()
    except DatosInvalidos:
        print "Datos invalidos"
    except Exception, error:
        print "Amigo Invisible Error: %s" % error


class DatosInvalidos(Exception):
    pass


if __name__ == '__main__':
    amigos = ['Pixie', 'Dixie', 'Tom', 'Jerry', 'Piolín', 'Lucas',
              'Correcaminos', 'Donald', 'Mickey', 'Pluto']
    amigo_invisible(amigos)
