def recommend(dfs,problemId):
  dfs.rename(columns = {'Unnamed: 0':'problemId'}, inplace = True)
  X = dfs.drop('problemId', axis=1)
  y = dfs['problemId']
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)
  model = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(X_train)
  model.kneighbors_graph(X_train).toarray()
  distances, indices = model.kneighbors(X_train)
  for i in range(len(distances)):
      if y_train.iloc[i] == problemId:
          return indices[i]


if __name__ == "__main__":
  dfs=pd.read_csv('/content/success_score.csv')
  ans=recommend(dfs,'6336b760ee62f10022c97c37')