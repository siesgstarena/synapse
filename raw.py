import json
import csv

def raw(jsondata):
  data_file = open('output1.csv', 'w', newline='')
  csv_writer = csv.writer(data_file)

  count = 0
  for data in jsondata:
    if count == 0:
      header = data.keys()
      csv_writer.writerow(header)
      count += 1
    csv_writer.writerow(data.values())

  data_file.close()
  return data_file

with open('/content/csvjson.json') as json_file:
	jsondata = json.load(json_file)


raw(jsondata)
