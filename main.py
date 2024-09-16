from __future__ import print_function
import os
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()
swagger_client.configuration.access_token = os.getenv('STRAVA_ACCESS_TOKEN')

api_instance = swagger_client.AthletesApi()

try: 
    api_response = api_instance.getLoggedInAthlete()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AthletesApi->getLoggedInAthlete: %s\n" % e)
