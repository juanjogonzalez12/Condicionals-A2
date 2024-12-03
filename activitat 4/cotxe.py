class Cotxe:
    def __init__(self, marca, model, color):
        self._marca = marca
        self._model = model
        self._color = color

    def get_marca(self):
        return self._marca
    
    def get_model(self):
        return self._model
    
    def get_color(self):
        return self._color
    

    def set_marca(self, marca):
        self._marca = marca
    
    def set_model(self, model):
        self._model = model
    
    def set_color(self, color):
        self._color = color