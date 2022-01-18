import re, requests, subprocess, urllib.parse, urllib.request
from bs4 import BeautifulSoup


def find_url(name):
    query_string = urllib.parse.urlencode({"search_query": name})
    format_url = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)

    search_results = re.findall(r"watch\?v=(\S{11})", format_url.read().decode())
    clip = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])

    print(clip)
    return clip