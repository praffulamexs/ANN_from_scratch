class HiddenLayer():
    def __init__(self, number):
        super().__init__()
        self.neurons = []
    
    def __repr__(self):
        return self.neurons