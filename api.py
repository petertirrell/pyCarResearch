# -*- coding: utf-8 -*-

import requests, json

from api_config import EDMUNDS_API_KEY, EDMUNDS_API_BASE

def get_nice_names(state, year, api_key):
    uri = EDMUNDS_API_BASE + 'makes?state=' + state \
        + '&year=' + year \
        + '&view=basic&fmt=json&api_key=' + EDMUNDS_API_KEY

    r = requests.get(uri)

    if r.status_code == 200:
        return r.json()['makes']
    else:
        print r.status_code
        return []


def get_all_sedans(make, year):            
    uri = EDMUNDS_API_BASE + make + '/models?state=new' \
        + '&year=' + year \
        + '&category=Sedan&view=basic&fmt=json&api_key=' + EDMUNDS_API_KEY

    r = requests.get(uri)

    if r.status_code == 200:        
        return r.json()['models']
    else:
        print r.status_code
        return []    


def get_style_for_id(style_id):
    uri = EDMUNDS_API_BASE + 'styles/' + style_id + '?view=full&fmt=json&api_key=' + EDMUNDS_API_KEY

    r = requests.get(uri)

    if r.status_code == 200:        
        return r.json()    
    else:
        print r.status_code
        return []


def get_other_details(style_id):
    uri = EDMUNDS_API_BASE + 'styles/' + style_id + '/equipment?availability=standard&equipmentType=OTHER&fmt=json&api_key=' + EDMUNDS_API_KEY

    r = requests.get(uri)

    if r.status_code == 200:        
        return r.json()    
    else:
        print r.status_code
        return []


def get_sedan_style_ids(make, year):
    rtn = []
    for model in get_all_sedans(make, year):
        for year in model['years']:
            for style in year['styles']:
                if style['id']:
                    rtn.append(str(style['id']))
    return rtn



# print out basic make/model details for a given make and year
'''
    for model in get_all_sedans(make, '2014'):
        #print model['id']
        for year in model['years']:
            #print year
            for style in year['styles']:
                #print style
                print str(model['id']) + ', ' + str(year['year']) + ', ' + str(style['id']) + ', ' + style['name']
'''                        