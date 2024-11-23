class Asignatura:

    def __init__(self, nombre, salon="remoto"): #Salida predeterminada si la clase no se hace en un salón
        self._nombre = nombre;
        self._salon = salon;

    def __str__(self): #Inicialmente se remueven los comentarios
        return f"{self._nombre} {self._salon}"; #Ahora esto va a devolver "Matemáticas remoto" et. al.