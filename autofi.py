import urllib2
import wifi
import os
import time
def internet_on():
    try:
        urllib2.urlopen('http://google.com', timeout=1)
        return True
    except urllib2.URLError as err: 
        return False

def FindFromSavedList(ssid):
    cell = wifi.Scheme.find('wlp3s0', ssid)

    if cell:
        return cell

    return False

def Search():
    wifilist = []

    cells = wifi.Cell.all('wlp3s0')

    for cell in cells:
        wifilist.append(cell)

    return wifilist

if __name__ == '__main__':
	status = ''
	n = 0
	while True:
		a = internet_on()
		if a == True:
			print('Internet Available')
			status = 'online'
			time.sleep(10)
		else:
			print("We are Offline.")
			os.system('root | sudo -S systemctl restart NetworkManager')
			a = internet_on()
			if a == True:
				status = 'online'
			else:
				status = 'offline'
			if n != 500:
				n+=5
		if status == 'offline':
			wifilist = Search()
			for wifi in wifilist:
				s = FindFromSavedList(wifi.ssid)
				if s:
					s.activate()
				else:
					if not wifi.encrypted:
						wifi.activate()
			time.sleep(20+n)