import schedule
import time
from apicall import fetchHospitals

# Fetch data every hour
schedule.every().hour.do(fetchHospitals)

while True:
    schedule.run_pending()
    time.sleep(1)
