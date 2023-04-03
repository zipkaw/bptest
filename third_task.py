import urllib.request as rq
import matplotlib.pyplot as plt
from collections import defaultdict

url = 'http://www.python.org/'

response = rq.urlopen(url)

symbol = defaultdict(int)

for line in response.readlines():
    for char in line: 
        symbol[char] += 1

plt.bar([chr(_) for _ in symbol.keys()], 
        symbol.values(), 
        width=0.2)

plt.show()