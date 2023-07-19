
# IMPORTANT: RUN THIS CELL IN ORDER TO IMPORT YOUR KAGGLE DATASETS
# TO THE CORRECT LOCATION (/kaggle/input) IN YOUR NOTEBOOK,
# THEN FEEL FREE TO DELETE CELL.

import os
import sys
from tempfile import NamedTemporaryFile
from urllib.request import urlopen
from urllib.parse import unquote
from urllib.error import HTTPError
from zipfile import ZipFile

CHUNK_SIZE = 40960
DATASET_MAPPING = 'google-research-identify-contrails-reduce-global-warming:https%3A%2F%2Fstorage.googleapis.com%2Fkaggle-competitions-data%2Fkaggle-v2%2F51753%2F5692552%2Fbundle%2Farchive.zip%3FX-Goog-Algorithm%3DGOOG4-RSA-SHA256%26X-Goog-Credential%3Dgcp-kaggle-com%2540kaggle-161607.iam.gserviceaccount.com%252F20230711%252Fauto%252Fstorage%252Fgoog4_request%26X-Goog-Date%3D20230711T195716Z%26X-Goog-Expires%3D259200%26X-Goog-SignedHeaders%3Dhost%26X-Goog-Signature%3D79673c645033fc507124950a8fcae4d215a126a99e6581caf88611b6e1c62f66bdf1d9f112b6eb47cbb848b5d8362ef1eb84f39f5d7e84fce63049c25e1df3bc401866affdb9a2252c07068a1f4aa0150119668c3be0bfac605917cbfae3bfb78b6df57abf00d2e242b82a7dca631d8d837848ba988ecdcf97c24305e4af22756fa927cc70ba3c0814cb1dd1c88ad5d7a5611658f5a3a48134aedd939743109f03661f8dabfcecb42d100091e24bc159dc53b2a15cb2b00032acb1ee022b683842a8f549fb2c7ceb37deaa6452587d9b9a1c5e5523481c44b0d38ea835d58b134faae9cea6772c3f56e68370639d80aa33d9703e4b381ba37d4c641250cad1fd'

HOME_DIR = '/home/jupyter'

KAGGLE_INPUT_PATH=os.path.join(HOME_DIR, 'kaggle/input')
#KAGGLE_INPUT_SYMLINK='kaggle'

TEMP_DIR = os.path.join(HOME_DIR, 'temp')
TEMP_FILE = os.path.join(TEMP_DIR, 'archive.zip')

#os.makedirs(KAGGLE_INPUT_PATH, 777)
#os.symlink(KAGGLE_INPUT_PATH, os.path.join('..', 'input'), target_is_directory=True)
#os.makedirs(KAGGLE_INPUT_SYMLINK)
#os.symlink(KAGGLE_INPUT_PATH, os.path.join(KAGGLE_INPUT_SYMLINK, 'input'), target_is_directory=True)

for dataset_mapping in DATASET_MAPPING.split(','):
    directory, download_url_encoded = dataset_mapping.split(':')
    download_url = unquote(download_url_encoded)
    destination_path = os.path.join(KAGGLE_INPUT_PATH, directory)
    try:
#        with urlopen(download_url) as zipfileres, NamedTemporaryFile(dir=TEMP_DIR) as tfile:
        with urlopen(download_url) as zipfileres, open(TEMP_FILE, 'wb') as tfile:
            total_length = zipfileres.headers['content-length']
            print(f'Downloading {directory} to {tfile.name}, {total_length} bytes zipped')
            dl = 0
            data = zipfileres.read(CHUNK_SIZE)
            while len(data) > 0:
                dl += len(data)
                tfile.write(data)
                done = int(50 * dl / int(total_length))
                sys.stdout.write(f"\r[{'=' * done}{' ' * (50-done)}] {dl} bytes downloaded")
                sys.stdout.flush()
                data = zipfileres.read(CHUNK_SIZE)
            print(f'\nUnzipping {directory}')
            with ZipFile(tfile) as zfile:
                zfile.extractall(destination_path)
    except HTTPError as e:
        print(f'Failed to load (likely expired) {download_url} to path {destination_path}')
        continue
    except OSError as e:
        print(f'Failed to load {download_url} to path {destination_path}')
        continue
print('Dataset import complete.')
