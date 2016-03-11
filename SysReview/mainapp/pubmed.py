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
    startIndex = 0
    query_list = []
    query_lines = query_string.split("\r")
    count = 0
    for unformatted_line in query_lines:
        line = unformatted_line.strip("\n")
        keyword_line=False
        for keyword in KEYWORDS:
            if keyword in line:
                query_list = parseKeywords(line,query_list,keyword)
                keyword_line = True
                break
        if not keyword_line:
            query_list.append(line)
        print query_list
def summary():
    return

def parseKeywords(line,list,keyword):
    limits = [0,0]
    line_as_list = line.split(" ")
    limits[0] = int(line_as_list[1])

    if " TO " in line:
        limits[1] = int(line_as_list[3])
    else:
        limits[1] = int(line_as_list[1])

    limits[0] -= 1
    limits[1] -= 1

    result = list
    result[limits[0]] = "(" + result[limits[0]]
    result[limits[1]] = result[limits[1]] + ")"
    result.append(keyword.strip(" "))

    return result
