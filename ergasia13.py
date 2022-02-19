import urllib.request
from urllib.request import Request, urlopen
import json
req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
data=json.loads(data)
randomness=data["randomness"]

n = 2
split_string = [randomness[i:i+n] for i in range(0, len(randomness), n)]
new_split_string=[]#κενη για να προσθεσω τα διαγεγραμμενα διπλα
for item in split_string:   
    item=(int(item, 16))
    item=item%80  
    if item not in new_split_string:
        new_split_string.append(item)      
random_nums=new_split_string
print("Random numbers from Cloudflare:",random_nums)
print(" ")

url="https://api.opap.gr/draws/v3.0/1100/last-result-and-active "
reqq=Request('https://api.opap.gr/draws/v3.0/1100/last-result-and-active')
data1 = urlopen(reqq).read()
data1=json.loads(data1)
Kino_winning_num=data1['last']['winningNumbers']['list']
print("Kino winnig numbers:",Kino_winning_num)
print(" ")
common_numbers=set(random_nums).intersection(Kino_winning_num)
print(" ")
print("Randomm numbers from Cloudflare that would be drawn in the last draw of KINO:",common_numbers)
        

 

    
 


