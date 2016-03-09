import json
import urllib, urllib2
from mainapp.models import Query

BASE_URL = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
QUERY_URL = BASE_URL + "esearch.fcgi?db=pubmed&term="
SUMMARY_URL = BASE_URL + "esummary.fcgi?db=pubmed&id="
FETCH_URL = BASE_URL + "efetch.fcgi?db=pubmed&id="
KEYWORDS = ("AND ","OR ","NOT ")
DATE = "[pdat]"
JOURNAL = "[journal]"


def query(query_string):
    query_list = []
    query_lines = query_string.split("\n")
    for line in query_lines:
        for keyword in KEYWORDS:
            if keyword in line:
                query_list = parseKeywords(line,query_list,keyword)
                break


def summary():
    return

def parseKeywords(line,list,keyword):
    to = False
    if " TO " in line:
        to = True
    if (keyword == "AND "):
        pass
    if (keyword == "OR "):
        pass
    if (keyword == "NOT "):
        pass