import argparse
import json
import sys
import requests

baseURL = "http://digital-factory.herokuapp.com"
dataa = str(open('order.txt', 'r').read().replace("'", "\""))
#dat = """ {'name' : %s}""" % dataa

dat= """ {\"name\" : \"isaacc\"}"""
print(dat)
tok = requests.post(baseURL+ '/api/token', data=dat) 
print(tok.content) 
"""
dat = requests.get(baseURL+ '/api/token', data=dat)
print(dat.content) 

tok = requests.put(baseURL+ '/api/token', data=dat)
print(tok.content) 
"""
