import urllib.request
import json
import time

# Check if tqdm is installed; if it is, use it, if it isn't, define a function that just returns its input so that we don't crash later in the program.
try:
    from tqdm import tqdm
except:
    print("tqdm is not present")
    def tqdm(stuff):
        return stuff
else:
    print("tqdm is present.")

# Delay in seconds between each request.
delay = 0.2

errors = "Errors:"

f = open("data.json", "r")
data = json.loads(f.read())
f.close()

# For each key-value pair from the JSON file, attempt to download it, falling back on smaller sizes if it fails.
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
