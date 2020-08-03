class Neuron:
    def __init__(self):
        super().__init__()
        self.bias = None
        self.weights = None
        self.activation_function = None
        self.inputs = None

    def set_inputs(self, inputs):
        self.inputs = inputs

    def set_activation_function(self, function):
        self.activation_function = function