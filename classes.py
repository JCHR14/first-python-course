
class Persona:
    NACIONALIDAD = 'Honduras'

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def greetings(self):
        return f'Hi {self.first_name} {self.last_name}'


class Policia(Persona):
    def __init__(self, first_name, last_name, age, rango):
        super().__init__(first_name, last_name, age)
        self.rango = rango
    
    def mi_rango(self):
        return f'{self.rango}'



policia = Policia('Juan Carlos', 'Hernandez Reyes', 26, 'rango')
print(policia.mi_rango())