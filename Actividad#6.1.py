class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color 
        self.ruedas = ruedas
        self.puertas = puertas
        
        
    def __str__(self):
        return "Color {}, {} ruedas".format(self.color,self.ruedas,self.puertas )
        
class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindraje):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindrada = cilindraje
        
    def __str__(self):
        return "color {}, {} km/h, {} ruedas, {} puertas, {} cc".format( self.color, self.velocidad, self.ruedas, self.puertas, self.cilindrada )


coche = Coche("rojo", 5, 7, 50, 1500)
print(coche)
