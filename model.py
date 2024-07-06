from langchain.llms import Ollama

class Model:
    def __init__(self, model):
        self.model = Ollama(model=model)

