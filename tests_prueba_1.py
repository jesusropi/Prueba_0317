from unittest import TestCase, main
from prueba_1 import ganador_vuelta, ganador_etapa, DatosInvalidos


class TestPrueba1(TestCase):

    def test_ganador_etapa(self):
        # Caso normal
        ciclistas = ['Miguel Indurain', 'Alberto Contador', 'Pedro Delgado']
        tiempos = [[1233.0, 1233.0, 3234.4, 1111.1, 1223.5],
                   [1232.0, 1233.0, 3234.4, 1111.1, 1223.2],
                   [1233.0, 1233.0, 3234.4, 1111.1, 1223.3]]
        etapa = 1
        self.assertEqual(ganador_etapa(ciclistas, tiempos, etapa),
                         'Alberto Contador')
        # Etapa que no existe
        ciclistas = ['Miguel Indurain', 'Alberto Contador', 'Pedro Delgado']
        tiempos = [[1233.0, 1233.0, 3234.4, 1111.1, 1223.5],
                   [1233.0, 1233.0, 3234.4, 1111.1, 1223.2],
                   [1233.0, 1233.0, 3234.4, 1111.1, 1223.3]]
        etapa = 6
        self.assertRaises(DatosInvalidos,
                          ganador_etapa(ciclistas, tiempos, etapa))

        # Errores en los registros: mas tiempos que ciclistas
        ciclistas = ['Miguel Indurain', 'Alberto Contador']
        tiempos = [[1233.0, 1233.0, 3234.4, 1111.1, 1223.5],
                   [1233.0, 1233.0, 3234.4, 1111.1, 1223.2],
                   [1233.0, 1233.0, 3234.4, 1111.1, 1223.3]]
        etapa = 5
        self.assertRaises(DatosInvalidos,
                          ganador_etapa(ciclistas, tiempos, etapa))

        # Error parametro de entrada
        ciclistas = ['Miguel Indurain', 'Alberto Contador', 'Pedro Delgado']
        tiempos = [[1233.0, 1233.0, 3234.4, 1111.1, 1223.5],
                   [1233.0, 1233.0, 3234.4, 1111.1, 1223.2],
                   [1233.0, 1233.0, 3234.4, 1111.1, 1223.3]]
        etapa = 5
        self.assertRaises(TypeError,
                          ganador_etapa(ciclistas, 3.141516, etapa))

        # Empate en la etapa de los tres ciclistas
        ciclistas = ['Miguel Indurain', 'Alberto Contador', 'Pedro Delgado']
        tiempos = [[1233.0, 1233.0, 3234.4, 1111.1, 1223.5],
                   [1233.0, 1233.0, 3234.4, 1111.1, 1223.5],
                   [1233.0, 1233.0, 3234.4, 1111.1, 1223.5]]
        etapa = 5
        self.assertEqual(ganador_etapa(ciclistas, tiempos, etapa),
                         ('Empatados: Miguel Indurain, Alberto Contador, '
                          'Pedro Delgado'))

        # Dos ganadores, empatados en primer lugar
        ciclistas = ['Miguel Indurain', 'Alberto Contador', 'Pedro Delgado']
        tiempos = [[1233.0, 1234.0, 3234.4, 1111.1, 1223.5],
                   [1233.0, 1233.0, 3234.4, 1111.1, 1223.2],
                   [1233.0, 1233.0, 3234.4, 1113.1, 1223.2]]
        etapa = 2
        self.assertEqual(ganador_etapa(ciclistas, tiempos, etapa),
                         'Empatados: Alberto Contador, Pedro Delgado')

    def test_ganador_vuelta(self):
        # Caso normal
        ciclistas = ['Miguel Indurain', 'Alberto Contador', 'Pedro Delgado']
        tiempos = [[1233.0, 1233.0, 3234.4, 1111.1, 1223.5],
                   [1232.0, 1233.0, 3234.4, 1111.1, 1223.2],
                   [1233.0, 1233.0, 3234.4, 1111.1, 1223.3]]
        self.assertEqual(ganador_vuelta(ciclistas, tiempos),
                         'Alberto Contador')

        # Errores en los registros: mas tiempos que ciclistas
        ciclistas = ['Miguel Indurain', 'Alberto Contador']
        tiempos = [[1233.0, 1233.0, 3234.4, 1111.1, 1223.5],
                   [1233.0, 1233.0, 3234.4, 1111.1, 1223.2],
                   [1233.0, 1233.0, 3234.4, 1111.1, 1223.3]]
        self.assertRaises(DatosInvalidos,
                          ganador_vuelta(ciclistas, tiempos))

        # Error parametro de entrada
        ciclistas = ['Miguel Indurain', 'Alberto Contador', 'Pedro Delgado']
        tiempos = [[1233.0, 1233.0, 3234.4, 1111.1, 1223.5],
                   [1233.0, 1233.0, 3234.4, 1111.1, 1223.2],
                   [1233.0, 1233.0, 3234.4, 1111.1, 1223.3]]
        self.assertRaises(TypeError,
                          ganador_vuelta(ciclistas, 3.141516))

        # Empate de los tres ciclistas
        ciclistas = ['Miguel Indurain', 'Alberto Contador', 'Pedro Delgado']
        tiempos = [[1233.0, 1233.0, 3234.4, 1111.1, 1223.5],
                   [1233.0, 1233.0, 3234.4, 1111.1, 1223.5],
                   [1233.0, 1233.0, 3234.4, 1111.1, 1223.5]]
        self.assertEqual(ganador_vuelta(ciclistas, tiempos),
                         ('Empatados: Miguel Indurain, Alberto Contador, '
                          'Pedro Delgado'))

        # Dos ganadores, empatados en primer lugar
        ciclistas = ['Miguel Indurain', 'Alberto Contador', 'Pedro Delgado']
        tiempos = [[1233.0, 1233.0, 3234.4, 1111.1, 1223.5],
                   [1233.0, 1233.0, 3234.4, 1111.1, 1223.2],
                   [1233.0, 1233.0, 3234.4, 1111.1, 1223.2]]
        self.assertEqual(ganador_vuelta(ciclistas, tiempos),
                         'Empatados: Alberto Contador, Pedro Delgado')


if __name__ == '__main__':
    main()
