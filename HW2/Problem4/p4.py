import requests
import StringIO


#This homework uses exactly the same code as the github, but it is commented to explain what the libraries do.

url_str='http://elections.huffingtonpost.com/pollster/api/charts/?topic=2014-senate'

#r=requests.get('url_str')
#   r.json() parses the raw text by element, so it can be indexed.
#   for example, r.json()[0] can get {u'attribute1':u'value1', u'attribute2':u'value2'} 
#element = r.json()[0]
#   element['attribute1'] will return 'value1'


elections_urls=[election['url']+'.csv' for election in requests.get(url_str).json()]


#r=requests.get('url_str')
#   r.content gets the stuff inside without modification
#parameters to pd.Dataframe.from_csv
#   index_col: which column to set as index
#parameters to convert_objects:
#   convert_dates: convert type (e.g. string) to datetime
#        True: convert whenever possible
#        coerce: force conversion, if value is not convertible will become NaT
#   convert_numeric: convert type (e.g. string) to numeric


def build_frame(url):
    source=requests.get(url).content
    data=StringIO.StringIO(source)
    return pd.DataFrame.from_csv(data,index_col=None).convert_objects(convert_dates="coerce",convert_numeric=True)


dfs = dict( (url.split("/")[-1][:-4], build_frame(election) ) for url in election_urls)
