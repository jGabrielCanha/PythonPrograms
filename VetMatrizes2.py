# Desenvolva um programa que leia pelo teclado os valores x, y e z de um vetor de 3 dimensões (ou preencha com valores aleatórios). Em seguida, apresente ao usuário um menu com as seguintes opções:
#Calcular o tamanho do vetor;
#Normalizar o vetor, apresentando o vetor resultante da normalização;
#Adicionar outro vetor ao que foi lido anteriormente, lendo os valores x, y e z deste novo vetor;
#Subtrair outro vetor ao que foi lido anteriormente, lendo os valores x, y e z deste novo vetor;
#Ler o valor de um escalar e realizar a multiplicação do mesmo pelo vetor, mostrando o vetor resultante;
#Ler o valor de um escalar e realizar a divisão do mesmo pelo vetor, mostrando o vetor resultante;
#Calcular o produto escalar do vetor lido anteriormente por outro vetor, lendo os valores x, y e z deste novo vetor e mostrando o resultado na tela.

def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = float(input(f"Digite o valor para a posição ({i+1}, {j+1}): "))
            row.append(value)
        matrix.append(row)
    return matrix

def add_matrices(matrix1, matrix2):
    return [[x + y for x, y in zip(row1, row2)] for row1, row2 in zip(matrix1, matrix2)]

def subtract_matrices(matrix1, matrix2):
    return [[x - y for x, y in zip(row1, row2)] for row1, row2 in zip(matrix1, matrix2)]

def multiply_matrix_by_scalar(matrix, scalar):
    return [[x * scalar for x in row] for row in matrix]

def multiply_matrix_by_vector(matrix, vector):
    return [sum(matrix[i][j] * vector[j] for j in range(len(vector))) for i in range(len(matrix))]

def multiply_matrices(matrix1, matrix2):
    return [[sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2[0]))) for j in range(len(matrix2[0]))] for i in range(len(matrix1))]

def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def print_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    rows, cols = 3, 3
    matrix = []

    while True:
        print("\nMenu:\n1. Adição\n2. Subtração\n3. Multiplicação escalar\n4. Multiplicação vetor\n5. Multiplicação matriz\n6. Transposta\n7. Sair")
        choice = int(input("Escolha uma opção: "))
        
        if choice == 7:
            print("Saindo do programa.")
            break
        
        if choice == 1 or choice == 2 or choice == 5:
            matrix = read_matrix(rows, cols)
        
        if choice == 1:
            other_matrix = read_matrix(rows, cols)
            result = add_matrices(matrix, other_matrix)
            print_matrix(result)
        elif choice == 2:
            other_matrix = read_matrix(rows, cols)
            result = subtract_matrices(matrix, other_matrix)
            print_matrix(result)
        elif choice == 3:
            scalar = float(input("Digite o valor do escalar: "))
            result = multiply_matrix_by_scalar(matrix, scalar)
            print_matrix(result)
        elif choice == 4:
            vector = [float(input(f"Digite o valor do elemento {i+1} do vetor: ")) for i in range(rows)]
            result = multiply_matrix_by_vector(matrix, vector)
            print(result)
        elif choice == 5:
            other_matrix = read_matrix(cols, rows)
            result = multiply_matrices(matrix, other_matrix)
            print_matrix(result)
        elif choice == 6:
            result = transpose_matrix(matrix)
            print_matrix(result)
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
