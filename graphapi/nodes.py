import json
from dateparser import parse
import datetime

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime.datetime):
            return obj.__str__()
        if hasattr(obj,'__dict__'):
            return obj.__dict__()
        else:
            return json.JSONEncoder.default(self, obj)

class BasicPage(object):

    def __init__(self,id,fan_count,name):
        self.id = id
        self.fan_count = fan_count
        self.name = name

    def __iter__(self):
        yield 'id',self.id
        yield 'fan_count',self.fan_count
        yield 'name',self.name

    def __dict__(self):
        return dict(self)

    def __json__(self):
        return json.dumps(self.__dict__())

class Adress(object):

    def __init__(self,**kwargs):
        kwargs = kwargs['data'] if kwargs.has_key('data') else {}
        self.id = kwargs['id'] if kwargs.has_key('id') else None
        self.city = kwargs['city'] if kwargs.has_key('city') else None
        self.city_page = kwargs['city_page'] if kwargs.has_key('city_page') else None
        self.country = kwargs['country'] if kwargs.has_key('country') else None
        self.postal_code = kwargs['postal_code'] if kwargs.has_key('postal_code') else None
        self.region = kwargs['region'] if kwargs.has_key('region') else None
        self.street1 = kwargs['street1'] if kwargs.has_key('street1') else None
        self.street2 = kwargs['street2'] if kwargs.has_key('street2') else None

    def __iter__(self):
        yield 'id',self.id
        yield 'city',self.city
        yield 'city_page',self.city_page
        yield 'country',self.country
        yield 'postal_code',self.postal_code
        yield 'region',self.region
        yield 'street1',self.street1
        yield 'street2',self.street2

    def __dict__(self):
        return dict(self)

    def __json__(self):
        return json.dumps(self.__dict__())

class Location(object):

    def __init__(self,**kwargs):
        kwargs = kwargs['data'] if kwargs.has_key('data') else {}
        self.city_id = kwargs['city_id'] if kwargs.has_key('city_id') else None
        self.city = kwargs['city'] if kwargs.has_key('city') else None
        self.state = kwargs['state'] if kwargs.has_key('state') else None
        self.country = kwargs['country'] if kwargs.has_key('country') else None
        self.street = kwargs['street'] if kwargs.has_key('street') else None
        self.zip = kwargs['zip'] if kwargs.has_key('zip') else None
        self.latitude = kwargs['latitude'] if kwargs.has_key('latitude') else None
        self.longitude = kwargs['longitude'] if kwargs.has_key('longitude') else None

    def __iter__(self):
        yield 'city_id',self.city_id
        yield 'city',self.city
        yield 'state',self.state
        yield 'country',self.country
        yield 'street',self.street
        yield 'zip',self.zip
        yield 'latitude',self.latitude
        yield 'longitude',self.longitude

    def __dict__(self):
        return dict(self)

    def __json__(self):
        return json.dumps(self.__dict__())

class Page(BasicPage):

    def __init__(self,**kwargs):
        kwargs = kwargs['data'] if kwargs.has_key('data') else {}
        self.id = kwargs['id'] if kwargs.has_key('id') else None
        self.about = kwargs['about'] if kwargs.has_key('about') else None
        self.fan_count = kwargs['fan_count'] if kwargs.has_key('fan_count') else None
        self.bio = kwargs['bio'] if kwargs.has_key('bio') else None
        self.category = kwargs['category'] if kwargs.has_key('category') else None
        self.company_overview = kwargs['company_overview'] if kwargs.has_key('company_overview') else None
        self.contact_address = Adress(data=kwargs['contact_address']) if kwargs.has_key('contact_address') else None
        self.picture = kwargs['picture']['data']['url'] if kwargs.has_key('picture') else None
        self.current_location = kwargs['current_location'] if kwargs.has_key('current_location') else None
        self.description = kwargs['description'] if kwargs.has_key('description') else None
        self.description_html = kwargs['description_html'] if kwargs.has_key('description_html') else None
        self.general_info = kwargs['general_info'] if kwargs.has_key('general_info') else None
        self.likes = kwargs['likes'] if kwargs.has_key('likes') else None
        self.link = kwargs['link'] if kwargs.has_key('link') else None
        self.location = Location(data=kwargs['location']) if kwargs.has_key('location') else None
        self.new_like_count = kwargs['new_like_count'] if kwargs.has_key('new_like_count') else None
        self.name = kwargs['name'] if kwargs.has_key('name') else None
        self.phone = kwargs['phone'] if kwargs.has_key('phone') else None
        self.rating_count = kwargs['rating_count'] if kwargs.has_key('rating_count') else None
        self.talking_about_count = kwargs['talking_about_count'] if kwargs.has_key('talking_about_count') else None
        self.website = kwargs['website'] if kwargs.has_key('website') else None
        self.were_here_count = kwargs['were_here_count'] if kwargs.has_key('were_here_count') else None

    def __str__(self):
        return super(Page, self).__str__()

    def __iter__(self):
        yield 'id',self.id
        yield 'about',self.about
        yield 'fan_count',self.fan_count
        yield 'bio',self.bio
        yield 'category',self.category
        yield 'company_overview' ,self.company_overview
        yield 'contact_address',self.contact_address
        yield 'picture',self.picture
        yield 'current_location',self.current_location
        yield 'description',self.description
        yield 'description_htmls',self.description_html
        yield 'general_info',self.general_info
        yield 'likes',self.likes
        yield 'link',self.link
        yield 'location',self.location
        yield 'new_like_count',self.new_like_count
        yield 'name',self.name
        yield 'phone',self.phone
        yield 'rating_count' , self.rating_count
        yield 'talking_about_count',self.talking_about_count
        yield 'website',self.website
        yield 'were_here_count',self.were_here_count

    def __dict__(self):
        return dict(self)

    def __json__(self):
        return json.dumps(self.__dict__(),cls=ComplexEncoder)

class From(object):

    def __init__(self,**kwargs):
        if kwargs.has_key('data'):
            kwargs = kwargs['data']
        self.id = kwargs.get('id') if kwargs.has_key('id') else None
        self.name = kwargs.get('name') if kwargs.has_key('name') else None

    def __iter__(self):
        yield 'id',self.id
        yield 'name',self.name

    def __dict__(self):
        return dict(self)

    def __json__(self):
        return json.dumps(self.__dict__(),cls=ComplexEncoder)

class Comment(object):

    def __init__(self,**kwargs):
        if kwargs.has_key('data'):
            kwargs = kwargs['data']

        self.id = kwargs.get('id') if kwargs.has_key('id') else None
        self.created_time = parse(kwargs.get('created_time')) if kwargs.has_key('created_time') else None
        self._from = From(data=kwargs.get('from')) if kwargs.has_key('from') else None
        self.message = kwargs.get('message') if kwargs.has_key('message') else None

    def __iter__(self):
        yield 'id',self.id
        yield 'from',self._from
        yield 'created_time',self.created_time
        yield 'message',self.message

    def __dict__(self):
        return dict(self)

    def __json__(self):
        return json.dumps(self.__dict__(),cls=ComplexEncoder)

class Post(object):

    def __iter__(self):
        yield 'id', self.id
        yield 'from', self._from
        yield 'created_time', self.created_time
        yield 'message', self.message
        yield 'permalink_url', self.permalink_url
        yield 'type', self.type
        yield 'updated_time', self.updated_time
        yield 'likes', self.likes
        yield 'loves', self.loves
        yield 'wows', self.wows
        yield 'angries', self.angries
        yield 'sads', self.sads
        yield 'hahas', self.hahas
        yield 'comments', self.comments
        yield 'shares', self.shares
        yield 'page', self.page
        yield 'likeCount', self.likeCount
        yield 'loveCount', self.loveCount
        yield 'wowCount', self.wowCount
        yield 'sadCount', self.sadCount
        yield 'angryCount', self.angryCount
        yield 'hahaCount', self.hahaCount
        yield 'commentCount', self.commentCount

    def __dict__(self):
        return dict(self)

    def __json__(self):
        return json.dumps(self.__dict__(),cls=ComplexEncoder)

    def __init__(self,**kwargs):
        if kwargs.has_key('data'):
            kwargs = kwargs['data']
        self.id = kwargs.get('id') if kwargs.has_key('id') else None
        self._from = From(data=kwargs.get('from')) if kwargs.has_key('from') else None
        self.created_time = parse(kwargs.get('created_time')) if kwargs.has_key('created_time') else None
        self.message  = kwargs.get('message') if kwargs.has_key('message') else None
        self.permalink_url = kwargs.get('permalink_url') if kwargs.has_key('permalink_url') else None
        self.type = kwargs.get('type') if kwargs.get('type') else None
        self.updated_time = parse(kwargs.get('updated_time')) if kwargs.has_key('updated_time') else None
        self.likes = [From(data=like) for like in kwargs.get('like').get('data')] if kwargs.has_key('like') else None
        self.loves = [From(data=love) for love in kwargs.get('love').get('data')] if kwargs.has_key('love') else None
        self.wows = [From(data=wow) for wow in kwargs.get('wow').get('data')] if kwargs.has_key('wow') else None
        self.hahas = [From(data=haha) for haha in kwargs.get('haha').get('data')] if kwargs.has_key('haha') else None
        self.sads = [From(data=sad) for sad in kwargs.get('sad').get('data')] if kwargs.has_key('sad') else None
        self.angries = [From(data=angry) for angry in kwargs.get('angry').get('data')] if kwargs.has_key(
            'angry') else None
        self.comments = [Comment(data=comment) for comment in kwargs.get('comments').get('data')] if kwargs.has_key(
            'comments') else None
        self.shares = kwargs.get('shares').get('count') if kwargs.has_key('shares') else None
        self.page   = kwargs.get('page') if kwargs.has_key('page') else None
        self.likeCount = kwargs.get('like').get('summary').get('total_count') if kwargs.has_key(
            'like') else 0
        self.wowCount = kwargs.get('wow').get('summary').get('total_count') if kwargs.has_key(
            'wow') else 0
        self.angryCount = kwargs.get('angry').get('summary').get('total_count') if kwargs.has_key(
            'angry') else 0
        self.hahaCount = kwargs.get('haha').get('summary').get('total_count') if kwargs.has_key(
            'haha') else 0
        self.sadCount = kwargs.get('sad').get('summary').get('total_count') if kwargs.has_key(
            'sad') else 0
        self.loveCount = kwargs.get('love').get('summary').get('total_count') if kwargs.has_key(
            'live') else 0
        self.commentCount = kwargs.get('comments').get('summary').get('total_count') if kwargs.has_key(
            'comments') else 0