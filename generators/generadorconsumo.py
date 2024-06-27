import random

def generarDatos():
    datos=[]

    for i in range (5000):
        dato={}
        id=random.randint(1,10000)
        referencia=random.choice(["ACH01,ACH22,ACH43"])
        marca=random.choice(["sony, rico, kelley"])
        capacidad=random.randint(100, 2000)
        ciudad=random.choice(["Medellin, Bogota, Cali, Barranquilla, Cartagena"])
        responsable=random.choice(["jaime arenas, estefa zapata, dairon rodriguez, coman mamey, erika correa"])

        dato=[id,referencia,marca,capacidad,ciudad,responsable]

        datos.append(dato)
    
    return datos

print(generarDatos())