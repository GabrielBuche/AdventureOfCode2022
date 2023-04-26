with open('data.in') as file:
    content = [i for i in file.read().strip().split('\n')]

pares = []
for string in content:
    partes = string.split(",")
    pares.append((tuple(map(int, partes[0].split("-"))), tuple(map(int, partes[1].split("-")))))


def intervalo_contido(total, parcial):
    """
    Verifica se o intervalo total está totalmente contido no intervalo parcial.
    """
    inicio_total, fim_total = total
    inicio_parcial, fim_parcial = parcial
    return inicio_parcial <= inicio_total and fim_parcial >= fim_total

def contar_pares_de_reconsideracao(pares):
    """
    Conta quantos pares de atribuição de seção precisam de reconsideração.
    """
    reconsideracao = 0
    for i in range(len(pares)):
        for j in range(i+1, len(pares)):
            par_a = pares[i]
            par_b = pares[j]
            if intervalo_contido(par_a, par_b):
                reconsideracao += 1
            elif intervalo_contido(par_b, par_a):
                reconsideracao += 1
    return reconsideracao

reconsideracao = contar_pares_de_reconsideracao(pares)
print(reconsideracao)