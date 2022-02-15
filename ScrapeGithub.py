import re
import datetime

from bs4 import BeautifulSoup
import urllib.request
import re
import datetime


def extract_daily_report(date):
    date = date.strftime('%m-%d-%Y')

    BASE_URL = "https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/"

    resp = urllib.request.urlopen(f'{BASE_URL}{date}.csv')

    soup = BeautifulSoup(resp, 'html.parser', from_encoding=resp.info().get_param('charset'))

    search_word = 'Portugal'
    results = soup.body.find_all(string=re.compile('.*{0}.*'.format(search_word)), recursive=True)[0]

    return results

# dates mm-dd-yyyy
# new standard starts at '07-17-2020'
# date = '07-17-2020'

# date = datetime.datetime(2020, 7, 16)
date = datetime.datetime(2020, 7, 16)


while date.strftime('%m-%d-%Y') != datetime.datetime.now().strftime('%m-%d-%Y'):

    date += datetime.timedelta(days=1)

    print(date.strftime('%m-%d-%Y'))


    try:
        f = open("test.txt", "a")

        report = extract_daily_report(date)

        f.write(report + '\n')
        f.close()


    except:
        print('Done!')
        break
