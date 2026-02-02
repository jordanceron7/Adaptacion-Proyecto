# Dashboard.py
# Adaptado por: Jordan Anderson Cerón Díaz
# Materia: Programación Orientada a Objetos
# Universidad Estatal Amazónica

class Tarea:
    def __init__(self, titulo, descripcion, estado="Pendiente"):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado

    def completar(self):
        self.estado = "Completada"


class Proyecto:
    def __init__(self, nombre, materia):
        self.nombre = nombre
        self.materia = materia
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def mostrar_tareas(self):
        print(f"\nProyecto: {self.nombre}")
        for i, tarea in enumerate(self.tareas, 1):
            print(f"{i}. {tarea.titulo} - {tarea.estado}")


class Dashboard:
    def __init__(self, estudiante):
        self.estudiante = estudiante
        self.proyectos = []

    def agregar_proyecto(self, proyecto):
        self.proyectos.append(proyecto)

    def mostrar_dashboard(self):
        print("\n===== DASHBOARD DE PROGRAMACIÓN ORIENTADA A OBJETOS =====")
        print(f"Estudiante: {self.estudiante}")
        print("Proyectos registrados:")

        for proyecto in self.proyectos:
            proyecto.mostrar_tareas()


# ------------------ PROGRAMA PRINCIPAL ------------------

# Crear tareas
tarea1 = Tarea("Investigar POO", "Conceptos básicos de POO")
tarea2 = Tarea("Modificar Dashboard.py", "Adaptar el proyecto a necesidades propias")

# Crear proyecto
proyecto_poo = Proyecto("Proyecto POO", "Programación Orientada a Objetos")
proyecto_poo.agregar_tarea(tarea1)
proyecto_poo.agregar_tarea(tarea2)

# Crear dashboard
dashboard = Dashboard("Jordan Anderson Cerón Díaz")
dashboard.agregar_proyecto(proyecto_poo)

# Mostrar información
dashboard.mostrar_dashboard()
