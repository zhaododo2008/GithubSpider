# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql as pymysql
import scrapy
from scrapy.pipelines.images import ImagesPipeline


class MygithubPipeline(ImagesPipeline):
    def get_media_requests(self, item, spider):
            print(item['avatar'])
            yield scrapy.Request(item['avatar'])


class MysqlPipeline(object):
    def process_item(self,item,spider):
        '''
        将爬取的信息保存到mysql
        '''
        # 将item里的数据拿出来
        res_id = item['id']
        author = item['author']
        avatar = item['avatar']
        resume = item['desc']
        html_link = item['link']
        post_time = item['posttime']

        post_time = post_time.replace('T', ' ')
        post_time = post_time.replace('Z', '')
        tag = item['language']

        # 和本地的newsDB数据库建立连接
        db = pymysql.connect(
            host='localhost',  # 连接的是本地数据库
            user='root',  # 自己的mysql用户名
            passwd='ilovethis',  # 自己的密码
            db='cmarket',  # 数据库的名字
            charset='utf8mb4',  # 默认的编码方式：
            cursorclass=pymysql.cursors.DictCursor)
        try:
            # 使用cursor()方法获取操作游标
            cursor = db.cursor()

            # SQL 插入语句
            sql = "insert into `t_resource`(res_id, author, avatar, resume, link, post_time, tag) \
                  VALUES (%d ,'%s', '%s', '%s','%s','%s','%s')" % (res_id, author, avatar, resume, html_link,post_time,tag)

            # 执行SQL语句
            cursor.execute(sql)
            # 提交修改
            db.commit()
        finally:
            # 关闭连接
            db.close()
            return item
