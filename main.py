from plyer import notification
import requests
from bs4 import BeautifulSoup as soup
import time
# from urllib.request import urlopen as uReq



def notifyMe(title, message):
    notification.notify(
        title =  title,
        message = message,
        app_icon = "C:\\Users\\Ashish Sharma\\Documents\\Data Science ML Projects\\Corona Notification\\icon.ico",
        timeout = 10
    )

def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    myHtmlData = getData("https://www.mohfw.gov.in/")
    # print(myHtmlData)
    soup = soup(myHtmlData, 'html.parser')
    # # print(soup.prettify())
    myDataStr = ""
    for tr in soup.find_all('tbody')[0].find_all('tr'):
        myDataStr += tr.get_text()
    myDataStr = myDataStr[1:]
    itemList = myDataStr.split("\n\n")

    states = ["Delhi", "Uttar Pradesh", "Maharashtra"]
    for item in itemList[0:34]:
        dataList = item.split('\n')
        if dataList[1] in states:
            # print(dataList)
            nTitle = "Covid-19 Cases"
            nText = f"State : {dataList[1]}\nConfirmed Cases : {dataList[2]}\nCured Cases : {dataList[3]}\nDeaths : {dataList[4]}"
            notifyMe(nTitle, nText)
            time.sleep(2)


