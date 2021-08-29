#simple script to make http post requests




# importing the requests library
import requests
import json




import urllib3
import certifi

if __name__ == '__main__':
    # defining the api-endpoint
    API_ENDPOINT = "http://localhost:8081"


    # sending post request and saving response as response object


    r = requests.post(url=API_ENDPOINT, params={
        'resource': 'aws_s3_bucket',
        'category': 'Storage',
        'creation_date': '1628406616705',

        #details
            #'severity': 'low',
            #'status': 'error',
            #'tags':json.dumps([{"name": 'application_bucket'}, {"size": '10GB'}, {"region": 'us_west_2'}])
        })

    # extracting response text
    pastebin_url = r.text
    print("The pastebin URL is:%s" % pastebin_url)

