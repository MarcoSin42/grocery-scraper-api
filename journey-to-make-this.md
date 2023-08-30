Currently planned:
- 

* Using ABC (Abstract methods)
* Using beautiful soup for webscraping


To be decided:
-

* How to store data
* What to do with the data build some front-end stuff



Potential use cases
-

Track inflation over time.  The CPI is reflected for the average, I thought a good idea would be to track inflation for an invidual.  My diet is mostly asian, so it would probably not reflect the average.  

Shopping around. 



Log
-



August 29, 2023

Today, I was looking at commonly used Python libraries for webscraping.  I also was thinking about how I should store this data which brought me to the topic of databases.  Since I am interested in collecting this data over time, I thought a good thing to optimize would be for querying and storing time series data.  I found [TimescaleDB](https://en.wikipedia.org/wiki/TimescaleDB), a PostgresSQL extension, however, I worry that additional complications may be introduced with the added features.  I haven't looked too much into it so I don't know whether or not going with TimescaleDB would be worth it, this is something I will need to decide later on.  For now, I will continue working on just web scraping.

I also thought about how I wanted to structure the project.  Clearly, different stores will have different web interfaces making the idea of making a omni-scraper unnatenable, additionally, it's highly likely that stores will change their front-end in the future.  Thus, I think it'd be best to seperate the web scraping for different stores to various different modules and have them all implement the same public interface.  My mind immediately thought about Java's abstract methods, however, Python has no built-in direct equivalent, luckily, I did find ABC which implements this feature... sorta.

I still feel weird about using classes for this because I think classes should be reserved for objects which include but are not limited to containing a state and APIs, by definition, should be stateless.


August 30, 2023

Thinking about what methods I should have.  One obvious answer is the price of a grocery store item, however, stores often will have differing names for the same item.  Thinking of using a large-language model, will have to test to see what I can get away with in regards to tokenization.

