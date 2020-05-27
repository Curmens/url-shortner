    # importing required libraries

from __future__ import with_statement
import contextlib
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
import sys
import argparse


    # using tinyurl api for shortening given urls 
def make_tiny(url):
    request_url = ('http://tinyurl.com/api-create.php?' + 
    urlencode({'url':url}))
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')

# Create the parser
my_parser = argparse.ArgumentParser(description='Shortens url')

# Add the arguments
my_parser.add_argument('Url', metavar='url', nargs='*', help='add your url to sohrten')

# Execute the parse_args() method
args = my_parser.parse_args()

input_url = args.Url
print(input_url)
# using sys.argv to collect sample urls
def main():
    for tinyurl, urls in zip(map(make_tiny, input_url), input_url):
        print(tinyurl + ' ===>> ' + urls)



if __name__ == '__main__':
    main()