import pickle
from collections import defaultdict
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier as KNN
def load_model(model_name):
    with open(model_name) as file:
        model = pickle.load(model_name)
    return model
def knn_recommend(problemId, n_neighbors,df, knn):
    Y = df['problemId']
    to_predict = np.array(df[df['problemId']==problemId].drop('problemId', axis=1)).reshape(1, -1)
    distances, indices = knn.kneighbors(to_predict, n_neighbors=n_neighbors+1)
    rec = []
    for i in indices[0]:
        if Y.iloc[i] != problemId:
            rec.append(Y.iloc[i])
    return rec
def save_sim(sim,filename):
  with open(filename,"wb") as filename:
    pickle.dump(sim,filename)
if __name__ == "__main__":
  df=pd.read_csv('success_score.csv')
  df.rename(columns = {'Unnamed: 0':'problemId'}, inplace = True)
  sim = defaultdict(list)
  for j in df['problemId']:
    sim[j].append(knn_recommend(j, 3 , df , load_model('knn_model_3_ball_tree')))
  save_sim(sim,'similarities.pkl')