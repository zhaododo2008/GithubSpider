from scrapy import cmdline


cmdline.execute("scrapy crawl github -o items.json ".split())