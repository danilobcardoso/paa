#https://www.urionlinejudge.com.br/judge/pt/problems/view/2795

# Vou quebrando a sequencia até chegar em apenas um elemento
# Caso base: Toda string de um elemento é um palindromo
# Backtrack:
# Caso o bloco tem mais de uma letra tenho que:
# 1 - descobrir o custo de transformar o bloco em um palindromo e
# 2 - com k blocos tenho tres opções:
#        - mante-los separados
#        - juntar com o vizinho da esquerda
#       - juntar com o vizinho da direita


def calculate_distance(src, trg):
    return min(abs(ord(src) - ord(trg)), abs(abs(ord(src) - ord(trg)) - 26) )


def build_distance_matrix(word):
    distances = []
    for i in range(len(word)):
        col_distances = []
        for j in range(len(word)):
            col_distances.append(calculate_distance(word[i], word[j]))
        distances.append(col_distances)
    return distances


def build_palindrome_distances(distances):
    palindrome_distances = []
    n = len(distances)
    for palindrome_size in range(1,n+1):
        palindrome_distances_row = []
        for palindrome_index in range(n+1-palindrome_size):
            sum = 0
            for comp_positions in range(int((palindrome_size+1)/2)):
                a = palindrome_index + comp_positions
                b = palindrome_index + palindrome_size - comp_positions - 1
                sum += distances[a][b]
            palindrome_distances_row.append(sum)
        palindrome_distances.append(palindrome_distances_row)
    return palindrome_distances


def check_range(idx, bases, ranges):
    length = len(bases)
    for i in range(length):
        if (idx>=bases[i]) and (idx<bases[i]+ranges[i]):
            return False
    return True


def find_palindrome_cost(calculations, resta_no_vetor, blocos_restantes, closed_index, closed_ranges, cost_so_far):
    if resta_no_vetor == 0:
        return cost_so_far
    if blocos_restantes == 0:
        return -1

    cost = float('inf')
    for tamanho in range(resta_no_vetor, 0, -1):
        min_blocos_completar = resta_no_vetor / tamanho

        if min_blocos_completar > blocos_restantes:
            break;

        restara_no_vetor = resta_no_vetor - tamanho
        for j in range(len(calculations[tamanho-1])):
            if check_range(j, closed_index, closed_ranges):
                new_closed_index = closed_index + (j,)
                new_closed_range = closed_ranges + (tamanho,)
                curr_cost = find_palindrome_cost(calculations, restara_no_vetor, blocos_restantes-1, new_closed_index, new_closed_range, cost_so_far+calculations[tamanho-1][j])
                if curr_cost >= 0:
                    cost = min(cost, curr_cost)
    return cost


def print_matrix(matrix):
    for row in matrix:
        print(row)


##
def word_cost_to_palindrome(word, n, k):
    distances = build_distance_matrix(word)
    calculations = build_palindrome_distances(distances)
    print_matrix(calculations)
    cost = find_palindrome_cost(calculations, n, k, (0,), (-1,), 0)
    print(cost)
    return cost



params = input().split()
n = int(params[0])
k = int(params[1])
entrada = input()

print(word_cost_to_palindrome(entrada, n, k))
