import json
import os 
import pdb

def convert_json(json_data_path):
  data_dict = {}

  for txt in os.listdir(json_data_path):
    if ".txt" in txt:
      with open(os.path.join(json_data_path, txt)) as f:
        data = f.read()
        txt = txt.replace(".txt", "")
        data_dict[txt] = data

  with open(os.path.join(json_data_path, "news_data.json"), "w") as f:
    json.dump(data_dict, f, indent = 4)

if __name__ == "__main__":
  json_data_path = "/home/nttung/BB/Whoosh_Text_Search/news_data"
  convert_json(json_data_path)