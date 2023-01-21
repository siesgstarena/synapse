import pickle


def save_model(model, model_name):
    with open(model_name, "wb") as file:
        pickle.dump(model, file)
