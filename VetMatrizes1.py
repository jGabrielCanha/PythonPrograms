#Desenvolva um programa que leia pelo teclado os valores de uma matriz 3x3 (ou preencha com valores aleatórios), e então apresente um menu com as seguintes opções:
#Adição e subtração de outra matriz, lendo os valores dessa outra matriz 3x3 e mostrando o resultado na tela;
#Multiplicação e Divisão de um escalar lido pelo teclado;
#Multiplicação da matriz por um vetor de 3 elementos, este lido pelo teclado;
#Multiplicação da matriz por outra matriz 3x3, esta lida pelo teclado;
#Apresentar a transposta da matriz lida inicialmente.

import math

def read_vector():
    x = float(input("Digite o valor de x: "))
    y = float(input("Digite o valor de y: "))
    z = float(input("Digite o valor de z: "))
    return [x, y, z]

def calculate_vector_length(vector):
    return math.sqrt(sum(x ** 2 for x in vector))

def normalize_vector(vector):
    length = calculate_vector_length(vector)
    return [x / length for x in vector]

def add_vectors(vector1, vector2):
    return [x + y for x, y in zip(vector1, vector2)]

def subtract_vectors(vector1, vector2):
    return [x - y for x, y in zip(vector1, vector2)]

def multiply_vector_by_scalar(vector, scalar):
    return [x * scalar for x in vector]

def divide_vector_by_scalar(vector, scalar):
    return [x / scalar for x in vector]

def calculate_dot_product(vector1, vector2):
    return sum(x * y for x, y in zip(vector1, vector2))

def main():
    x, y, z = read_vector()

    while True:
        print("\nMenu:")
        print("1. Calcular o tamanho do vetor")
        print("2. Normalizar o vetor")
        print("3. Adicionar outro vetor")
        print("4. Subtrair outro vetor")
        print("5. Multiplicar vetor por escalar")
        print("6. Dividir vetor por escalar")
        print("7. Calcular produto escalar")
        print("8. Sair")

        choice = int(input("Escolha uma opção: "))

        if choice == 1:
            length = calculate_vector_length([x, y, z])
            print("O tamanho do vetor é:", length)
        elif choice == 2:
            normalized_vector = normalize_vector([x, y, z])
            print("Vetor normalizado:", normalized_vector)
        elif choice == 3:
            vector2 = read_vector()
            result = add_vectors([x, y, z], vector2)
            print("Resultado da adição:", result)
        elif choice == 4:
            vector2 = read_vector()
            result = subtract_vectors([x, y, z], vector2)
            print("Resultado da subtração:", result)
        elif choice == 5:
            scalar = float(input("Digite o valor do escalar: "))
            result = multiply_vector_by_scalar([x, y, z], scalar)
            print("Resultado da multiplicação:", result)
        elif choice == 6:
            scalar = float(input("Digite o valor do escalar: "))
            result = divide_vector_by_scalar([x, y, z], scalar)
            print("Resultado da divisão:", result)
        elif choice == 7:
            vector2 = read_vector()
            result = calculate_dot_product([x, y, z], vector2)
            print("Produto escalar:", result)
        elif choice == 8:
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
