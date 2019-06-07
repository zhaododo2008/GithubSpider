# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MygithubItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    id = scrapy.Field()  # 唯一编码
    author = scrapy.Field()  # 作者
    avatar = scrapy.Field()  # 头像
    desc = scrapy.Field()  # 简述
    link = scrapy.Field()  # 链接
    language = scrapy.Field()  # 语言
    posttime = scrapy.Field()  # 发布时间
    pass
