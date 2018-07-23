import random

class OitoRainhas():
    """docstring for OitoRainhas."""
    def __init__(self):
        self.rainhas = []
        for linha in range(8):
            self.rainhas += [int(random.randrange(1,8))]
        self.adaptacao = None

    def calculaAdaptacao(self):
        adaptacao = 28
        for i in range(0, len(self.rainhas)):
            for j in range(i+1, len(self.rainhas)):
                if self.rainhas[i] == self.rainhas[j]:
                    adaptacao -= 1
                elif abs((self.rainhas[i]-self.rainhas[j])/float(i-j))==1:
                    adaptacao -=1
        self.adaptacao = adaptacao
        return adaptacao

    def setRainhas(self, rainhas):
        if len(rainhas) != 8:
            return None
        else:
            for rainha in rainhas:
                if rainha > 8 or rainha < 1:
                    return None
        self.rainhas = rainhas
