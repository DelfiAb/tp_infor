#objetos:

class Video:
    def __init__(self, titulo, categoria, fecha_publicacion, rating):
        self.titulo = titulo
        self.categoria = categoria
        self.fecha_publicacion = fecha_publicacion
        self.rating = rating

    def __str__(self):
        return f'-------------------------' \
               f'\nNombre: {self.titulo}' \
               f'\nCategoria: {self.categoria}' \
               f'\nAño: {self.fecha_publicacion}' \
               f'\nRating: {self.rating}'\

class Pelicula(Video):
    def __init__(self, titulo, categoria, fecha_publicacion, rating, duracion, director, sinopsis):
        super().__init__(titulo, categoria, fecha_publicacion, rating)
        self.duracion = duracion
        self.director = director
        self.sinopsis = sinopsis

    def __str__(self):
        return super().__str__() + f'\nDuracion: {self.duracion}'+ f'\nDirector: {self.director}'f'\nSinopsis: {self.sinopsis}'

class Serie(Video):
    def __init__(self, titulo, categoria, fecha_publicacion, rating, temporada, capitulo, sinopsis):
        super().__init__(titulo, categoria, fecha_publicacion, rating)
        self.temporada = temporada
        self.capitulo = capitulo
        self.sinopsis = sinopsis

    def __str__(self):
        return super().__str__() + f'\nTemporada: {self.temporada}'+ f'\nCapitulo: {self.capitulo}'f'\nSinopsis: {self.sinopsis}'

class Usuarios():
    def __init__(self, nombre, apellido, nombre_usuario, direccion_email, contrasena):
       self.nombre = nombre
       self.apellido = apellido
       self.nombre_usuario = nombre_usuario
       self.direccion_email = direccion_email
       self.contrasena = contrasena

    def __str__(self):
        return f'-------------------------' \
               f'\nNombre: {self.nombre}' \
               f'\nApellido: {self.apellido}' \
               f'\nNombre de usuario: {self.nombre_usuario}' \
               f'\nDireccion de e-mail: {self.direccion_email}' \
               f'\nContraseña: {self.contrasena}'\


