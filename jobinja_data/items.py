# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field


class JobinjaDataItem(scrapy.Item):
    title_fa=Field()
    title_en=Field()
    open_jobs=Field()
    category=Field()
    company_size=Field()
    year=Field()

class JobinjaJobItem(scrapy.Item):
    name = Field()
    company_fa = Field()
    category = Field()
    location = Field()
    minExperience = Field()
    jobType = Field()
    salary = Field()
    desc = Field()
    company_desc = Field()
    skills = Field()
    period = Field()
    militaryServiceStatus = Field()
    gender = Field()
    degree = Field()
    language = Field()
    allowedMajors = Field()
    active = Field()


