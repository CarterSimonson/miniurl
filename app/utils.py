import random
import string
from urllib.parse import urlparse
from db import get_shortened

KEY_LENGTH = 7

def is_valid_url(url):
  parsed_url = urlparse(url)
  return all([parsed_url.scheme, parsed_url.netloc])

def generate_key():
  return ''.join(random.choice(string.ascii_letters) for i in range(KEY_LENGTH))

def get_available_key():
  while True:
    key = generate_key()
    if get_shortened(key) == None:
      return key