#!/usr/bin/python3
TOKEN="RokNHxieRWZySdOCslYJgbJCLGLOtZnVYNIZChsi"

import discogs_client
from mixes_extract_mixdb import mixesdb_extractor
import slskd_api


d = discogs_client.Client('download_mix_files/1.0', user_token=TOKEN)

ltracks = mixesdb_extractor.get_list("Laurent Garnier",5)
track = ltracks[5]
release = d.search(track['artist'] + " - " + track['title'])[0]
print()
print('*****')
print(track)
print()
print(release.title)

# for track in ltracks:
#     if(track):
#         try:
#             release = d.search(track['artist'] + " - " + track['title'])[0]
#             print()
#             print('*****')
#             print(track)
#             print()
#             print(release.title)
#         except:
#             pass