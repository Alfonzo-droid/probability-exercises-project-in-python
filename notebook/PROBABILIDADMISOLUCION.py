# Ejercicios de probabilidad

## Ejercicio 1 

#Dos dados se lanzan una vez y se observa el total obtenido. Usa una simulación para encontrar la probabilidad estimada de que la puntuación sea mayor a 7 o un número par. Una simulación es una repetición del mismo experimento multiples veces para observar su comportamiento:

#- Ejecuta el experimento 1000 veces (lanza 2 dados 1000 veces, y suma el número de ambos dados).
#- Lleva una cuenta de los números y las veces que la suma fue mayor a 7 o un número par.
#- Divide el número del paso 2 entre el número de iteraciones(1000).


# TODO
import numpy as np

trials = 1000

dado1 = [1,2,3,4,5,6]
dado2 = [1,2,3,4,5,6]

Sumatoria = []
Contador = 0
for i in range(trials):
    seleccion = np.random.choice(dado1)
    seleccion2 = np.random.choice(dado2)
    suma = seleccion + seleccion2
    Sumatoria.append(suma)

    if suma > 7  or suma % 2 ==0:
        Contador = Contador + 1


#EJERCICIO 1
print(Sumatoria)

#EJERCICIO 2
print(Contador)

#EJERCICIO 3
print("La probabilidad de que se generen numeros mayores a 7 o pares de la suma de los dados es" , Contador/trials)



## Ejercicio 2

#Una caja contiene 10 bolas blancas, 20 bolas rojas y 30 bolas verdes. Si tomamos 5 bolas de la caja reemplazándolas (tomando una bola, anotando el color y luego regresandola a la caja). Queremos saber la probabilidad de:

#1. Tomar 3 blancas y 2 rojas.
#2. Tomar todas del mismo color.

#Ejecuta el experimento 1000 veces y calcula las probabilidades que mencionadas.


ball_box = {}

# Crea la cajas con las bolas
for i in range(60):
    if i < 10:
        ball_box[i] = "White"
    elif (i > 9) and (i < 30):
        ball_box[i] = "Red"
    else:
        ball_box[i] = "Green"

print(ball_box)
            
# TODO



def tomar_bola(simulaciones = 1000):
    contador1 = 0
    contador2 = 0

    for i in range(simulaciones):
        colors = []

        # Take 5 balls from the box
        for i in range(5):
            colors.append(ball_box[np.random.randint(0, 59)])

        # Convert list to Numpy array for better filtering
        colors = np.array(colors)
        
        white_balls = sum(colors == "White")
        red_balls = sum(colors == "Red")
        green_balls = sum(colors == "Green")

        # Decide if we should add it to the count:
        if (white_balls == 3) and (red_balls == 2):
            contador1 += 1
        
        if (white_balls == 5) or (red_balls == 5) or (green_balls == 5):
            contador2 += 1
    
    return contador1 / simulaciones, contador2 / simulaciones
    
probabilidades = tomar_bola(simulaciones = 1000)

print(f"The probability of 3 white and 2 red is:{np.round(probabilidades[0] * 100, 2)}%")
print(f"The probability of all the same color is:{np.round(probabilidades[1] * 100, 2)}%")