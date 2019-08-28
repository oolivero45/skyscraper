import urllib.request
import json
from tqdm import tqdm
import time

delay = 0.2
errors = "Errors:"

f = open("data.json", "r")
data = json.loads(f.read())
f.close()

for url, name in tqdm(data.items()):
    try:
        urllib.request.urlretrieve(url, "images/" + name.replace("&", "AND").replace("/", "SLASH") + ".png")
        time.sleep(delay)
    except:
        print("ERRORED 640x280, TRYING 320x140: " + url)
        errors += "\nERRORED 640x280, TRYING 320x140: " + url
        try:
            urllib.request.urlretrieve(url.replace("/640/280/", "/320/140/"), "images/" + name.replace("&", "AND").replace("/", "SLASH") + ".png")
            time.sleep(delay)
        except:
            print("ERRORED 320x140, TRYING 160x70: " + url)
            errors += "\nERRORED 320x140, TRYING 160x70: " + url
            try:
                urllib.request.urlretrieve(url.replace("/640/280/", "/160/70/"), "images/" + name.replace("&", "AND").replace("/", "SLASH") + ".png")
                time.sleep(delay)
            except:
                print("ERRORED 160x70, TRYING 80x35: " + url)
                errors += "\nERRORED 160x70, TRYING 80x35: " + url
                try:
                    urllib.request.urlretrieve(url.replace("/640/280/", "/80/35/"), "images/" + name.replace("&", "AND").replace("/", "SLASH") + ".png")
                    time.sleep(delay)
                except:
                    print("ERRORED 80x35, NO MORE ALTERNATIVES: " + url)
                    errors += "\nERRORED 80x35, NO MORE ALTERNATIVES: " + url

print("\n" * 100)
print("Done!")
print(errors)
