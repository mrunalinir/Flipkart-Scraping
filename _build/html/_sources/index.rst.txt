.. Flipkart Scraping documentation master file, created by
   sphinx-quickstart on Thu May 30 00:48:25 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Flipkart Scraping's documentation!
=============================================
This project is aimed to scrape https://www.flipkart.com/ and find the name, price and rating of all the laptops listed.
The spider can be run by using the following command:
  python3 flipkart.py NUMBER_OF_LAPTOPS PICKLE_DIR
(Running the spider as a python script has been faciclitated by CrawlerProcess.)

The laptop listings will be pickled and saved to the directory specified by the user

Requirements:
  In order to run this project, python3 needs to be installed on the system along with the following packages:
    1. Scrapy
    2. Pickle

(Search modules)

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
