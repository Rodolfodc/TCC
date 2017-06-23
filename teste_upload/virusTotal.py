# from .models import Document
import requests
import json

def send_to_virusTotal(file_to_send, entire_json = False):
    params = {'apikey': 'e02d488ac39ca6fa86ac70d6dd5deedbdbd7f009a7140588f5f3a7dcbb4f8ed2'}
    files = {'file': (file_to_send, open(file_to_send, 'rb'))}
    response = requests.post('https://www.virustotal.com/vtapi/v2/file/scan', files=files, params=params)
    json_response = response.json()
    if entire_json:
        return json_response
    resource_code =json_response['resource']
    return resource_code
    

def get_json_from_virusTotal(resource_code):
    params = {'apikey': 'e02d488ac39ca6fa86ac70d6dd5deedbdbd7f009a7140588f5f3a7dcbb4f8ed2',
     'resource': resource_code}
    headers = {
        "Accept-Encoding": "gzip, deflate",
        "User-Agent" : "gzip,  r_dc"
    }
    response = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params, headers=headers)
    json_response = response.json()
    return json_response


def get_from_virusTotal(resource_code, antivirus='gdata'):
    json_resp = get_json_from_virusTotal(self.resource_code)
    return json_resp[antivirus]


def check_virusTotal_report(file_to_send):
    return get_json_from_virusTotal(send_to_virusTotal(file_to_send))
