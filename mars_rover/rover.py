import json
import os
import requests
import urllib
import webbrowser


class Rover:
    def __init__(self, date):
        self.date = date
    
    def retrieve_photo(self):
        url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?'
        params = {
            'earth_date': self.date,
            'api_key': 'oaUQy2gye3023IgJeDMVAbQkNCwCbB9fQNFMoiWR',
        }

        response = None

        try:
            # Check for error in response
            response = requests.get(url, params)
            response.raise_for_status()
        except Exception as err:
            print('Error has occured: %s' % err)
        
        if response:
            data = response.json()
            folder = 'images/%s' % self.date.strftime('%Y-%m-%d')
            if not os.path.exists(folder):
                os.makedirs(folder)

            print('%s\nDownloading images...' % self.date.strftime('%Y-%m-%d'))
            file_path = None
            for photo in data['photos']:
                file_name = photo['img_src'].split('/')[-1]
                file_path = os.path.join(folder, file_name)

                if not os.path.exists(file_path):
                    urllib.request.urlretrieve(photo['img_src'], file_path)
            
            print('Downloaded %s images.' % len(data['photos']))

            if file_path:
                # Opens last downloaded photo
                webbrowser.open(file_path)
    