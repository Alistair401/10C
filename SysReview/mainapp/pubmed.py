import json
import urllib, urllib2
from xml.dom.minidom import *
from mainapp.models import Query
import datetime

BASE_URL = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
QUERY_URL = BASE_URL + "esearch.fcgi?db=pubmed&term="
SUMMARY_URL = BASE_URL + "esummary.fcgi?db=pubmed&id="
FETCH_URL = BASE_URL + "efetch.fcgi?db=pubmed&id="
ABSTRACT_EXTENSION = "&retmode=xml&rettype=abstract"
KEYWORDS = ("AND ","OR ","NOT ")
DATE = "[pdat]"
JOURNAL = "[journal]"


def query(query_string):
    # all formatting stuff TODO: comment stuff better
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
    # encode inital ID query
    encoded_query = urllib.pathname2url(query_string)
    # get xml response
    response = urllib2.urlopen(QUERY_URL+encoded_query)
    # parse using minidom
    dom = parse(response)
    # get all the ID elements
    id_elements = dom.getElementsByTagName("Id")
    # put them in a list
    id_list = []
    for i in id_elements:
        id_list.append(getText(i.childNodes))
    # get the summaries of the IDs
    summary_dict = summary(id_list)
    return summary_dict

def std_query(query_string):
    # formats the string with brackets (may be redundant)
    query_list = query_string.split(" ")
    # removes weird empty strings from the query
    while "" in query_list:
        query_list.remove("")
    # add brackets
    for i in range(0,len(query_list)-1,2):
        query_list[0] = "(" + query_list[0]
        query_list[i] = query_list[i] + ")"
    # turn list back into string
    proper_query = ""
    for i in query_list:
        proper_query += i + " "
    # get abstracts
    return make_query(proper_query)


def summary(id_list):
    # format id list to query
    id_query = ""
    for i in range(0,len(id_list)-1):
        id_query += id_list[i] + ","
    id_query += id_list[len(id_list)-1]
    # encode inital ID query
    encoded_query = urllib.pathname2url(id_query)
    # get xml response
    response = urllib2.urlopen(SUMMARY_URL+encoded_query)
    # parse using minidom
    dom = parse(response)
    # get the summary document
    eSummaryResult = dom.childNodes[1]
    # get the child nodes of those
    summary_nodes =  eSummaryResult.childNodes
    # loop through nodes and check if they're DocSums or weird empty text nodes
    docSums = []
    for node in summary_nodes:
        if node.nodeType != node.TEXT_NODE:
            docSums.append(node)
    # make a dictionary to store document summaries
    summary_dict = {}
    # loop through nodes and get their values for each doc
    for doc in docSums:
        # get all the xml items of the document
        item_elements = doc.getElementsByTagName("Item")
        # get the ID of the current doc
        current_id = getText(doc.getElementsByTagName("Id")[0].childNodes)
        # build a dictionary to fill out for each doc
        value_dict = {"authors":[],"title":"","abstract":"","publish_date":datetime.date.today(),"paper_url":"#"}
        summary_dict[current_id] = value_dict
        for i in item_elements:
            # get titles
            if i.attributes["Name"].value == "Title":
                summary_dict[current_id]["title"] = getText(i.childNodes)
            # then append authors
            if i.attributes["Name"].value == "Author":
                summary_dict[current_id]["authors"].append(getText(i.childNodes))
            # then publish dates
            if i.attributes["Name"].value == "PubDate":
                d = getText(i.childNodes)
                date = None
                # sometimes the date is formatted wierdly and so can't be parsed TODO
                try:
                    date = datetime.datetime.strptime(d,"%Y %b %d")
                except ValueError:
                    pass
                summary_dict[current_id]["publish_date"] = date
    return getAbstracts(summary_dict)

def getText(nodelist):
    # get the text attributes of xml nodes
    rc = ""
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc = rc + node.data
    return rc

def parseKeywords(line,list,keyword):
    # formatting stuff TODO: comment more stuff
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

def getAbstracts(id_dictionary):
    # build the list of ID's to query with
    unencoded_query = ""
    for key in id_dictionary:
        unencoded_query += key + ","
    unencoded_query = unencoded_query[:-1]
    # encode the list
    encoded_query = urllib.pathname2url(unencoded_query)
    # get the API response
    response = urllib2.urlopen(FETCH_URL+encoded_query+ABSTRACT_EXTENSION)
    print FETCH_URL+encoded_query+ABSTRACT_EXTENSION
    # parse the xml using minidom
    dom = parse(response)
    # fill out the abstract entries in the result dictionary with abstracts
    result_dict = id_dictionary
    article_elements = dom.getElementsByTagName("PubmedArticle")
    for element in article_elements:
        result_dict[getText(element.getElementsByTagName("PMID")[0].childNodes)]["abstract"] = getText(element.getElementsByTagName("AbstractText")[0].childNodes)
    return id_dictionary