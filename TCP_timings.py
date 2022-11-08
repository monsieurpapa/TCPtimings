'''Author : Dieudonne MUNGANGA
Email : dieudonneishara@gmail.com 

ABout the script :
This script measures TCP timings of a list of websites . The websites used are the mostly accessed webisites in DRC according to Open .Trends : https://www.semrush.com/trending-websites/cd/all

This is a step towards measuring users' Web Quality of Experience.
'''


import pycurl, time
c = pycurl.Curl()
import pandas as pd
from datetime import datetime
import certifi
#website='https://technixmw.com'
#c.setopt(c.VERBOSE, False) # to see request details
ts = time.process_time()
def tcp_timings(website):
    website = 'https://www.{0}'.format(website)
    c.setopt(pycurl.WRITEFUNCTION, lambda x: None) ##hide data
    #response = requests.get(website)
    c.setopt(pycurl.CAINFO, certifi.where())
    c.setopt(c.URL, website)
    c.perform()
    tcp_timings = {}
    tcp_timings['domain'] = c.getinfo(pycurl.EFFECTIVE_URL)
    tcp_timings['IPAddress'] = c.getinfo(pycurl.PRIMARY_IP)
    #tcp_timings['Port'] = c.getinfo(pycurl.PRIMARY_PORT)
    tcp_timings['DNST'] = c.getinfo(pycurl.NAMELOOKUP_TIME)
    #tcp_timings['SSLT'] = c.getinfo(pycurl.APPCONNECT_TIME)
    tcp_timings['TCPT'] = c.getinfo(pycurl.CONNECT_TIME)
    tcp_timings['TTFB'] = c.getinfo(pycurl.PRETRANSFER_TIME)
    #tcp_timings['redirect'] = c.getinfo(pycurl.REDIRECT_TIME)
    tcp_timings['starttransfer'] = c.getinfo(pycurl.STARTTRANSFER_TIME)
    tcp_timings['total-time'] = c.getinfo(pycurl.TOTAL_TIME)
    tcp_timings['http-code'] = c.getinfo(pycurl.HTTP_CODE)
    tcp_timings['redirect-count'] = c.getinfo(pycurl.REDIRECT_COUNT)
    tcp_timings['size-upload'] = c.getinfo(pycurl.SIZE_UPLOAD)
    tcp_timings['size-download'] = c.getinfo(pycurl.SIZE_DOWNLOAD)
    tcp_timings['header-size'] = c.getinfo(pycurl.HEADER_SIZE)
    tcp_timings['request-size'] = c.getinfo(pycurl.REQUEST_SIZE)
    tcp_timings ['date'] = today
    #tcp_timings['content-length-download'] = c.getinfo(pycurl.CONTENT_LENGTH_DOWNLOAD)
    #cp_timings['content-length-upload'] = c.getinfo(pycurl.CONTENT_LENGTH_UPLOAD)
    #tcp_timings['content-type'] = c.getinfo(pycurl.CONTENT_TYPE)
    tcp_timings['response-code'] = c.getinfo(pycurl.RESPONSE_CODE)
    #tcp_timings['Protocol'] = c.getinfo(pycurl.PROTOCOL)
    #tcp_timings['certificate-info'] = c.getinfo(pycurl.INFO_CERTINFO)
    #tcp_timings['filetime'] = c.getinfo(pycurl.INFO_FILETIME)
    #tcp_timings['starttransfer-time'] = c.getinfo(pycurl.STARTTRANSFER_TIME)
    #tcp_timings['redirect-time'] = c.getinfo(pycurl.REDIRECT_TIME)
    tcp_timings['redirect-count'] = c.getinfo(pycurl.REDIRECT_COUNT)
    #tcp_timings['http-connectcode'] = c.getinfo(pycurl.HTTP_CONNECTCODE)
    # tcp_timings['httpauth-avail'] = c.getinfo(pycurl.HTTPAUTH_AVAIL)
    # tcp_timings['proxyauth-avail'] = c.getinfo(pycurl.PROXYAUTH_AVAIL)
    # tcp_timings['os-errno'] = c.getinfo(pycurl.OS_ERRNO)
    #tcp_timings['num-connects'] = c.getinfo(pycurl.NUM_CONNECTS)
    #tcp_timings['ssl-engines'] = c.getinfo(pycurl.SSL_ENGINES)
    # tcp_timings['cookielist'] = c.getinfo(pycurl.INFO_COOKIELIST)l
    # tcp_timings['lastsocket'] = c.getinfo(pycurl.LASTSOCKET)
    # tcp_timings['ftp-entry-path'] = c.getinfo(pycurl.FTP_ENTRY_PATH)
    #print(response.text)
    return tcp_timings

if __name__ == "__main__":
    DRC_globally = ['google.com','y2mate.com','kooora.com','mangafreak.net','youtube.com',
            'savefrom.net','xvideos.com','rarbgdata.org','pornhub.com','xnxx.com','googlevideo.com','torrent9.re',
            'vostfree.cx', 'evolve-rdc.com','aliexpress.com','frenchstream.site','facebook.com','voiranime.com','wikipedia.org',
'matchendirect.fr','premierbet.cd','premierbet.com','theguardian.com',
'torrent9.to', '1377x.is']
    DRC_locally = ['google.cd','radiookapi.net','politico.cd','7sur7.cd','senat.cd','presidence.cd','senat.cd','facebook.com', 'twitter.com', 'youtube.com']
    results = []
    local_results =[]
    today = datetime.today()
    for site in DRC_globally:
        print('doing :' + site)
        results.append(tcp_timings(site))
    print('Done')
    global_data =pd.DataFrame(results)
    global_data.to_csv(str(today) + '_globaldata.csv')

    for site in DRC_locally:
        print('doing :' + site)
        local_results.append(tcp_timings(site))
    local_data = pd.DataFrame(local_results)
    local_data.to_csv(str(today) + '_localdata.csv'.format(today))

