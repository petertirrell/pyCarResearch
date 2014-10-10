# -*- coding: utf-8 -*-

import json, time

from api import *

class AutoDetail(object):
    """
    Class to describe automobile details I want to track
    """
    style_id = -1
    make = ''
    model = ''
    year = ''
    name = ''
    baseMSRP = 0
    engine_horsepower = 0
    engine_torque = 0
    engine_type = ''

    width = 0
    length = 0
    height = 0

    mpg_city = 0
    mpg_highway = 0
    mpg_combined = 0
    fuel_capacity = 0

    row_1_legroom = 0
    row_2_legroom = 0
    row_1_headroom = 0
    row_2_headroom = 0

    cargo_capacity_allseats = 0
    cargo_capacity_max = 0

    

    def __init__(self, style_id):
    	self.style_id = style_id

        # get details for this style id
    	my_style = get_style_for_id(str(style_id))

        if my_style:        
            self.make = my_style['make']['name']
            self.model = my_style['model']['name']
            self.year = str(my_style['year']['year'])
            self.name = my_style['name']
            self.baseMSRP = my_style['price']['baseMSRP']
            self.engine_horsepower = my_style['engine']['horsepower']
            self.engine_torque = my_style['engine']['torque']
            self.engine_type = my_style['engine']['type']

        details = get_other_details(style_id)
        time.sleep(1)

        if details:
            for each in details['equipment']:
                if each['name'] == 'Specifications':
                    for attribute in each['attributes']:
                        if attribute['name'] == 'Epa Combined Mpg':
                            self.mpg_combined = attribute['value']
                        if attribute['name'] == 'Epa City Mpg':
                            self.mpg_city == attribute['value']
                        if attribute['name'] == 'Epa Highway Mpg':
                            self.mpg_highway = attribute['value']
                        if attribute['name'] == 'Fuel Capacity':
                            self.fuel_capacity = attribute['value']
                if each['name'] == 'Exterior Dimensions':
                    for attribute in each['attributes']:
                        if attribute['name'] == 'Overall Length':
                            self.length = attribute['value']
                        if attribute['name'] == 'Overall Width Without Mirrors':
                            self.width = attribute['value']
                        if attribute['name'] == 'Overall Height':
                            self.height = attribute['value']
                if each['name'] == 'Interior Dimensions':
                    for attribute in each['attributes']:
                        if attribute['name'] == '1st Row Leg Room':
                            self.row_1_legroom = attribute['value']
                        if attribute['name'] == '1st Row Head Room':
                            self.row_1_headroom = attribute['value']
                        if attribute['name'] == '2nd Row Leg Room':
                            self.row_2_legroom = attribute['value']
                        if attribute['name'] == '2nd Row Head Room':
                            self.row_2_headroom = attribute['value']
                if each['name'] == 'Cargo Dimensions':
                    for attribute in each['attributes']:
                        if attribute['name'] == 'Cargo Capacity, All Seats In Place':
                            self.cargo_capacity_allseats = attribute['value']
                        if attribute['name'] == 'Max Cargo Capacity':
                            self.cargo_capacity_max = attribute['value']                       


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if not isinstance(obj, AutoDetail):
            return super(MyEncoder, self).default(obj)

        return obj.__dict__