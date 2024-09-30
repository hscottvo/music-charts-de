from datetime import datetime

import requests


def check_updated(request: requests.models.Response) -> bool:
    print(type(request))

    return True


if __name__ == "__main__":
    r = requests.get("https://kworb.net/spotify/country/global_daily.html")
    last_modified = r.headers["Last-Modified"]
    last_modified = " ".join(last_modified.split()[1:])
    check_updated(r)

    date = datetime.strptime(last_modified, "%d %b %Y %H:%M:%S %Z")

    print(date)
