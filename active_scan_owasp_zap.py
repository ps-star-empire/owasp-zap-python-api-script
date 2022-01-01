from zapv2 import ZAPv2

import time

#target url for scan

target = 'http://testphp.vulnweb.com'

apikey = '8ij7v7nl0t6d777okrh4kf3icb'



zap = ZAPv2(apikey=apikey,proxies={'http':'http://localhost:8081','https':'http://localhost:8081'})

zap.urlopen(target)



#Passive scan

while (int(zap.pscan.records_to_scan) > 0):

    print ('Passive Scan Records %: ' + zap.pscan.records_to_scan)

    time.sleep(5)



print('Passive Scan Completed..!')

#Active Scan

zap.ascan.scan(url=target,apikey = apikey)

time.sleep(5)

while int(zap.ascan.status()) < 100:

    print ('Active Scan Progress %: ' + zap.ascan.status())

    time.sleep(5)

print ('Active Scan completed..!')



# HTML Report

with open ('report.html', 'w') as f:f.write(zap.core.htmlreport(apikey = 'apikey'))

# XML Report

#with open ('report.xml', 'w') as f:f.write(zap.core.xmlreport(apikey = 'apikey'))



#zap.core.shutdown()