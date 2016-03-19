import json
import urllib, urllib2
from xml.dom.minidom import *
from mainapp.models import Query
import datetime

BASE_URL = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
QUERY_URL = BASE_URL + "esearch.fcgi?db=pubmed&retmax=1000&term="
SUMMARY_URL = BASE_URL + "esummary.fcgi?db=pubmed&id="
FETCH_URL = BASE_URL + "efetch.fcgi"
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
    return id_list


def efetch_query(id_list):
    # format id list to query
    id_query = ""
    for i in range(0,len(id_list)-1):
        id_query += id_list[i] + ","
    id_query += id_list[len(id_list)-1]
    POST_data = {"id":id_query,
                 "db":"pubmed",
                 "retmode":"xml"}
    # encode inital ID query
    encoded_query = urllib.urlencode(POST_data)
    # get xml response from a POST request
    request = urllib2.Request(FETCH_URL,encoded_query)
    response = urllib2.urlopen(request)
    # parse using minidom
    dom = parse(response)
    # parse the xml through getting all the labelled elements
    PubmedArticles = dom.getElementsByTagName("PubmedArticle")
    efetch_dict = {}
    for article in PubmedArticles:
        value_dict = {"authors":[],"title":"","abstract":"","publish_date":datetime.date.today(),"paper_url":"#"}
        article_id = getNodeText(article.getElementsByTagName("PMID")[0].childNodes)
        efetch_dict[article_id] = value_dict
        for author in article.getElementsByTagName("Author"):
            forename = ""
            lastname = ""
            try:
                forename = getNodeText(author.getElementsByTagName("ForeName")[0].childNodes)
            except IndexError:
                pass
            try:
                lastname = getNodeText(author.getElementsByTagName("LastName")[0].childNodes)
            except IndexError:
                pass
            full_name = forename + " " + lastname
            efetch_dict[article_id]["authors"].append(full_name)
        efetch_dict[article_id]["title"] = getNodeText(article.getElementsByTagName("ArticleTitle")[0].childNodes)
        try:
            efetch_dict[article_id]["abstract"] = getNodeText(article.getElementsByTagName("AbstractText")[0].childNodes)
        except IndexError:
            efetch_dict[article_id]["abstract"] = "No abstract available"
        day = "01"
        month = "Jan"
        year = "0001"
        article_data = article.getElementsByTagName("Article")[0]
        date_data = article_data.getElementsByTagName("PubDate")[0]
        try:
            day = getNodeText(date_data.getElementsByTagName("Day")[0].childNodes)
        except IndexError:
            pass
        try:
            month = getNodeText(date_data.getElementsByTagName("Month")[0].childNodes)
        except IndexError:
            pass
        try:
            year = getNodeText(date_data.getElementsByTagName("Year")[0].childNodes)
        except IndexError:
            pass
        efetch_dict[article_id]["publish_date"] = datetime.datetime.strptime(day+","+month+","+year,"%d,%b,%Y")
    return efetch_dict


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