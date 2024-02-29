"""importamos random para generar el juego de adivina el numero"""
import random

# declaramos variable que representa el numero del cpu
n_cpu = random.randrange(0, 10)
n_player = int(input("que numero piensa el cpu: "))
SALIDA = 0

while n_cpu != n_player:

    if n_player < n_cpu:
        print("El numero que ingresaste es muy bajo, intentalo de nuevo, vamos...")
        n_player = int(input("que numero piensa el cpu: "))
    elif n_player > n_cpu:
        print("El numero que ingresaste es muy alto, intentalo de nuevo, vamos...")
        n_player = int(input("que numero piensa el cpu: "))
    else:
        break
print("Has ganado...")
