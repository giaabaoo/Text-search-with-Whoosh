# Text-search-with-Whoosh
Text search system with index construction using Whoosh

## Description

In this repo, a rudimentary text search system is built to do the following tasks:
- Crawl latest news data on [VnExpress](https://e.vnexpress.net/)
- Preprocess data and construct index with Whoosh library
- Input query and preprocess query data
- Search and show the results

## Getting Started

### Dependencies
Install conda and run the following block:
```
conda create --name IR python=3.7
conda activate IR
pip install -r requirements.txt
```

### Running the code
* Crawl news data with an editable crawl_limit and do json conversion:
```
python crawler.py
python convert_data_json.py
```

* Search with text query
```
python whoosh_search.py --query "your query"
```

#### List of Arguments accepted
```--k``` Top k retrieval results (Default = 3) <br>
```--data_path``` Path to data folder (Default = "./news_data/news_data.json") <br>
```--query``` Input query for searching <br>




