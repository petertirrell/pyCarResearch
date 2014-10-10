# -*- coding: utf-8 -*-

import csv, json, requests, time
from datetime import datetime

from api_config import EDMUNDS_API_KEY, EDMUNDS_API_BASE
from AutoDetail import AutoDetail, MyEncoder

from api import *

OUTPUT_CSV_NAME = 'exported_auto_data.csv'

def write_csv_file(filename, list_of_autodetails):
    with open(filename, 'wb+') as f:
        writer = csv.writer(f)
        # print_me = ['style_id', 'make', 'model', 'year', 'name', 'MSRP'] + list_of_autodetails
        # writer.writerow(['style_id', 'make', 'model', 'year', 'name', 'MSRP'])
        writer.writerow(['STYLEID', 'MAKE', 'MODEL', 'YEAR', 'NAME', 'MSRP', 'MPG_CITY', 'MPG_HIGHWAY', 'MPG_COMBINED',
            'FUEL_CAPACITY', 'HORSEPOWER', 'TORQUE', 'ENGINE', 'WIDTH', 'HEIGHT', 'LENGTH', 'ROW1LEGROOM', 'ROW2LEGROOM',
            'ROW1HEADROOM', 'ROW2HEADROOM', 'CARGO_CAPACITY', 'MAX_CARGO'])
        writer.writerows([item.style_id, 
            item.make,item.model,item.year,item.name,item.baseMSRP,
            item.mpg_city, item.mpg_highway, item.mpg_combined, item.fuel_capacity,
            item.engine_horsepower, item.engine_torque, item.engine_type,
            item.width, item.height, item.length, 
            item.row_1_legroom, item.row_2_legroom, item.row_1_headroom, item.row_2_headroom,
            item.cargo_capacity_allseats, item.cargo_capacity_max] for item in list_of_autodetails)        

# list of makes that I'm interested in
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

# model years to query
years = ['2013', '2014', '2015']

# for comparison, these are the style IDs for our current cars
'''
Ford Escape XLT 2003 - style ID 100079608
Ford Focus S 2008 - style ID 100924405
'''
seed_style_ids = ['100079608', '100924405'] 

cars = []

# populate with initial comparison IDs
for style in seed_style_ids:
    cars.append(AutoDetail(style))

# get style ids for sedans for each make
style_list = []
for year in years:
    for make in makes:
        print '{2} Getting sedans for {0} {1}'.format(year, make, str(datetime.now()))
        style_list += get_sedan_style_ids(make, year)
        # getting occasional 403s so gotta slow it down...
        time.sleep(1)

print 'Found {0} styles!'.format(len(style_list))

# now for each style ID build out detail!
for style in style_list:
    print '{1} Looking up style {0}'.format(style, str(datetime.now()))
    cars.append(AutoDetail(style))

# print json.dumps(cars, cls=MyEncoder, indent=4, sort_keys=True) # useful for debugging

# write csv
print '{1} Writing CSV file to {0}'.format(OUTPUT_CSV_NAME, str(datetime.now()))
write_csv_file(OUTPUT_CSV_NAME, cars)



