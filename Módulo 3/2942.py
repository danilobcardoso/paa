# https://www.urionlinejudge.com.br/judge/en/problems/view/2942
def bit_mix(array,i):
    value = array[i-1] ^ array[i]
    value = value ^ array[i+1]
    array[i] = value


instancias = int(input())
origem = input()
origem = list(map(int, origem.split()))
objetivo = input()
objetivo = list(map(int, objetivo.split()))

bit_mix(origem,1)
print(origem)