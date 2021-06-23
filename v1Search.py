import json
import os
import urllib3

validSourceTypes = ["endpointActivityData", "messageActivityData", "detections", "networkActivityData"]
validQueryFields = ["hostname" "macaddr" "ip"]

def searchEndpoint(http, baseUrl, httpHeaders, computerId=""):

    body = {
        "computerId": str(computerId)
    }

    r = http.request('POST', baseUrl + "/xdr/eiqs/query/endpointInfo", headers=httpHeaders, body=json.dumps(body))

    return json.loads(r.data)

def searchMultipleEndpoints(http, baseUrl, httpHeaders, computerIds=[]):

    body = {
        "computerIds": computerIds
    }

    r = http.request('POST', baseUrl + "/xdr/eiqs/query/batch/endpointInfo", headers=httpHeaders, body=json.dumps(body))

    return json.loads(r.data)

def queryAgentInfo(http, baseUrl, httpHeaders, field="hostname", value=""):

    body = {
        "criteria": {
            "field": str(field),
            "value": str(value)
        }
    }

    r = http.request('POST', baseUrl + "/xdr/eiqs/query/agentInfo", headers=httpHeaders, body=json.dumps(body))

    return json.loads(r.data)

def searchData(http, baseUrl, httpHeaders, sourceType):

    body = {
        "from": 1620091758,
        "to": 1622755762,
        "source": sourceType,
        "query": "fileName:mimilove.exe"
    }

    r = http.request('POST', baseUrl + "/xdr/search/data", headers=httpHeaders, body=json.dumps(body))

    return json.loads(r.data)

def main(event, context):

    v1ApiEndpoint = str(os.environ.get("v1ApiEndpoint")) + str(os.environ.get("v1ApiVersion"))
    v1ApiAuthToken = str(os.environ.get("v1ApiAuthToken"))

    http = urllib3.PoolManager()

    headers = {
        "Content-Type": "application/json;charset=utf-8",
        "Authorization": "Bearer " + v1ApiAuthToken
    }

    # print("searchEndpoint - " + str(searchEndpoint(http, v1ApiEndpoint, headers, "D1C31A8E-8944-4317-9E62-9E8FE5EAAA52")))
    # print("searchMultipleEndpoints - " + str(searchMultipleEndpoints(http, v1ApiEndpoint, headers, ["D1C31A8E-8944-4317-9E62-9E8FE5EAAA52"])))
    # print("queryAgentInfo - " + str(queryAgentInfo(http, v1ApiEndpoint, headers, "hostname", "UbuntuXDR")))
    # print("searchData - " + str(searchData(http, v1ApiEndpoint, headers)))

    return {"statusCode": 200}