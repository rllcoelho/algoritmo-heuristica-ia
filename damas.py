class Casa:
    def __init__(self, position, vizinho_se=None, vizinho_sd=None, vizinho_ie=None, vizinho_id=None, ocupado_por=0):
        self.position = position
        self.vizinho_se = vizinho_se
        self.vizinho_sd = vizinho_sd
        self.vizinho_ie = vizinho_ie
        self.vizinho_id = vizinho_id
        self.ocupado_por = ocupado_por


        
