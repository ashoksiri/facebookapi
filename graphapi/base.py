import requests,time,urllib

API_URL = 'https://graph.facebook.com/v'

VERSION = ['2.8','2.9','2.10']

MAX_PAGE_SIZE = 1000

class Graph(object):



    def __init__(self,access_token,version):
        self.access_token = access_token
        self.version = version

        if self.version not in VERSION:
            raise ValueError("Version Not Found")


    def _request_until_succeed(self,url):
        response = requests.get(url)
        success = False
        while success is False:
            try:
                if response.status_code == 200:
                    success = True
            except Exception as e:
                time.sleep(2)
                print("Retrying.......")
        return response.text


    def get_sccess_token(self):
        return self.access_token;


    def getpages(self,keyword,**kwargs):
        limit = 25
        fields = 'id,name'
        if kwargs.has_key('limit'):
            limit = kwargs['limit']
            if limit > MAX_PAGE_SIZE:
                raise ValueError('Max Allowed Size is 1000')
        if kwargs.has_key('fields'):
            fields = kwargs['fields']

        url = API_URL+self.version
        keyword = urllib.quote_plus(keyword)
        url = url+'/search?type=page&limit={}&q={}&access_token={}'.format(limit,keyword,self.access_token)
        final_url = url+'&fields='+fields
        response = self._request_until_succeed(final_url)
        return  response

