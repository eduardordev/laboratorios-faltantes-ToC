import re
from itertools import product

# Función para leer gramática de un archivo de texto
def leer_gramatica(archivo):
    gramatica = {}
    with open(archivo, 'r', encoding='utf-8') as file:
        for linea in file:
            if '→' in linea:
                izquierda, derecha = linea.strip().split('→')
                izquierda = izquierda.strip()
                producciones = [p.strip() for p in derecha.split('|')]
                if izquierda not in gramatica:
                    gramatica[izquierda] = []
                gramatica[izquierda].extend(producciones)
    return gramatica

# Función para eliminar producciones-ε
def eliminar_producciones_epsilon(gramatica):
    anulables = set()
    for nt, producciones in gramatica.items():
        if 'ε' in producciones:
            anulables.add(nt)

    nuevos_prods = {nt: set() for nt in gramatica}
    for nt, producciones in gramatica.items():
        for prod in producciones:
            nuevos_prods[nt].add(prod)
            for i in range(1, len(prod) + 1):
                for comb in product([True, False], repeat=len(prod)):
                    if any(comb):
                        nueva_prod = ''.join([prod[j] for j in range(len(prod)) if not comb[j]])
                        if nueva_prod:
                            nuevos_prods[nt].add(nueva_prod)

    for nt in anulables:
        nuevos_prods[nt].discard('ε')
    return {nt: list(prods) for nt, prods in nuevos_prods.items()}

# Función para eliminar producciones unarias
def eliminar_producciones_unarias(gramatica):
    unarias = {nt: [prod for prod in prods if len(prod) == 1 and prod.isupper()] for nt, prods in gramatica.items()}
    for nt in gramatica:
        for prod in unarias[nt]:
            if prod in gramatica:
                gramatica[nt].extend([p for p in gramatica[prod] if p not in gramatica[nt]])
        gramatica[nt] = [p for p in gramatica[nt] if not (len(p) == 1 and p.isupper())]
    return gramatica

# Función para remover símbolos inútiles (no productivos e inalcanzables)
def remover_simbolos_inutiles(gramatica):
    productivos = set()
    cambio = True
    while cambio:
        cambio = False
        for nt, prods in gramatica.items():
            if nt not in productivos:
                for prod in prods:
                    if all(c.islower() or c in productivos for c in prod):
                        productivos.add(nt)
                        cambio = True
                        break

    gramatica = {nt: prods for nt, prods in gramatica.items() if nt in productivos}
    
    alcanzables = {'S'}
    cambio = True
    while cambio:
        cambio = False
        for nt in list(alcanzables):
            for prod in gramatica.get(nt, []):
                for c in prod:
                    if c.isupper() and c not in alcanzables:
                        alcanzables.add(c)
                        cambio = True

    gramatica = {nt: [prod for prod in prods if all(c in alcanzables or c.islower() for c in prod)]
                 for nt, prods in gramatica.items() if nt in alcanzables}
    return gramatica

# Función para convertir la gramática a la forma normal de Chomsky (CNF)
def convertir_a_cnf(gramatica):
    nuevas_reglas = {}
    nuevos_simbolos = {}
    contador = 0

    for nt, prods in gramatica.items():
        nuevas_reglas[nt] = []
        for prod in prods:
            if len(prod) == 1:
                nuevas_reglas[nt].append(prod)
            elif len(prod) == 2:
                nuevas_reglas[nt].append(prod)
            else:
                ultimo_simbolo = prod[0]
                for i in range(1, len(prod) - 1):
                    nuevo_nt = f"X{contador}"
                    contador += 1
                    nuevas_reglas[nuevo_nt] = [ultimo_simbolo + prod[i]]
                    ultimo_simbolo = nuevo_nt
                nuevas_reglas[nt].append(ultimo_simbolo + prod[-1])

    for nt, prods in nuevas_reglas.items():
        if nt not in gramatica:
            nuevos_simbolos[nt] = prods

    nuevas_reglas.update(nuevos_simbolos)
    return nuevas_reglas

archivo1 = 'gramatica1.txt'
archivo2 = 'gramatica2.txt'

gramatica1 = leer_gramatica(archivo1)
gramatica2 = leer_gramatica(archivo2)

print("Gramática 1 original:", gramatica1)
gramatica1 = eliminar_producciones_epsilon(gramatica1)
print("\nGramática 1 sin producciones-ε:", gramatica1)
gramatica1 = eliminar_producciones_unarias(gramatica1)
print("\nGramática 1 sin producciones unarias:", gramatica1)
gramatica1 = remover_simbolos_inutiles(gramatica1)
print("\nGramática 1 sin símbolos inútiles:", gramatica1)
gramatica1 = convertir_a_cnf(gramatica1)
print("\nGramática 1 en CNF:", gramatica1)

print("Gramática 2 original:", gramatica2)
gramatica1 = eliminar_producciones_epsilon(gramatica2)
print("\nGramática 2 sin producciones-ε:", gramatica2)
gramatica1 = eliminar_producciones_unarias(gramatica2)
print("\nGramática 2 sin producciones unarias:", gramatica2)
gramatica1 = remover_simbolos_inutiles(gramatica2)
print("\nGramática 2 sin símbolos inútiles:", gramatica2)
gramatica1 = convertir_a_cnf(gramatica2)
print("\nGramática 2 en CNF:", gramatica2)
