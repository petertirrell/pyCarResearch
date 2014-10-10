# -*- coding: utf-8 -*-

import csv
import requests, json

from api_config import EDMUNDS_API_KEY, EDMUNDS_API_BASE
from AutoDetail import AutoDetail, MyEncoder

from api import *

def write_csv_file(filename, list_of_autodetails):
    with open(filename, 'wb+') as f:
        writer = csv.writer(f)
        # print_me = ['style_id', 'make', 'model', 'year', 'name', 'MSRP'] + list_of_autodetails
        # writer.writerow(['style_id', 'make', 'model', 'year', 'name', 'MSRP'])
        writer.writerows([item.style_id, item.make,item.model,item.year,item.name,item.baseMSRP] for item in list_of_autodetails)        

makes = ['buick',
'cadillac',
'chevrolet',
'chrysler',
'dodge',
'ford',
'gmc',
'honda',
'lincoln',
'mazda',
'nissan',
'subaru',
'tesla',
'toyota',
'volkswagen']

years = ['2013', '2014', '2015']

# for make in get_nice_names('new', '2014', EDMUNDS_API_KEY):
#     print make

# print json.dumps(get_all_sedans('ford', '2014'), indent=4, sort_keys=True) 
# style_list = []
# for make in makes:
#     style_list += get_sedan_style_ids(make, '2014')

# print style_list

#my_car = AutoDetail('100079608')

cars = []
cars.append(AutoDetail('100079608'))
cars.append(AutoDetail('100924405'))

# print json.dumps(cars, cls=MyEncoder, indent=4, sort_keys=True)

# write csv
# write_csv_file('output.csv', style_list)
write_csv_file('output.csv', cars)

'''
Ford Escape XLT 2003 - style ID 100079608
Ford Focus S 2008 - style ID 100924405


'''

