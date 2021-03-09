# Get_financial
This project is using python for collecting stock's financial data from financial website( https://www.reuters.com/ ).

# Why this Project ?
When I decide to analyze or screen fundamental of stock in the market (especially from country outside US). I always find hard way to gather information from each website.
So I decide to reduce my manual task as much as possible by writing this script.

# Why Reuters ?
When compare to other financial website, Reuters has more complete financial information i.e. incomestatment of some stock before IPO.
But if you need to analyze Stock Data from US zone I suggest you to use yahoo finance library, It will make your life much more easy.

# Library that I used:
1. pandas - to store final information. 
2. urllib.request - to request information from website 
3. Beautifulsoup - to manage html and xml data from urllib.request
4. json - to covert json to dictionary data in python

# How to use ?
Before using this function you need to know "Symbol" of stock you looking for.

For example, 
- Tesla Inc --> TSLA.OQ
- Airports of Thailand PCL --> AOT.BK

If you don't sure about Symbol youcan search in this site https://www.reuters.com/search

After youget Symbol you can run code by this command

```
df = get_income_statement(Stock)
```

#Hope This Help
