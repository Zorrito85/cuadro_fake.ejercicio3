class ObraArte:
    def __init__(self, titulo, ac, tecnica, subtecnica, soporte, autor, estado_conservacion,):
        self.titulo = titulo
        self.ac = ac
        self.tecnica = tecnica
        self.subtecnica = subtecnica
        self.soporte = soporte
        self.autor = autor
        self.estado_conservacion = estado_conservacion
        self.lugar = None

    def asignar_lugar(self, lugar):
        self.lugar = lugar

    def __str__(self):
        texto=(
            f"Título: {self.titulo}\n"
            f"Año de creación: {self.ac}\n"
            f"Técnica: {self.tecnica}\n"
            f"Subtécnica: {self.subtecnica}\n"
            f"Soporte: {self.soporte}\n"
            f"Autor: {self.autor}\n"
            f"Estado de conservación: {self.estado_conservacion}\n"
        )
        if self.lugar:
            texto += f"Lugar: {self.lugar}\n"
        return texto