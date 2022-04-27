# scrapeWebMeta-python
This is an example that i use to scrape metadata of websites from list of url in csv format, and save as a new file with the data of `title, description and keywords` in csv format.

![image](https://user-images.githubusercontent.com/5538753/165499192-04500acf-b8b0-49bb-a2e2-e430071c3901.png)

## Run
Prepare your url list in `urlList.csv`

```
$ pip install pandas urllib bs4
$ python scraper.py 
```

and you will get the result in `scrapedMeta.csv`
