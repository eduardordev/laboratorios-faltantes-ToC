
D = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Apple', 'model': 2, 'color': 'Silver'},
    {'make': 'Huawei', 'model': 50, 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

D_sorted = sorted(D, key=lambda x: x['model'])

print("Ejercicio 1 - Lista ordenada:")
print(D_sorted)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3 

result = list(map(lambda x: x ** n, nums))

print("\nEjercicio 2 - Potencia n-ésima de la lista:")
print(result)

X = [
    [1, 2, 3, 1],
    [4, 5, 6, 0],
    [7, 8, 9, -1]
]

transpose = lambda matrix: [list(row) for row in zip(*matrix)]

print("\nEjercicio 3 - Matriz transpuesta:")
print(transpose(X))

initial_list = ['rojo', 'verde', 'azul', 'amarillo', 'gris', 'blanco', 'negro']
elements_to_remove = ['amarillo', 'café', 'blanco']

filtered_list = list(filter(lambda x: x not in elements_to_remove, initial_list))

print("\nEjercicio 4 - Lista después de eliminar elementos:")
print(filtered_list)
