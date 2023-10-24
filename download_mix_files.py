#!/usr/bin/python3
TOKEN="RokNHxieRWZySdOCslYJgbJCLGLOtZnVYNIZChsi"

import discogs_client
import mixesdb_extractor

d = discogs_client.Client('download_mix_files/1.0', user_token=TOKEN)

ltracks = mixesdb_extractor.get_list("Laurent Garnier",5)

for track in ltracks:
    if '[' in track:
        title = track['title'].split('[')[0]
    else:
        title = track['title']
    
    results = d.search(title + " " + track['artist'])
    print()
    print('*****')
    print(track)
    print()
    try:
        if results.page(1)[0]:
            print(results.page(1)[0])
    except:
        pass