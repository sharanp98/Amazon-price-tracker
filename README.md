# Amazon-price-tracker
A web scraper that sends a mail when the price of a product falls below the required price.

Technology used : Python, BeautifulSoup,Argparse

The file has been tested and works for all URLs on the Amazon.in website

Prerequisites: Requests and BeautifulSoup modules
```pip3 install requests bs4```

To run the script

```
python3 scraper.py --email '<YOUR-GMAIL-ID>' --password '<YOUR-GMAIL PASSWORD>' --email_to '<GMAIL-TO-SEND THE MAIL TO>' --url '<AMAZON.IN URL>' --price <PRICE>
```
  
eg code: 

```python3 scraper.py --email 'xyz@gmail.com' --password 'abcdef' --email_to 'abc@gmail.com' --url 'https://www.amazon.in/dp/B07YSSG8C7/' --price 80000```


This code was inspired from the tutorial video by [Dev Ed](https://www.youtube.com/watch?v=Bg9r_yLk7VY)
