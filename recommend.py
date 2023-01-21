import pickle
import numpy as np
def load_model(model_name):
    with open(model_name,'rb') as file:
        model = pickle.load(file)
    return model

def recommend(id):
   sim = load_model('similarities.pkl')
   return sim[id]


if __name__ == "__main__":
    print(recommend('5b5c8cd7276e2200208fed62'))