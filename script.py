import requests
from bs4 import BeautifulSoup
import re
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
def get_dlink(ep_link,ep):
	page=requests.get(ep_link)
	soup = BeautifulSoup(page.text, 'html.parser')
	print("\033[1m [+] Episode ["+str(ep)+"] download links: \033[0m")
	for d_link in soup.find("div", class_="downloads").find("ul").findChildren("a" , recursive=False): 
		mirror_name=re.sub('[^a-zA-Z0-9]+', '', d_link.getText())
		print(style.YELLOW+"  > "+style.RESET+"\033[1m ["+style.YELLOW+mirror_name+style.RESET+"]: \033[0m"+d_link.get('href'))
print(style.RED+"""
 █████╗ ███╗   ██╗██╗███╗   ███╗███████╗    ██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ 
██╔══██╗████╗  ██║██║████╗ ████║██╔════╝    ██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
███████║██╔██╗ ██║██║██╔████╔██║█████╗      ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝
██╔══██║██║╚██╗██║██║██║╚██╔╝██║██╔══╝      ██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
██║  ██║██║ ╚████║██║██║ ╚═╝ ██║███████╗    ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝╚══════╝    ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                                                                  
	"""+style.RESET)
print("""					   __  ___      ___       __      __          
					  /  |/  /___  / _ \___ _/ /_____/ /  ___ ____
					 / /|_/ / __/ / ___/ _ `/ __/ __/ _ \/ -_) __/
					/_/  /_/_/   /_/   \_,_/\__/\__/_//_/\__/_/   
                                              
                                              """)
print(style.GREEN+style.BOLD+"ANIME DOWNLOADER V1 \nThis script allows you to get the download link of animes with Arabic subs\n"+style.YELLOW+"[+]Github : https://github.com/Eljakani"+style.RESET)
name=input('\033[1m=>\033[0m Enter an anime name : \033[1m ')
print(style.GREEN+"[+] Looking for Animes ..."+style.RESET)
page=requests.get('https://ww.xsanime.com/?s='+name+'&type=anime')
html_text = page.text
soup = BeautifulSoup(html_text, 'html.parser')
index=0
for anime in soup.find_all("div", class_="itemtype_anime"):
	if "فيلم" in anime.find("h4").get_text():
		print("\033[1m ["+str(index)+"](Movie) \033[0m"+re.sub('[^a-zA-Z0-9 ]+', '', anime.find("h4").get_text()))
	else:
		print("\033[1m ["+str(index)+"] \033[0m"+anime.find("h4").get_text())
	index+=1
if len(soup.find_all("div", class_="itemtype_anime"))==0:
	print(style.RED+"[!] No Anime Found "+style.RESET)
	exit()
choice=input('\033[1m=>\033[0m Choose your anime : \033[1m ')
if int(choice) <= len(soup.find_all("div", class_="itemtype_anime"))-1:
	print(style.GREEN+"[+] Gathering Anime Information ..."+style.RESET)
else:
	print(style.RED+"ERROR"+style.RESET)
	exit()
link = soup.find_all("div", class_="itemtype_anime")[int(choice)].find('a').get('href')
page=requests.get(link)
soup = BeautifulSoup(page.text, 'html.parser')
if "فيلم" in soup.find("title").get_text():
	print(style.GREEN+style.BOLD+" [+] General Info:"+style.RESET+style.YELLOW)
	print("  Movie Name : ["+style.GREEN+str(re.sub('[^a-zA-Z0-9 ]+', '', soup.find("h1", class_="post--inner-title").get_text()))+style.RESET+style.YELLOW+"] / Rating :  ["+style.GREEN+re.sub('[^a-zA-Z0-9.]+','',soup.find("div", class_="Ratings").get_text())+style.YELLOW+"]"+style.RESET)
	print(style.GREEN+"[+] Collecting Movie download links ..."+style.RESET)
	print("\033[1m [+] Movie download links: \033[0m")
	for d_link in soup.find("div", class_="downloads").find("ul").findChildren("a" , recursive=False): 
		mirror_name=re.sub('[^a-zA-Z0-9]+', '', d_link.getText())
		print(style.YELLOW+"  > "+style.RESET+"\033[1m ["+style.YELLOW+mirror_name+style.RESET+"]: \033[0m"+d_link.get('href'))
else:
	episodes = len(soup.find("div", class_="EpisodesList").findChildren("a" , recursive=False))
	print(style.GREEN+style.BOLD+" [+] General Info:"+style.RESET+style.YELLOW)
	print("  Anime Full Name : ["+style.GREEN+str(re.sub('[^a-zA-Z0-9 ]+', '', soup.find("h1", class_="post--inner-title").get_text()))+style.RESET+style.YELLOW+"] / EPs :  ["+style.GREEN+str(episodes)+style.YELLOW+"]"+style.RESET)
	ep_choice=input('\033[1m=>\033[0m Choose EP (0 to download all EPs) : \033[1m ')
	print(style.GREEN+"[+] Collecting download links ..."+style.RESET)
	if int(ep_choice) == 0:
		for x in range(episodes):
			actual_ep_order=int(episodes)-int(x+1)
			ep_link = soup.find("div", class_="EpisodesList").findChildren("a" , recursive=False)[int(actual_ep_order)].get('href')
			get_dlink(ep_link=ep_link,ep=x+1)
	elif int(ep_choice) <= episodes:
		actual_ep_order=int(episodes)-int(ep_choice)
		ep_link = soup.find("div", class_="EpisodesList").findChildren("a" , recursive=False)[int(actual_ep_order)].get('href')
		get_dlink(ep_link=ep_link,ep=ep_choice)
	else:
		print('Error')
		exit()
