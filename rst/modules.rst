source

FlipkartSpider
======
The class consists of a series of instructions to extract the required data from the url.

Class Variables:
   1. x takes the value of the number of laptops
   2. pickle_data takes the name of the direrctory entered
   3. index - used to go to the next page from the main url once a page has been scraped
   4. count - used to keep count of the number of items that have been scraped
   5. data  - used to hold all the data etracted from the website
   6. start_urls - list of the urls to be crawled
   7. name - name of the spider

A method parse() is set up within it to access the web pages (response) and return a dictionary of the extracted data.
The individual properties (name, rating, price) of each listing having the div marker is extracted
Each listing is saved as a dictionary and is appended to self.data and returned using yield.
The spider moves on (crawls) to the next page through respone.follow().

self.data is finally pickled and passed to the directory specified by the user.

.. toctree::
   :maxdepth: 4

   flipkart
