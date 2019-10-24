## https://www.urionlinejudge.com.br/judge/pt/problems/view/1382


def trocas_possiveis(permutacao):
    trocas_duplas = []
    trocas_simples = []
    for idx in range(len(permutacao)-1):
        idx_ida = idx
        idx_volta = permutacao[idx_ida] - 1
        if (idx_volta == permutacao[idx_ida] - 1) and (idx_ida == permutacao[idx_volta] - 1):
            if idx_volta > idx_ida:
                trocas_duplas.append((idx_ida, idx_volta))
        elif idx != (permutacao[idx_ida]-1):
            trocas_simples.append((idx_ida, idx_volta))
    return trocas_duplas, trocas_simples



def numero_trocas(permutacao):
    trocas_duplas, trocas_simples = trocas_possiveis(permutacao)
    count = 0

    while (len(trocas_duplas)>0) or (len(trocas_simples)>0):
        if len(trocas_duplas)>0:
            for x, y in trocas_duplas:
                permutacao[x], permutacao[y] = permutacao[y], permutacao[x]
                count += 1
        elif len(trocas_simples)>0:
            x, y = trocas_simples[0]
            permutacao[x], permutacao[y] = permutacao[y], permutacao[x]
            count += 1
        trocas_duplas, trocas_simples = trocas_possiveis(permutacao)

    return count



instancias = int(input())
for instancia in range(instancias):
    tamanho = int(input())
    permutacao = input()
    permutacao = list(map(int, permutacao.split()))

    print(numero_trocas(permutacao))
