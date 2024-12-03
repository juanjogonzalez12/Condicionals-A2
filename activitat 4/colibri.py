class Colibri:
    def __init__(self, especie, plomatge, mida, pes):
        self._especie = especie
        self._plomatge = plomatge
        self._mida = mida
        self._pes = pes

    def get_especie(self):
        return self._especie
    
    def get_plomatge(self):
        return self._plomatge
    
    def get_mida(self):
        return self._mida
    
    def get_pes(self):
        return self._pes
    

    def set_especie(self, especie):
        self._especie = especie
    
    def set_plomatge(self, plomatge):
        self._plomatge = plomatge
    
    def set_mida(self, mida):
        self._mida = mida
    
    def set_pes(self, pes):
        self._pes = pes