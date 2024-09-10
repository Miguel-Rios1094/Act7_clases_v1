print("introduccion a clases")
class animal:
    edad=3
    raza="Chihuas"
    comida="croquetas"
    def come(self):
        print(f"El perro come "+self.comida)
        
print(animal)
print("Creando el obj de la clase animal")
perro=animal()
print(f"Edad del perro {perro.edad}")
print(f"Raza del perro {perro.raza}")
perro.come()