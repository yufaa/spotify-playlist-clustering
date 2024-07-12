import pandas as pd
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import datetime

import sqlite3


DATABASE_LOCATION = "sqlite://my_played_tracks.sqlite"
USER_ID = "whoami"
TOKEN = "BQCZ5cCy0hwTNDzswIK1pyV7G5L10KGoTAkimEYO-WpH8nJTYO_3nOPKzGJjJSCsGDXJS58puP_FSXk5gFlALcO1XY1tLtmBJufFn6eIIQIfBVuDmnY"


if __name__ == "__main__":

    headers = {
        "Accept" : "application/json",
        "Content-Type" : "application/json",
        "Authorization" : "Bearer {token}".format(token=TOKEN)
    
    }

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000

    r = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterday_unix_timestamp), headers=headers)

    data = r.json()

    print(data)

