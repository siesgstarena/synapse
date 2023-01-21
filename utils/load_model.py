import pickle


def load_model(model_name):
    with open(model_name, "rb") as file:
        model = pickle.load(file)
    return model
