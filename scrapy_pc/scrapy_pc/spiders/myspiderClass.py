
import scrapy

class MySpiderClass(scrapy.Spider):



    def start_requests(self):

        url = 'https://github.com/session'

        scrapy.FormRequest(url=url,
                           formdata={
                                'authenticity_token': 'Th1p8vt/oVpKCtgSDIrA/yhccQ5Mm6TyjXoWLLHDtaUhOMYSFGu5OAyTLTfyNQZ75J/RDX5PxpI8lH6NFZe02Q==',
                                'login': 'kylinxjd',
                                'password': '15858102962kylin'
                           },
                           callback=self.parse_req
                           )

    def parse_req(self, response):
        pass


class GitHubLogin(MySpiderClass):

    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/']

    def parse(self, response):
        print("--------------------------------")
        print(response.text)
        pass