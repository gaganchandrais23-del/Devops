import urllib.error
import urllib.request

BASE_URL = "http://localhost:5002"

for endpoint in ("/", "/about", "/restricted-test"):
    request = urllib.request.Request(BASE_URL + endpoint)

    try:
        with urllib.request.urlopen(request, timeout=5) as response:
            print(f"{endpoint}: HTTP {response.status}")
            print(response.read().decode())
    except urllib.error.HTTPError as error:
        print(f"{endpoint}: HTTP {error.code}")
        print(error.read().decode())
    except urllib.error.URLError as error:
        print(f"{endpoint}: connection failed: {error.reason}")
