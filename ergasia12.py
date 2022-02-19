from random import random
import urllib.request
from urllib.request import Request, urlopen
from io import StringIO
import json
req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
data=json.loads(data)
round=data["round"]
randomness=data["randomness"]

big_string = StringIO()
for i in range(98):
    req = Request(f'https://drand.cloudflare.com/public/{round-1}', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(req).read()
    data=json.loads(data)
    round=data["round"]
    randomness=data["randomness"]
    big_string.write(randomness)
big_randomness=randomness+big_string.getvalue() 
bin = ''.join(format(i, '08b') for i in bytearray(big_randomness, encoding ='utf-8'))
print(bin)
def max_consecutive_0(x): 
     return  max(map(len,x.split('1')))

def max_consecutive_1(x): 
     return  max(map(len,x.split('0')))
print(" ")
print("Maximum length of consecutive 0’s:")
print(max_consecutive_0(bin))

print(" ")
print("Maximum length of consecutive 1’s:")
print(max_consecutive_1(bin))


