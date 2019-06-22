from libs.crawler import crawl

url = "https://www.instagram.com/explore/tags/%EC%84%9C%EC%B4%8C/"

pageString = crawl(url)
print(pageString)
