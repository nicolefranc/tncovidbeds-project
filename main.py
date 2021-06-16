import schedule
import time
from apicall import fetchHospitals

# Fetch data every hour
schedule.every().hour.do(fetchHospitals)
# schedule.every(5).seconds.do(fetchHospitals)  # for testing only

while True:
    schedule.run_pending()
    time.sleep(1)
