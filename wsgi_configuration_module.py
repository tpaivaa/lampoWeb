import os
import sys

sys.path.append('/var/www/server/lampo')

os.environ['PYTHON_EGG_CACHE'] = '/var/www/server/lampo/.python-egg'

def application(environ, start_response):
    status = '200 OK'
    output = 'Hello World!\n You Lose !'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]
