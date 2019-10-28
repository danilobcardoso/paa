## https://www.urionlinejudge.com.br/judge/pt/problems/view/1382



def numero_trocas(permutacao):
    visitados = [0 for i in range(len(permutacao))]
    ciclos = []
    for i in range(len(permutacao)):
        if visitados[i] == 0:
            count = 0
            next_step = i
            while (visitados[next_step] == 0):
                visitados[next_step] = 1
                next_step = permutacao[next_step]-1
                count += 1
            count -= 1
            if count > 0:
                ciclos.append(count)
    total = sum(ciclos)
    return total




instancias = int(input())
for instancia in range(instancias):
    tamanho = int(input())
    permutacao = input()
    permutacao = list(map(int, permutacao.split()))

    print(numero_trocas(permutacao))
