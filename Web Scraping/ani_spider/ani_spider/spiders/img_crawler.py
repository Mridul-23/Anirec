import scrapy
from ani_spider.items import aniItem

class WebCrawlerSpider(scrapy.Spider):

    name = "img_crawler"
    allowed_domains = ["myanimelist.net"]
    start_urls = [f"https://myanimelist.net/topanime.php?limit={50*i}" for i in range(531,532)]
    
    custom_settings = {
        
        'CONCURRENT_REQUESTS': 2,  # Limit concurrent requests to avoid overwhelming the server
        'DOWNLOAD_DELAY': 1,  # Add a small delay between requests to be polite
        'FEEDS' : {
            '000.json' : {'format' : 'json', 'overwrite' : False}
        }
    }

    def start_requests(self):
        # Iterate through start URLs sequentially
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):

        page_anime = response.xpath("//table[@class='top-ranking-table']//tr[@class='ranking-list']//td[2]/a/@href").getall()

        for anime in page_anime:
            stats_url = anime + '/stats'
            yield scrapy.Request(anime, callback = self.parseAnimePage, meta={'stats_url' : stats_url})


    def parseAnimePage(self, response):
            
        item = aniItem()

        if response.xpath("//div['contentWrapper']//div[@class='spaceit_pad']//span[text()='English:']/following-sibling::text()").get():
            item['name_english'] = response.xpath("//div['contentWrapper']//div[@class='spaceit_pad']//span[text()='English:']/following-sibling::text()").get()
        else:
            item['name_english'] = response.xpath("//div[@id='contentWrapper']//h1[@class='title-name h1_bold_none']/strong/text()").get()

        if response.xpath('//div[@class="di-b mt4 mb8 ac"]/preceding-sibling::div/a/img/@data-src').get():
            item['img'] = response.xpath('//div[@class="di-b mt4 mb8 ac"]/preceding-sibling::div/a/img/@data-src').get()
        else:
            item['img'] = response.xpath('//div[@class="profileRows pb0"]/preceding-sibling::div/a/img/@data-src').get()

        yield item
