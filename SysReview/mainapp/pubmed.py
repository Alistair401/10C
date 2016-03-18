import json
import urllib, urllib2
from xml.dom.minidom import *
from mainapp.models import Query
import datetime

BASE_URL = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
QUERY_URL = BASE_URL + "esearch.fcgi?db=pubmed&retmax=1000&term="
SUMMARY_URL = BASE_URL + "esummary.fcgi?db=pubmed&id="
FETCH_URL = BASE_URL + "efetch.fcgi?db=pubmed&id="
LINK_URL = BASE_URL + "elink.fcgi?dbfrom=pubmed&id="
ABSTRACT_EXTENSION = "&retmode=xml&rettype=abstract"
LINK_EXTENSION = "&cmd=prlinks"
DATE = "[pdat]"
JOURNAL = "[journal]"


def esearch_query(query_string):
    # encode inital ID query
    encoded_query = urllib.pathname2url(query_string)
    # get xml response
    response = urllib2.urlopen(QUERY_URL+encoded_query)
    # parse using minidom
    dom = parse(response)
    # get all the ID elements
    id_elements = dom.getElementsByTagName("Id")
    # get the formatted query
    query_translation = getNodeText(dom.getElementsByTagName("QueryTranslation")[0].childNodes)
    # put them in a list
    id_list = []
    for i in id_elements:
        id_list.append(getNodeText(i.childNodes))
    # # get the summaries of the IDs
    # summary_dict = esummary_query(id_list)
    # summary_dict["QueryTranslation"] = query_translation
    return id_list


def esummary_query(id_list):
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
        current_id = getNodeText(doc.getElementsByTagName("Id")[0].childNodes)
        # build a dictionary to fill out for each doc
        value_dict = {"authors":[],"title":"","abstract":"","publish_date":datetime.date.today(),"paper_url":"#"}
        summary_dict[current_id] = value_dict
        for i in item_elements:
            # get titles
            if i.attributes["Name"].value == "Title":
                summary_dict[current_id]["title"] = getNodeText(i.childNodes)
            # then append authors
            if i.attributes["Name"].value == "Author":
                summary_dict[current_id]["authors"].append(getNodeText(i.childNodes))
            # then publish dates
            if i.attributes["Name"].value == "PubDate":
                d = getNodeText(i.childNodes)
                date = None
                # sometimes the date is formatted wierdly and so can't be parsed TODO
                try:
                    date = datetime.datetime.strptime(d,"%Y %b %d")
                except ValueError:
                    pass
                summary_dict[current_id]["publish_date"] = date
    return efetch_query(summary_dict)


def efetch_query(id_dictionary):
    # build the list of ID's to query with
    unencoded_query = ""
    for key in id_dictionary:
        unencoded_query += key + ","
    unencoded_query = unencoded_query[:-1]
    # encode the list
    encoded_query = urllib.pathname2url(unencoded_query)
    # get the API response
    response = urllib2.urlopen(FETCH_URL+encoded_query+ABSTRACT_EXTENSION)
    # parse the xml using minidom
    dom = parse(response)
    # fill out the abstract entries in the result dictionary with abstracts
    result_dict = id_dictionary
    article_elements = dom.getElementsByTagName("PubmedArticle")
    for element in article_elements:
        try:
            result_dict[getNodeText(element.getElementsByTagName("PMID")[0].childNodes)]["abstract"] = getNodeText(element.getElementsByTagName("AbstractText")[0].childNodes)
        except IndexError:
            result_dict[getNodeText(element.getElementsByTagName("PMID")[0].childNodes)]["abstract"] = "No abstract available"
    return id_dictionary


def elink_query(id):
    encoded_query = urllib.pathname2url(id)
    response = urllib2.urlopen(LINK_URL+encoded_query+LINK_EXTENSION)
    dom = parse(response)
    link_element = None
    try:
        link_element = dom.getElementsByTagName("Url")[0]
        return getNodeText(link_element.childNodes)
    except:
        pass
    return None


def getNodeText(nodelist):
    # get the text attributes of xml nodes
    rc = ""
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc = rc + node.data
    return rc