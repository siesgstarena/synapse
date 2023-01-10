import pickle
import numpy as np
def load_model(model_name):
    with open(model_name) as file:
        model = pickle.load(file)
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


if __name__ == "__main__":
  df=pd.read_csv('/content/success_score.csv')
  df.rename(columns = {'Unnamed: 0':'problemId'}, inplace = True)
  knn_recommend('6336b760ee62f10022c97c37', 3,df, load_model('knn_model_3_ball_tree'))