# Methods in this script must return the responses for the bot.
from db import getHospitalByDistrict, getHospitalByDistrictAndIndex
from typing import Type
from pymongo import MongoClient
import time
from apicall import *
from constants import ERROR_MESSAGE, LIST_DISTRICTS_RESPONSE, SOURCE


def listInstructions():
    message = '''INSTRUCTIONS

- To get a list of district codes, enter 'districts'

- To get a list of hospital codes, enter '<district code>' e.g. entering 'ARI' will return a list hospitals in Ariyalur

- To get info for a particular hospital, enter '<district code> - <hospital code>' e.g. entering 'ARI-3' will return info on Arts College, Ariyalur
'''

    return message


def subscribe(incoming):
    # incoming should be in the form 'sub <district code>'
    # 1. extract the district code
    # 2. trigger message to send a list of hospitals in that district
    # 3. process the hospital code and save to db matching user and hospitals they're subscribed to
    pass


def listDistricts():
    message = f'List of Districts\n{SOURCE}\n'

    message += LIST_DISTRICTS_RESPONSE
    print(message)
    return message


def listHospitals(incoming):
    # incoming should be in the form '<district code>'
    # 1. convert the hospital code to uppercase
    # 2. send a list of hospitals in that district
    try:
        code = incoming.upper()
    except (IndexError, TypeError, ValueError):
        return (ERROR_MESSAGE, '', '', '', '', '', '', '')
    print(incoming, code)
    message = f'HOSPITALS IN {code}\n{SOURCE}\n\n\n'
    for item in getHospitalByDistrict(code):
        message = message + str(item['index']) + \
            '.   ' + item['result']["Name"] + '\n'
    print(message)

    out = message[:1599]
    out2 = message[1600:3199]
    out3 = message[3200:4799]
    out4 = message[4800:6399]
    out5 = message[6400:7999]
    out6 = message[8000:9599]
    out7 = message[9600:11199]
    out8 = message[11200:]

    return out, out2, out3, out4, out5, out6, out7, out8


def getHospitalInfo(incoming):
    # incoming should be in the form '<district code> - <hospital code>'
    # 1. extract the district and hospital code
    # 2. check if that hospital has updates and send response
    try:
        in_district, in_num = incoming.split('-')
        district = in_district.strip()
        num = in_num.strip()
        print(district, num)
    except (IndexError, TypeError, ValueError):
        return ERROR_MESSAGE
    result = getHospitalByDistrictAndIndex(district_code=district, index=num)
    print(result)

    if result is None:
        return f'Hospital or district does not exist. {ERROR_MESSAGE}'

    bed_info = result['result']['CovidBedDetails']
    last_updated = time.ctime(bed_info["LastUpdatedTime"])
    try:
        line1 = result['result']['AddressDetail']['Line1']
    except KeyError:
        line1 = ''
    try:
        line2 = result['result']['AddressDetail']['Line2']
        if line1 == line2:
            line2 = ''
    except KeyError:
        line2 = ''
    try:
        line3 = result['result']['AddressDetail']['Line3']
        if line1 == line3 or line2 == line3:
            line3 = ''
    except KeyError:
        line3 = ''

    address = ' '.join([line1, line2, line3])
    if address == '  ':
        address = 'Not Available'

    message = f'''
BEDS INFORMATION
{SOURCE}

{result['district_name']} - {district.upper()}
{result['result']['Name']}

Vacant O2 Bed(s): {bed_info['VaccantO2Beds']}
Vacant Normal Bed(s): {bed_info['VaccantNonO2Beds']}
Vacant ICU Bed(s): {bed_info['VaccantICUBeds']}
Last updated on: {last_updated}

Address: {address}

Contact : {result['result']['PrimaryContactPerson']} - {result['result']['MobileNumber']}
'''

    return message
