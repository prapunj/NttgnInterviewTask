import urllib.request

urls = ["http://localhost:8000/interfaces", "http://localhost:8000/interface/FastEthernet0/0"]

for i in urls:
    req = urllib.request.urlopen(i)
    print(req.read().decode())