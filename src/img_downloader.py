import os
import datetime
import urllib.request
import urllib.error

import img_utilities

def download(filename):

    url_list = read_url_file(filename)
    
    url_list = clean_url_list(url_list)

    timestamp = datetime.datetime.now().strftime('/%Y-%m-%d-%H-%M-%S/')
    total_success = 0
    total_failure = 0
    
    for url in url_list:
        img_name = img_utilities.get_basename(url)
        directory = './downloads' + timestamp

        create_dir(directory)

        if img_utilities.is_valid_img_url(url):

            try:
                path = os.path.join(directory, img_name)
                urllib.request.urlretrieve(url, path)
                print('URL retrieval successful for: ' + url)
                total_success += 1

            except urllib.error.URLError:
                print('URL retrieval failed for: ' + url)
                total_failure += 1

        else:
            print('Invalid image URL: ' + url)
            total_failure += 1

    print("URL download completed with: " + str(total_success) + " Successes and " + str(total_failure) + " Failures!")
    
# open and read the url file
def read_url_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except IOError:
        print("Error while reading File - No such file or directory! " + filename)

# perform some cleansing operation. e.g. removing empty lines or white space character etc.
def clean_url_list(url_list):
    url_list = img_utilities.remove_empty_lines(url_list)

    url_list = img_utilities.remove_whitespace_character(url_list)
    
    return url_list

# create directory for storing downloaded images
def create_dir(path):
    if path.startswith('/'):
        path = path[1:]
    if not path.endswith('/'):
        path += '/'
    os.makedirs(path, exist_ok=True)