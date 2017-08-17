#!/usr/bin/env python
# -*- coding: utf-8 -*-


def es_primo(num):
    """ Devuelve True si num es un numero primo
    Entradas: (int) num
    Salidas: (boolean) True si el numero es primo, False en otro caso
    """
    try:
        if num >= 0:
            prime = True
            if num < 2:
                prime = False
            else:
                for x in range(2, num):
                    resto = num % x
                    if resto == 0:
                        prime = False
                        break
            return prime
        else:
            raise NoNumeroNatural()
    except NoNumeroNatural:
        print "Is Prime Error: No es un numero valido"
    except TypeError, error:
        print "Is Prime Error: %s" % error


def generar_primos():
    """Imprime por salida estandar numeros primos partiendo del cero hasta que
    recibe un control + c
    Entradas: -
    Salidas: Por salida estandar, la lista de numeros primos hasta que la
    ejecucion sea interrumpida.
    """
    try:
        num = 0
        while True:
            if es_primo(num):
                print "Numero primo: %s" % str(num)
            num += 1
    except KeyboardInterrupt:
        print "Detectado 'Control + C': Fin de la ejecución."


class NoNumeroNatural(Exception):
    pass


if __name__ == '__main__':
    generar_primos()
