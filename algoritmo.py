import problema
import random
import copy

class AlgoritmoGenetico():
    """docstring for AlgoritmoGenetico."""
    def __init__(self, populacao):
        self.populacao = populacao

    def pareia(self):
        popl = copy.deepcopy(self.populacao)
        adptPopl = [indv.adaptacao for indv in popl]
        pesos = [adptIndv/sum(adptPopl) for adptIndv in adptPopl]
        pares = []

        for i in range(0, int(len(popl)/2)):
            par = random.choices(
                population = popl,
                weights = pesos,
                k = 2
            )
            pares.append(par)
        return pares

    def reproduz(self, pares):
        nova_populacao
        for par in pares:
            corte = random.randrange(1,7)
            filho1 = par[0].rainhas[0:corte] + par[1].rainhas[corte:]
            filho2 = par[1].rainhas[0:corte] + par[0].rainhas[corte:]
            nova_populacao.append(filho1)
            nova_populacao.append(filho2)

    def mutacao(self, individuo, pmut):2
        cmut = random.uniform(0,1)
        if cmut >= pmut:
            return individuo
        x = random.randrange(0,7)
        y = random.randrange(1,8)

        rainhas[x] = y

        return rainhas
