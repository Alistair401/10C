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
    index_marker = 0
    count = 0
    for unformatted_line in query_lines:
        line = unformatted_line.strip("\n")
        keyword_line=False
        for keyword in KEYWORDS:
            if keyword in line:
                query_list,index_marker,count = parseKeywords(line,query_list,keyword,index_marker,count)
                keyword_line = True
                break
        if not keyword_line:
            query_list.append(line)
        print query_list

def summary():
    return

def parseKeywords(line,list,keyword,index,count):
    limits = [0,0]
    line_as_list = line.split(" ")
    if " TO " in line:
        to = True
        limits[0] = int(line_as_list[1]) - index - count
        limits[1] = int(line_as_list[3]) - index - count
    else:
        limits[0] = int(line_as_list[1]) - index - count
        limits[1] = int(line_as_list[1]) - index - count

    composed_string = "("
    for i in range(limits[0]-1,limits[1]-1):
        composed_string += list[i] + " " + keyword
    composed_string += list[limits[1]-1] + ")"

    new_index = index + (limits[1] - limits[0]) + 1

    if count == 0:
        result = [composed_string] + list[limits[1]:len(list)-1]
    else:
        result = list[:count-1]
        result.append(composed_string)
        result += list[limits[1]:len(list)-1]
    new_count = count + 1
    return result,new_index,new_count
