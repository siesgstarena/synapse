import os
import pandas as pd
from helper.problem.poc.preprocess import prepro
from helper.problem.recommend.recommend import recommend


# testing preprocess function
def test_preprocess():
    dirname = os.path.dirname(__file__)
    config_file = os.path.join(dirname, "test_submissions.csv")
    df = pd.read_csv(config_file)
    temp = prepro(df)
    assert temp.shape == (209, 7)


def test_recommend():
    temp = recommend("1")
    assert len(temp) == 0


def test_recommend_correct():
    temp = recommend("5b72f1a5750b6100209d9f13")
    assert len(temp[0]) == 207
