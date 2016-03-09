import json
import urllib, urllib2
from mainapp.models import Query

BASE_URL = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
QUERY_URL = BASE_URL + "esearch.fcgi?db=pubmed&term="
SUMMARY_URL = BASE_URL + "esummary.fcgi?db=pubmed&id="
FETCH_URL = BASE_URL + "efetch.fcgi?db=pubmed&id="
AND = "AND"


def query(query_string):
    query_lines = query_string.split("\n")
    query = ""
    for line in query_lines:
        query+= parseLine(line)
    return

def summary():
    return

def parseLine(line):

    return