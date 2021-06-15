from db import getHospitalByHospitalId, updateHospital
from constants import DISTRICT_CODES
import requests


def fetchHospitals():
    print("Fetching data...")
    url = r'https://tncovidbeds.tnega.org/api/hospitals'

    d = {
        "searchString": "",
        "sortCondition": {"Name": 1},
        "pageNumber": 1,
        "pageLimit": 2000,
        "SortValue": "Availability",
        "Districts": DISTRICT_CODES,
        "IsGovernmentHospital": "true",
        "IsPrivateHospital": "true",
        "FacilityTypes": ["CHO", "CHC", "CCC"]
    }

    headers = {
        'Content-Type': 'application/json'
    }

    res = requests.post(url, json=d, headers=headers)
    results = res.json()["result"]

    hospitalCount = len(results)

    print(f"{hospitalCount} hospitals found.")
    checkUpdates(results)


def checkUpdates(hospitals):
    print("Checking for updates...")

    for index, hospital in enumerate(hospitals):
        hospitalName = hospital["Name"]
        hospitalId = hospital["_id"]

        storedHospital = getHospitalByHospitalId(hospital_id=hospitalId)
        print(hospitalId)

        if storedHospital is not None:
            print(storedHospital["district_name"])
            storedUpdatedDateTime = storedHospital["result"]["UpdatedDateTime"]

            # Check if retrieved updatedTime is greater than stored updatedTime
            isUpdated = hospital["UpdatedDateTime"] > storedUpdatedDateTime

            if isUpdated:
                updateHospital(hospital_id=hospitalId,
                               updatedData=hospital)  # update the data
                print(f"{index}- UPDATED {hospitalName}!")
            else:
                print(f"{index}- No updates for {hospitalName}.")
        else:
            # TODO: add the new hospital entry in db
            print("Hospital doesn't exist in DB")

    # Separator
    print("==============================================\n")


def fetchDistricts():
    print("Fetching data...")
    url = "https://tncovidbeds.tnega.org/api/district"

    payload = {}
    headers = {}

    res = requests.request("GET", url, headers=headers, data=payload)
    return res.json()["result"]
