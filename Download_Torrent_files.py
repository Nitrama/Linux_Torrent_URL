import os, sys
from pprint import pprint
import requests
dir = os.path.split(os.path.abspath(sys.argv[0]))[0]
#pprint(files)
for root, dirs, files in os.walk(dir):
    for file in files:
        if not ".git" in root and not ".md" in file and not ".py" in file and not ".torrent" in file:
            print("####",root+"/"+file)
            file = open(root+"/"+file, "r")
            for line in file:
                if ("http:" in line or "https:" in line) and not "#" in line:
                    line = line.strip()
                    print(line)
                    response = requests.request("GET",line)
                    #print(response.encoding)
                    if response.status_code == 200:
                        with open(line.split("/")[-1], 'wb') as fd:
                            for chunk in response.iter_content(chunk_size=128):
                                fd.write(chunk)
                        #file_ = open(line.split("/")[-1], 'w')
                        #file_.write(response.text)
                        #file_.close()

        #if file.endswith('.txt'):
        #    print (file)
