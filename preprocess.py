import math
import pandas as pd
import numpy as np
from operator import itemgetter
from sklearn.preprocessing import Normalizer
def prepro(submission_df):
  TO_REMOVE = ["__v","_id","contestId","createdAt","duringContest","fileContent","memory","output","points","time","updatedAt","userId"]
  df = submission_df.drop(TO_REMOVE, axis=1)
  TO_REPLACE = ["Wrong Answer","Runtime Error","Time Limit Exceeded","Compilation Error"]
  REPLACE_WITH = "Not Accepted" 
  df.replace(TO_REPLACE,REPLACE_WITH,inplace=True)
  TO_REPLACE_LANGUAGE = ["C++14"]
  REPLACE_WITH_LANGUAGE = "C++"
  df.replace(TO_REPLACE_LANGUAGE,REPLACE_WITH_LANGUAGE,inplace=True)
  UNIQUE_PROBLEMS = df.problemId.unique()
  group_language = df.groupby(["language","status","problemId"]).size().reset_index(name="count")
  group_prob_status = df.groupby(["problemId","status"]).count()
  group_prob_status.reset_index(inplace=True)
  TO_REPLACE_STATUS = ["Accepted","Not Accepted"]
  REPLACE_WITH_STATUS = [1,0]
  group_prob_status.replace(TO_REPLACE_STATUS,REPLACE_WITH_STATUS,inplace=True)
  problem_group_language = dict()

  for problem in UNIQUE_PROBLEMS:
      problem_group_language[problem] = {
          1 : group_prob_status[group_prob_status.problemId == problem].language.values[0] if (group_prob_status[group_prob_status.problemId == problem].status == 1).any() else 0,
          0 : group_prob_status[group_prob_status.problemId == problem].language.values[1] if len(group_prob_status[group_prob_status.problemId == problem].language.values) > 1 else group_prob_status[group_prob_status.problemId == problem].language.values[0] if (group_prob_status[group_prob_status.problemId == problem].status == 0).any() else 0
      }
  group_language.replace(TO_REPLACE_STATUS,REPLACE_WITH_STATUS,inplace=True)
  problem_group_particular_language = dict()

  for problem in UNIQUE_PROBLEMS:
      problem_group_particular_language[problem] = {
          'Python3':{
          1 : group_language[(group_language.problemId == problem) & (group_language.language == "Python3") & group_language.status == 1]['count'].values[0] if (group_language[(group_language.problemId == problem) & (group_language.language == "Python3")]['status'] == 1).any() else 0,
          0 : group_language[(group_language.problemId == problem) & (group_language.language == "Python3") & (group_language.status == 0)]['count'].values[0] if (group_language[(group_language.problemId == problem) & (group_language.language == "Python3")]['status'] == 0).any() else 0,
          },
          'C++':{
          1 : group_language[(group_language.problemId == problem) & (group_language.language == "C++") & group_language.status == 1]['count'].values[0] if (group_language[(group_language.problemId == problem) & (group_language.language == "C++")]['status'] == 1).any() else 0,
          0 : group_language[(group_language.problemId == problem) & (group_language.language == "C++") & (group_language.status == 0)]['count'].values[0] if (group_language[(group_language.problemId == problem) & (group_language.language == "C++")]['status'] == 0).any() else 0,
          },
          'Java':{
          1 : group_language[(group_language.problemId == problem) & (group_language.language == "Java") & group_language.status == 1]['count'].values[0] if (group_language[(group_language.problemId == problem) & (group_language.language == "Java")]['status'] == 1).any() else 0,
          0 : group_language[(group_language.problemId == problem) & (group_language.language == "Java") & (group_language.status == 0)]['count'].values[0] if (group_language[(group_language.problemId == problem) & (group_language.language == "Java")]['status'] == 0).any() else 0,
          },
          'C':{
          1 : group_language[(group_language.problemId == problem) & (group_language.language == "C") & group_language.status == 1]['count'].values[0] if (group_language[(group_language.problemId == problem) & (group_language.language == "C")]['status'] == 1).any() else 0,
          0 : group_language[(group_language.problemId == problem) & (group_language.language == "C") & (group_language.status == 0)]['count'].values[0] if (group_language[(group_language.problemId == problem) & (group_language.language == "C")]['status'] == 0).any() else 0,
          },
          'Python':{
          1 : group_language[(group_language.problemId == problem) & (group_language.language == "Python") & group_language.status == 1]['count'].values[0] if (group_language[(group_language.problemId == problem) & (group_language.language == "Python")]['status'] == 1).any() else 0,
          0 : group_language[(group_language.problemId == problem) & (group_language.language == "Python") & (group_language.status == 0)]['count'].values[0] if (group_language[(group_language.problemId == problem) & (group_language.language == "Python")]['status'] == 0).any() else 0,
          }, 
          'Go':{
          1 : group_language[(group_language.problemId == problem) & (group_language.language == "Go") & group_language.status == 1]['count'].values[0] if (group_language[(group_language.problemId == problem) & (group_language.language == "Go")]['status'] == 1).any() else 0,
          0 : group_language[(group_language.problemId == problem) & (group_language.language == "Go") & (group_language.status == 0)]['count'].values[0] if (group_language[(group_language.problemId == problem) & (group_language.language == "Go")]['status'] == 0).any() else 0,
          }, 
          'Javascript':{
          1 : group_language[(group_language.problemId == problem) & (group_language.language == "Javascript") & group_language.status == 1]['count'].values[0] if (group_language[(group_language.problemId == problem) & (group_language.language == "Javascript")]['status'] == 1).any() else 0,
          0 : group_language[(group_language.problemId == problem) & (group_language.language == "Javascript") & (group_language.status == 0)]['count'].values[0] if (group_language[(group_language.problemId == problem) & (group_language.language == "Javascript")]['status'] == 0).any() else 0,
          }, 
      }
  from operator import itemgetter
  for key,value in problem_group_language.items():
      if value[0] + value[1] == 0:
          problem_group_language[key] = 0
      else:
          problem_group_language[key] = (value[1] / (value[0] + value[1]))
  for key,value in problem_group_particular_language.items():
    for key1,value1 in value.items():
        if(value1[0] + value1[1] != 0):
            problem_group_particular_language[key][key1] = value1[1]/(value1[0] + value1[1])
        else:
            problem_group_particular_language[key][key1] = 0
  success_score = dict()
  for problems in UNIQUE_PROBLEMS:
      temp = []
      languages = []
      for language in group_language.language.unique():
          languages.append(language)
          temp.append(1 / (1 + (problem_group_language[problems] - problem_group_particular_language[problems][language])))
          
      success_score[problems] = dict(zip(languages,temp))
  x = pd.DataFrame.from_dict(success_score, orient='index')
  x.columns.name = 'problemId'
  normalized_df=(x - x.min()) / (x.max() - x.min())
  return normalized_df


if __name__ == "__main__":
    submission_df=pd.read_csv('submission_csv')
    x=prepro(submission_df)
    x.to_csv("../data/processed/success_score.csv")