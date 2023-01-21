import json
import pandas as pd

# pylint: disable=redefined-outer-name


def raw(jsondata):
    # save json data to csv file
    df = pd.DataFrame(jsondata)
    df.to_csv("submissions.csv", index=False)
    return "submissions.csv"


if __name__ == "__main__":
    with open("csvjson.json", encoding="utf-8") as json_file:
        jsondata = json.load(json_file)
    raw(jsondata)
