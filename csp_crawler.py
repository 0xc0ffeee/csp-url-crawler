from __future__ import print_function
from requests import get, exceptions
import sys

##Author: 0xc0ffee => https://twitter.com/0xc0ffee_
##Description: Quick and dirty tool based on https://github.com/yamakira/domains-from-csp to grab a file with URLs and grab domains from their Content-Security Policy
##Note: Beta version - not handling exceptions. All URLs in the file need to be preceded by a scheme (http:// or https://) and need to be separated by a new line.
##Usage: ./csp_crawler.py <file.txt>

def get_csp_header():
    with open(sys.argv[1],"r") as file:
        for line in file:
            line = line.rstrip()
            try:
                r = get(line)

                if 'Content-Security-Policy' in r.headers:
                    csp_header = r.headers['Content-Security-Policy']
                    get_domains(csp_header)
                else:
                    print ("No CSP for "+line)

            except:
                pass
    file.close()

def get_domains(csp_header):
    domains = []
    csp_header_values = csp_header.split(" ")
    for line in csp_header_values:
        if "." in line:
            line = line.replace(";","")
            domains.append(line)
            print (line)
        else:
            pass

get_csp_header()
