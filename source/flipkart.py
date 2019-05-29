import scrapy
import sys
import pickle
from scrapy.crawler import CrawlerProcess

#  Checks if the required parameters have been entered
if len(sys.argv)!= 3:
    print("Error: Insufficient data!")


class FlipkartSpider(scrapy.Spider):
    x = int(sys.argv[1])
    pickle_data = str(sys.argv[2])
    name = 'flipkart'
    start_urls = [
        'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1'
    ]
    index = 2
    data = []
    count = 0

    def parse(self, response):
        for item in response.css("div._1UoZlX"):
            FlipkartSpider.count = FlipkartSpider.count + 1

            if FlipkartSpider.count<= int(FlipkartSpider.x) :
                listing={
                    'name': item.css('div._3wU53n ::text').get(),
                    'rating' : item.css('span._2_KrJI ::text').get(),
                    'price' : item.css('div._1vC4OE._2rQ-NK ::text').get(),
                    }
                FlipkartSpider.data.append(listing)
                yield listing

            else:
                break

        next = 'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=' +str(FlipkartSpider.index)
        if FlipkartSpider.count <= int(FlipkartSpider.x):
            if FlipkartSpider.index < 25:
                FlipkartSpider.index = FlipkartSpider.index + 1
                yield response.follow(next, self.parse)

        pickle_out = open('pickle_data','wb')
        pickle.dump(self.data, pickle_out)
        pickle_out.close()

#To run the spider as a python script
process = CrawlerProcess()
process.crawl(FlipkartSpider)
process.start()
