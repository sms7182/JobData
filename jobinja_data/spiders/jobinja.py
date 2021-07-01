from scrapy import item
from jobinja_data.items import JobinjaDataItem, JobinjaJobItem
import scrapy
from scrapy import selector
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule,CrawlSpider
from bs4 import BeautifulSoup

class JobinjaSpider(scrapy.Spider):
    name = 'jobinja'
    allowed_domains = ['https://jobinja.ir/']
    start_urls = ['https://jobinja.ir/jobs']
    rules =[Rule(callback='parse',follow=False)]

    def parse(self, response):
        # self.logger.info(f"\n parse jobinja\n{response.request.url}\n")
        # self.logger.info(f"after parsing")
        # self.logger.info(str(response.body))
        
        
        
        soup=BeautifulSoup(response.text,"html.parser")
        # self.logger.info('soup is '+str(soup))
        # job_containers=soup.find_all('div',class_='o-listView__itemInfo')
        
        self.logger.info('after jobcontainer')
        
        
        a=soup.find_all("div",{"class":"o-listView__itemInfo"})
        for data in a:
            job=JobinjaJobItem()
            job.company_desc=data.a.get("href")
            # job.=data.img.get("src")
            job.name=data.h3.a.text
            job.jobType=data.h3.a.get("href")
            info=data.find_all('li',class_="c-jobListView__metaItem")
            job.location=info[1].span.text
            job.company_fa=info[0].span.text
        
        