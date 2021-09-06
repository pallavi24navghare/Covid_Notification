from plyer import notification
import requests
from bs4 import BeautifulSoup


def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,
        timeout=5
    )


def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == '__main__':

    # notifyMe("rani" , "help us out here ")
    myHtmlData = getData('https://www.mohfw.gov.in/')

    soup = BeautifulSoup(myHtmlData, 'html.parser')
    # print(soup.prettify())
    myDataStr = ''
    #  ----------NO ERROR CODE ------
    # for table in soup.find_all('table'):
    #     print(table)



    # -----Index Error-------
    for tr in soup.find_all('tbody')[1].find_all('tr'):
        myDataStr += tr.get_text('')

    myDataStr = myDataStr[1:]
    itemList = myDataStr.split('/n/n')
    states = ['Maharashtra', 'Gujrat', 'Uttar Pradesh']
    for item in itemList[0:22]:
        Datalist = item.split('/n')
        if Datalist[1] in states:
            print(Datalist)
            ntitle = "Total Number Of cases of Covid-19"
            ntext = f"{Datalist[1]} India:{Datalist[2]}/n Forein:{Datalist[2]}/n" \
                    f" Cured:{Datalist[2]}/n  Death:{Datalist[2]}"
            notifyMe(ntitle, ntext)

    # --------------------------------------