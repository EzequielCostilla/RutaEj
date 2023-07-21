import json


class RutaVisita:
    """ Rutas de visitas. """

    def __init__(self, id, nombre, destinos):
        """ Inicializa los atributos. """
        self.id = id
        self.nombre = nombre
        self.destinos = destinos

    def a_json(self):
        """ Convierte a un diccionario los atributos de esta clase. """
        return {
            "id" : self.id,
            "nombre" : self.nombre,
            "destinos" : self.destinos
        }

destinos1 = (1, 2, 3)
destinos2 = (5, 2, 4)
destinos3 = (7, 1, 6)
destinos4 = (4, 5, 6)
ruta1 = RutaVisita(1, "ruta 1", destinos1)
ruta2 = RutaVisita(2, "ruta 2", destinos2)
ruta3 = RutaVisita(3, "ruta 3", destinos3)
ruta4 = RutaVisita(4, "ruta 4", destinos4)

def convert_json_ruta_visita(ruta):
    """ Convierte una ruta en un objeto json. """
    ruta_visita_json = json.dumps(ruta.a_json())
    print(ruta_visita_json)


convert_json_ruta_visita(ruta1)
convert_json_ruta_visita(ruta2)
convert_json_ruta_visita(ruta3)
convert_json_ruta_visita(ruta4)
