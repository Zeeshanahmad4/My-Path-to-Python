
#hidden elements that gives null values
    html = browser.page_source
    soup = BeautifulSoup(html)
    divTag = soup.find_all("yt-formatted-string", {"class": "style-scope ytd-toggle-button-renderer style-text"})
    for tag in divTag:
        print tag.text
 #second approch   # for tag in soup.find_all('yt-formatted-string'):
    #     print tag.text
