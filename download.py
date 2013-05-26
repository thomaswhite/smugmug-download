#!/usr/bin/env python2
from smugpy import SmugMug

API_KEY = os.environ['SMUGMUG_API_KEY']
NICKNAME = os.environ['SMUGMUG_NICKNAME']

smugmug = SmugMug(api_key=API_KEY, api_version="1.3.0", app_name="Download")
albums = smugmug.albums_get(NickName=NICKNAME)

for album in albums["Albums"]:
    print "%s, %s" % (album["id"], album["Title"])
