from classroom.asignatura import Asignatura;

class Grupo:
    grado = "Grado 12"; #Este es un valor predeterminado
                    #Aquí abajo debe decir grupo predeterminado
    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo;
        self._asignaturas = asignaturas if asignaturas is not None else []; #La lista se actualiza si hay estudiantes
        self.listadoAlumnos = estudiantes if estudiantes is not None else []; #Lo de arriba

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista==None:
            lista=[]
        lista.append(alumno)
        self.listadoAlumnos += lista

    def __str__(self):
        return f"Grupo de estudiantes: {self._grupo}";

    #@ classmethod
    #def asignarNombre(cls, nombre="Grado 10"): Se quita para que el predeterminado sea el 6
    #    cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    #@ classmethod
    #def asignarNombre(cls, nombre="Grado 4"): Se quita para que el predeterminado sea el 6
    #    cls.grado = nombre