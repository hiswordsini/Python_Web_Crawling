import os
import sys
import requests
from urllib.parse import urlparse

def get_api_result(keyword, display, start):
    url = "https://openapi.naver.com/v1/search/blog?query=" + keyword + "&display=" + str(display)+\
          "&start=" + str(start)
    result = requests.get(urlparse(url).geturl(),
          headers={"X-Naver-Client-Id":"4iyOwi5lcKr_ltPVXLKp",
                   "X-Naver-Client-Secret":"k2GCzMZQcu"})
    return result.json()

def call_and_print(keyword, page):
    json_obj = get_api_result(keyword, 100, page)
    #print(json_obj['items'])
    for item in json_obj['items']:
        title = item['title'].replace("<b>", "").replace("</b>", "")
        print(title + "§" + item['bloggername'] + "§" + item['link'])

keyword = "강남역"
call_and_print(keyword, 1)
call_and_print(keyword, 101)
call_and_print(keyword, 201)
call_and_print(keyword, 301)
call_and_print(keyword, 401)


#print(json_obj)
#print(json_obj['display'])
#print(json_obj['start'])
#print(len(json_obj['items']))
#for item in json_obj['items']:
#    print(item['title'].replace("<b>", "").replace("</b>", ""), item['link'])
#    print(item)
#print(json_obj['items'])

#import urllib.request
#client_id = "4iyOwi5lcKr_ltPVXLKp"
#client_secret = "k2GCzMZQcu"
#encText = urllib.parse.quote("강남역")
#url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
#request = urllib.request.Request(url)
#request.add_header("X-Naver-Client-Id",client_id)
#request.add_header("X-Naver-Client-Secret",client_secret)
#response = urllib.request.urlopen(request)
#rescode = response.getcode()
#if(rescode==200):
#    response_body = response.read()
#    print(response_body.decode('utf-8'))
#else:
#    print("Error Code:" + rescode)