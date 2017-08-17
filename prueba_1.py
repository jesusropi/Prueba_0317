#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import fsum


def ganador_vuelta(ciclistas, tiempos):
    """Devuelve el nombre del ganador de la vuelta. Se supone que los
    corredores tienen registrados tiempos en las cinco etapas. En caso
    contrario, por ejemplo, si un corredor puede tener registros solo
    en 4 etapas, se podria ordenar los tiempos por numero de registros
    y calcular asi la minima suma dentro de los que tengan todas las
    etapas. De esta forma, ademas, funcionaria fuese cual fuese el numero
    de etapas de la carrera. Tambien se supone que no tienen tiempo cero
    en ninguna etapa y que por tanto los tiempos son reales.
    Entradas: (list) ciclistas con los nombres y matriz (list de list)
              de tiempos
    Salidas: (str) nombre del vencedor
    """
    try:
        if (len(ciclistas) == len(tiempos)):
            totales = [fsum(t) for t in tiempos]
            tiempo_ganador = min(totales)
            if totales.count(tiempo_ganador) > 1:
                dorsales_empatados = [i for i, t in enumerate(totales) if
                                      t == tiempo_ganador]
                nombres_empatados = [ciclistas[i] for i in dorsales_empatados]
                return "Empatados: " + ", ".join(nombres_empatados)
            else:
                dorsal_ganador = totales.index(tiempo_ganador)
                return ciclistas[dorsal_ganador]
        else:
            raise DatosInvalidos()
    except TypeError:
        print "Ganador Vuelta - Error: Algun parametro de tipo inapropiado"
    except DatosInvalidos:
        print ("Ganador Vuelta - Error. Registros invalidos:"
               "\n Participantes: " + str(len(ciclistas)) +
               "\n Etapas registradas por corredor : " + str(len(tiempos[0])) +
               "\n Numero de carreras totales: " + str(len(tiempos)))
    except IndexError:
        print "Ganador Vuelta - Error. Indice invalido"
    except Exception, error:
        print "Ganador Vuelta - Error: " + error


def ganador_etapa(ciclistas, tiempos, etapa):
    """Devuelve el nombre del ganador de la etapa o 'Empataron: ' y los nombres
    de los ganadores concatenaods en caso de que hayan empatado varios
    corredores.
    Entradas: (list) de ciclistas, matriz de tiempos y (int) numero de la etapa
              Se supone que las etapas comienzan en la 1 (etapa primera)
    Salidas: (str) nombre del ganador de la etapa o None en caso de error
    """
    try:
        if (len(ciclistas) == len(tiempos) and etapa <= len(tiempos[0]) and
                etapa > 0):
            tiempos_etapa = [e[etapa - 1] for e in tiempos]
            tiempo_ganador = min(tiempos_etapa)
            if tiempos_etapa.count(tiempo_ganador) > 1:
                dorsales_empatados = [i for i, t in enumerate(tiempos_etapa) if
                                      t == tiempo_ganador]
                nombres_empatados = [ciclistas[i] for i in dorsales_empatados]
                return "Empatados: " + ", ".join(nombres_empatados)
            else:
                dorsal_ganador = tiempos_etapa.index(tiempo_ganador)
                return ciclistas[dorsal_ganador]
        else:
            raise DatosInvalidos()
    except TypeError:
        print "Ganador Etapa - Error: Algun parametro de tipo inapropiado"
    except DatosInvalidos:
        print ("Ganador Etapa - Error: Registros invalidos:"
               "\n Participantes: " + str(len(ciclistas)) +
               "\n Etapas registradas por corredor : " + str(len(tiempos[0])) +
               "\n Numero de carreras totales: " + str(len(tiempos)) +
               "\n Etapa solicitada: " + str(etapa))
    except IndexError:
        print "Ganador Etapa - Error. Indice invalido"
    except Exception, error:
        print "Ganador Etapa - Error: " + error


def ganador_por_etapa(ciclistas, tiempos):
    """
    Entradas: (list) de ciclistas, matriz de tiempos y (int) numero de la etapa
    Salidas: (str) imprime por pantalla los ganadores por etapa
    """
    try:
        if len(ciclistas) == len(tiempos):
            for etapa in range(1, len(tiempos[0]) + 1):
                print "Ganador etapa número: %s" % str(etapa)
                print ganador_etapa(ciclistas, tiempos, etapa)
            return "Fin"
        else:
            raise DatosInvalidos()
    except TypeError:
        print "Ganador por Etapa - Error: Algun parametro de tipo inapropiado"
    except IndexError:
        print ("Ganador por Etapa - Error: Indice fuera de rango."
               "\n Participantes: " + str(len(ciclistas)) +
               "\n Etapas registradas por corredor : " + str(len(tiempos[0])) +
               "\n Numero de carreras totales: " + str(len(tiempos)))
    except Exception, error:
        print "Ganador por Etapa - Error: " + error


class DatosInvalidos(Exception):
    pass


if __name__ == '__main__':
    ciclistas = ['Miguel Indurain', 'Alberto Contador', 'Pedro Delgado']
    tiempos = [[1233.0, 1233.0, 3234.4, 1111.1, 1223.5],
               [1233.0, 1233.0, 3234.4, 1111.1, 1223.3],
               [1233.0, 1233.0, 3234.4, 1111.1, 1223.3]]
    print ganador_vuelta(ciclistas, tiempos)
