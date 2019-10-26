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

class PalindromeCost:
    def __init__(self, inicio, tamanho, custo):
        self.inicio = inicio;
        self.fim = inicio + tamanho;
        self.custo = custo;
        self.tamanho = tamanho;

    def __str__(self):
        return "({0},{1},{2})".format(self.inicio, self.fim, self.custo)


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


def build_palindrome_costs(distances):
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
            palindrome_distances_row.append(PalindromeCost(palindrome_index, palindrome_size, sum))
        palindrome_distances.append(palindrome_distances_row);
    return palindrome_distances


def init_solution_matrix(distances):
    palindrome_distances = []
    n = len(distances)
    for palindrome_size in range(1,n+1):
        palindrome_distances_row = []
        for palindrome_index in range(n+1-palindrome_size):
            palindrome_distances_row.append(float('inf'))
        palindrome_distances.append(palindrome_distances_row);
    return palindrome_distances



def print_matrix(matrix):
    print('-----------')
    for row in matrix:
        temp = ''
        for item in row:
            temp += ' \t ' + str(item)
        print(temp)

def get_complement(matrix, l, c, n, offe=0, offd=0):
    se = c - offe
    sd = n - l - c - offd - 1
    ve = 0
    if se-1>offe:
        ve = matrix[se-1][offe].custo
    vd = 0
    if sd-1>offd:
        vd = matrix[sd-1][n - sd].custo
    return ve + vd

def get_right_complement(matrix, l, c, n, offd=0):
    sd = n - l - c - offd - 1
    vd = PalindromeCost(0, 0, 0)
    if sd-1>=offd:
        vd = matrix[sd-1][n - sd]
    return vd, sd, n - sd


def tentativa_5(solutions, calculations, n, t):
    raiz = calculations[t - 1][n - t]
    if t==1:
        solutions[t-1][n-t] = raiz.custo
    else:
        solutions[t - 1][n - t] = raiz.custo
        for l in range(raiz.tamanho - 1):
            teste = calculations[l][n - t]
            if l==0:
                solutions[l][n - t] = teste.custo
            else:
                minimo = float('inf')
                for j in range(0,l+1):
                    temp = calculations[j][n - t]
                    minimo = min(minimo, temp.custo + solutions[l-j][n-t+1+j])
                solutions[l][n - t] = minimo


def word_cost_to_palindrome(word, n, k, debug=False):
    distancias = build_distance_matrix(word)
    calculos = build_palindrome_costs(distancias)
    solucoes = init_solution_matrix(distancias)
    if debug:
        print_matrix(calculos)

    for i in range(n):
        tentativa_5(solucoes, calculos, n, i+1)
        if debug:
            print_matrix(solucoes)

    minimal = float('inf')
    for i in range(n-1,n-k-1,-1):
        minimal = min(minimal, solucoes[i][0])

    print(minimal)



params = input().split()
n = int(params[0])
k = int(params[1])
entrada = input()

word_cost_to_palindrome(entrada, n, k)
