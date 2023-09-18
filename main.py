# Capa de Datos - Definición de las clases
class Persona:
    def __init__(self, cod_persona, nombre, apellido_paterno, apellido_materno, fecha_nacimiento):
        self.cod_persona = cod_persona
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.fecha_nacimiento = fecha_nacimiento

class Libro:
    def __init__(self, codigo_libro, titulo, ano, tomo):
        self.codigo_libro = codigo_libro
        self.titulo = titulo
        self.ano = ano
        self.tomo = tomo

class Categoria:
    def __init__(self, cod_categoria, categoria):
        self.cod_categoria = cod_categoria
        self.categoria = categoria

class Autor:
    def __init__(self, cod_autor, pais, editorial):
        self.cod_autor = cod_autor
        self.pais = pais
        self.editorial = editorial

# Capa de Negocios - Gestor de Mantenimiento y operaciones CRUD
class GestorMantenimiento:
    def __init__(self):
        self.personas = []
        self.libros = []
        self.categorias = []
        self.autores = []

    # Métodos para guardar registros
    def guardar_persona(self, cod_persona, nombre, apellido_paterno, apellido_materno, fecha_nacimiento):
        persona = Persona(cod_persona, nombre, apellido_paterno, apellido_materno, fecha_nacimiento)
        self.personas.append(persona)

    def guardar_libro(self, codigo_libro, titulo, ano, tomo):
        libro = Libro(codigo_libro, titulo, ano, tomo)
        self.libros.append(libro)

    def guardar_categoria(self, cod_categoria, categoria):
        categoria_obj = Categoria(cod_categoria, categoria)
        self.categorias.append(categoria_obj)

    def guardar_autor(self, cod_autor, pais, editorial):
        autor = Autor(cod_autor, pais, editorial)
        self.autores.append(autor)

    # Métodos para editar registros
    def editar_persona(self, cod_persona, nombre, apellido_paterno, apellido_materno, fecha_nacimiento):
        for persona in self.personas:
            if persona.cod_persona == cod_persona:
                persona.nombre = nombre
                persona.apellido_paterno = apellido_paterno
                persona.apellido_materno = apellido_materno
                persona.fecha_nacimiento = fecha_nacimiento
                break

    def editar_libro(self, codigo_libro, titulo, ano, tomo):
        for libro in self.libros:
            if libro.codigo_libro == codigo_libro:
                libro.titulo = titulo
                libro.ano = ano
                libro.tomo = tomo
                break

    def editar_categoria(self, cod_categoria, categoria):
        for categoria_obj in self.categorias:
            if categoria_obj.cod_categoria == cod_categoria:
                categoria_obj.categoria = categoria
                break

    def editar_autor(self, cod_autor, pais, editorial):
        for autor in self.autores:
            if autor.cod_autor == cod_autor:
                autor.pais = pais
                autor.editorial = editorial
                break

    # Métodos para eliminar registros
    def eliminar_persona(self, cod_persona):
        persona = next((p for p in self.personas if p.cod_persona == cod_persona), None)
        if persona:
            self.personas.remove(persona)

    def eliminar_libro(self, codigo_libro):
        libro = next((l for l in self.libros if l.codigo_libro == codigo_libro), None)
        if libro:
            self.libros.remove(libro)

    def eliminar_categoria(self, cod_categoria):
        categoria_obj = next((c for c in self.categorias if c.cod_categoria == cod_categoria), None)
        if categoria_obj:
            self.categorias.remove(categoria_obj)

    def eliminar_autor(self, cod_autor):
        autor = next((a for a in self.autores if a.cod_autor == cod_autor), None)
        if autor:
            self.autores.remove(autor)

    # Métodos para obtener registros
    def obtener_personas(self):
        return self.personas

    def obtener_libros(self):
        return self.libros

    def obtener_categorias(self):
        return self.categorias

    def obtener_autores(self):
        return self.autores

# Crear una instancia de GestorMantenimiento
gestor = GestorMantenimiento()

# Ejemplo de creación de registros
gestor.guardar_persona(1, "Juan", "Perez", "Gomez", "2000-01-01")
gestor.guardar_libro(1, "El Libro de la Selva", 1894, "I")
gestor.guardar_categoria(1, "Ficción")
gestor.guardar_autor(1, "Estados Unidos", "Editorial Hinostroza")

# Ejemplo de obtención y muestra de registros
personas = gestor.obtener_personas()
for persona in personas:
    print(f"Código: {persona.cod_persona}, Nombre: {persona.nombre}, Apellidos: {persona.apellido_paterno} {persona.apellido_materno}")

libros = gestor.obtener_libros()
for libro in libros:
    print(f"Código: {libro.codigo_libro}, Título: {libro.titulo}, Año: {libro.ano}, Tomo: {libro.tomo}")

categorias = gestor.obtener_categorias()
for categoria in categorias:
    print(f"Código: {categoria.cod_categoria}, Categoría: {categoria.categoria}")

autores = gestor.obtener_autores()
for autor in autores:
    print(f"Código: {autor.cod_autor}, País: {autor.pais}, Editorial: {autor.editorial}")
