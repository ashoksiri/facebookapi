


class BasicPage(object):

    def __init__(self,id,fan_count,name):
        self.id = id
        self.fan_count = fan_count
        self.name = name

class Location(object):

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

class Page(BasicPage):

    def __init__(self,**kwargs):
        kwargs = kwargs['data'] if kwargs.has_key('data') else {}
        self.id = kwargs['id'] if kwargs.has_key('id') else None
        self.about = kwargs['about'] if kwargs.has_key('about') else None
        self.fan_count = kwargs['fan_count'] if kwargs.has_key('fan_count') else None
        self.bio = kwargs['bio'] if kwargs.has_key('bio') else None
        self.category = kwargs['category'] if kwargs.has_key('category') else None
        self.company_overview = kwargs['company_overview'] if kwargs.has_key('company_overview') else None
        self.contact_address = kwargs['contact_address'] if kwargs.has_key('contact_address') else None
        self.picture = kwargs['picture']['data']['url'] if kwargs.has_key('picture') else None
        self.current_location = kwargs['current_location'] if kwargs.has_key('current_location') else None
        self.description = kwargs['description'] if kwargs.has_key('description') else None
        self.description_html = kwargs['description_html'] if kwargs.has_key('description_html') else None
        self.general_info = kwargs['general_info'] if kwargs.has_key('general_info') else None
        self.likes = kwargs['likes'] if kwargs.has_key('likes') else None
        self.link = kwargs['link'] if kwargs.has_key('link') else None
        self.location = kwargs['location'] if kwargs.has_key('location') else None
        self.new_like_count = kwargs['new_like_count'] if kwargs.has_key('new_like_count') else None
        self.name = kwargs['name'] if kwargs.has_key('name') else None
        self.phone = kwargs['phone'] if kwargs.has_key('phone') else None
        self.rating_count = kwargs['rating_count'] if kwargs.has_key('rating_count') else None
        self.talking_about_count = kwargs['talking_about_count'] if kwargs.has_key('talking_about_count') else None
        self.website = kwargs['website'] if kwargs.has_key('website') else None
        self.were_here_count = kwargs['were_here_count'] if kwargs.has_key('were_here_count') else None

    def __str__(self):
        return super(Page, self).__str__()


if __name__ == '__main__':

    print Page(id=1,name=1,about=2).about
