import requests,time,urllib,json
from nodes import BasicPage,Page,Post

API_URL = 'https://graph.facebook.com/v'

VERSION = ['2.8','2.9','2.10']

MAX_PAGE_SIZE = 1000

PAGE_FIELDS =[ 'id','about','fan_count','bio','category','company_overview','contact_address','picture',
        'current_location','description','description_html','general_info','likes','link',
        'location','new_like_count','name','phone','rating_count','talking_about_count','website',
        "were_here_count"]

POST_FIELDS = ['id','from','created_time','message','icon','link','permalink_url','place','type','to',
               'updated_time','full_picture','picture',
                'reactions.type(LIKE).limit(20).summary(total_count).as(like)',
                'reactions.type(LOVE).limit(20).summary(total_count).as(love)',
                'reactions.type(WOW).limit(20).summary(total_count).as(wow)',
                'reactions.type(HAHA).limit(20).summary(total_count).as(haha)',
                'reactions.type(SAD).limit(20).summary(total_count).as(sad)',
                'reactions.type(ANGRY).limit(20).summary(total_count).as(angry)',
                'comments.limit(20).summary(total_count)',
                'shares'
               ]

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
        try:
            return json.loads(response.text)
        except ValueError:
            return {}

    def _get_api_url(self):
        return API_URL+self.version

    def _prepare_url(self,url):
        return url+'&access_token={}'.format(self.access_token)

    def get_sccess_token(self):
        return self.access_token;

    def getPages(self,keyword,**kwargs):
        limit = 25
        fields = 'id,name,fan_count'
        if kwargs.has_key('limit'):
            if limit < kwargs['limit']:
                limit = kwargs['limit']

            if limit > MAX_PAGE_SIZE:
                raise ValueError('Max Allowed Size is 1000')
        if kwargs.has_key('fields'):
            fields = kwargs['fields']

        url       = self._get_api_url()
        keyword   = urllib.quote_plus(keyword)
        url       = url + '/search?type=page&limit={}&q={}'.format(limit,keyword)
        final_url = self._prepare_url(url + '&fields='+fields)
        response  = self._request_until_succeed(final_url)

        if response.has_key('data'):
            return [BasicPage(page['id'],page['fan_count'],page['name']) for page in \
                    sorted(response['data'],key=lambda x:x['fan_count'],reverse=True)][:limit]
        else:
            return  []

    def getPage(self,pageid):
        url = self._get_api_url()
        url = self._prepare_url(url+'/'+pageid+'?fields={}'.format(','.join(PAGE_FIELDS)))
        response = self._request_until_succeed(url)
        if response:
            return Page(data=response)
        else:
            return None

    def getPosts(self,pageid,**kwargs):
        limit = 5
        if kwargs.has_key('limit'):
            limit = kwargs['limit']
        page = self.getPage(pageid=pageid)
        url = self._get_api_url()+'/{}'.format(pageid)
        url = self._prepare_url(url+'?fields=posts{}&limit={}'.format('{'+','.join(POST_FIELDS+'}'),limit))
        response = self._request_until_succeed(url)
        def addPage(post):
            post['page'] = page
            return post
        if response:
            if response.has_key('posts'):
                return [Post(data=addPage(post)) for post in response.get('posts').get('data')]
        else:
            return []

    def getPost(self,postid,**kwargs):
        pass

    def getComments(self,postid,**kwargs):
        pass

    def getComment(self,commentid,**kwargs):
        pass

    def getReactions(self,id,**kwargs):
        pass



