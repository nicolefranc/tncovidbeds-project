from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.environ['MONGODB_URL'])
db = client[os.environ['DB_NAME']]
hospitals = db[os.environ['COLLECTION_NAME']]


def getHospitalByHospitalId(hospital_id):
    hospital = hospitals.find_one(
        {'hospital_id': hospital_id})

    return hospital


def getHospitalByDistrictAndIndex(district_code, index):
    hospital = hospitals.find_one(
        {"$and": [{'district_short': district_code.upper()}, {'index': int(index)}]})

    return hospital


def getHospitalByDistrict(district_code):
    hospital = hospitals.find({'$and': [{'district_short': district_code},
                                        {'$or': [{'result.CovidBedDetails.VaccantO2Beds': {'$ne': 0}},
                                                 {'result.CovidBedDetails.VaccantNonO2Beds': {
                                                     '$ne': 0}},
                                                 {'result.CovidBedDetails.VaccantICUBeds': {'$ne': 0}}, ]}
                                        ]})

    return hospital


def updateHospital(hospital_id, updatedData):
    hospital = hospitals.update_one(
        filter={'hospital_id': hospital_id},
        update={'$set': {
            'result': updatedData
        }}
    )

    return hospital
