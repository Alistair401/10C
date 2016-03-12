import json
import urllib, urllib2
from xml.dom.minidom import *
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
    query_lines = query_string.split("\r")
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
    while "-" in query_list:
        query_list.remove("-")
    query_string = ""
    for i in query_list:
        query_string += i + " "
    return make_query(query_string)

def make_query(query_string):
    encoded_query = urllib.pathname2url(query_string)
    response = urllib2.urlopen(QUERY_URL+encoded_query)
    dom = parse(response)
    return

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
    for i in range(limits[0],limits[1]+1):
        if i == 0:
            result[i] = result[i] + ")"
        else:
            result[i] = keyword.strip(" ") + " " + result[i] + ")"
        result[0] = "(" + result[0]
    result.append("-")
    return result
