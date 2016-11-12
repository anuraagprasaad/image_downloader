from urllib.parse import urlparse
from posixpath import basename, dirname

import re

def remove_empty_lines(url_list):
    return list(filter(lambda x: not re.match(r'^\s*$', x), url_list))

def remove_whitespace_character(url_list):
    return list(map(lambda string: string.strip(), url_list))

def get_path(url):
    return str(urlparse(url).path)

def get_netloc(url):
    return str(urlparse(url).netloc.replace('www.', ''))

def get_dirname(url):
    return dirname(urlparse(url).path)

def get_basename(url):
    return basename(urlparse(url).path)

def is_valid_img_url(url):
        if not urlparse(url).scheme == '' and not urlparse(url).netloc == '' and has_valid_img_ext(url):
            return True
        else:
            return False

def has_valid_img_ext(url):
    r_image_ext = re.compile(r".*\.(jpg|png|gif|bmp|jpeg)$")
    return r_image_ext.match(str(urlparse(url).path).lower())

