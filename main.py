"""
Ejercicio Bola de Cristal

Una `BolaDeCristal` es un artefacto que te permite ver cuál será tu próxima mascota al enviarle el mensaje `adivinar_el_futuro`, utilizando la api: [https://dog.ceo/api/breeds/image/random](https://dog.ceo/api/breeds/image/random) 
Definí los atributos y métodos necesarios para que el objeto se comporte como se dijo anteriormente.

"""

import requests 

class BoladeCristal:
    def __init__(self):
        self.perrito = ""
    
    def adivinar_el_futuro(self):
        url = "https://dog.ceo/api/breeds/image/random"
        peticion = requests.get(url).json()
        self.perrito = peticion["message"]
        print(self.perrito)
        
BoladeCristal_Andy = BoladeCristal()
print(BoladeCristal_Andy.adivinar_el_futuro())
        
