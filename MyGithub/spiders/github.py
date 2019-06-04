# -*- coding: utf-8 -*-
import json

import scrapy
from MyGithub.items import MygithubItem


class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://api.github.com/search/repositories?q=%E7%88%AC%E8%99%AB%20java']

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "api.github.com"
    }

    def start_requests(self):
        """ 爬虫入口

        func 参数:
            self.parse_resultcnt:   查询返回结果数
        """

        func = self.parse_resultcnt
        urls = self.gen_urls()

        for url in urls:
            yield scrapy.Request(url=url, headers=self.headers, callback=func)

    def gen_urls(self, q=None, start=1, stop=10):

        q = '%E7%88%AC%E8%99%AB%20java'

        urls = ['https://api.github.com/search/repositories?q={q}&page={p}&per_page=30'.
                    format(p=p, q=q)
                for p in range(start, stop)]
        return urls



    def parse_resultcnt(self, response):
        """ 解析特定查询下返回的结果数 """
        datas = json.loads(response.body.decode("utf-8"))
        items = datas['items']
        print(len(items))

        reps = []
        for item in items:
            rep = MygithubItem()
            owner = item['owner']
            rep['id'] = item['id']
            rep['author'] = item['full_name']
            rep['desc'] = item['description']
            rep['link'] = item['html_url']
            rep['avatar'] = owner.get('avatar_url')
            reps.append(rep)
            yield rep

        print(reps)



