from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
from whoosh import qparser
import os
from pathlib import Path
import json
import argparse


def get_args_parser():
    data_path = "./news_data/news_data.json"

    parser = argparse.ArgumentParser('Whoosh search arguments', add_help=False)
    parser.add_argument('--k', default=3, type=int)
    parser.add_argument('--data_path', default=data_path, type=str)
    parser.add_argument('--query', default="", type=str)

    return parser

def indexing_db(args):
    schema = Schema(title=TEXT(stored=True), content=TEXT,
                path=ID(stored=True), tags=KEYWORD, icon=STORED)
    
    Path("./index").mkdir(parents = True, exist_ok = True)
    ix = create_in("index", schema)

    writer = ix.writer()
    with open(args.data_path) as f:
        data = json.load(f)

    count = 0
    for doc_name, doc_content in data.items():
        writer.add_document(title=doc_name, path="/"+str(count), content=doc_content)
        count += 1
    
    writer.commit()

    return ix

if __name__ == "__main__":
    parser = argparse.ArgumentParser('Whoosh search', parents=[get_args_parser()])
    args = parser.parse_args()

    # Indexing the database
    ix = indexing_db(args)

    # Build a search method
    with ix.searcher() as searcher:
        parser = QueryParser("content", ix.schema)

        myquery = parser.parse(args.query)
        results = searcher.search(myquery)

        print("Top {} results: {}".format(args.k, results[:args.k]))


