import json
import os
import urllib3

def listSupportedProducts(http, baseUrl, httpHeaders):

    r = http.request('GET', baseUrl + "/xdr/portal/connectors/saas", headers=httpHeaders)

    return json.loads(r.data)

def enableTrendRemoteSupport(http, baseUrl, httpHeaders):

    body = {
        'enabled': True
    }

    r = http.request('PUT', baseUrl + "/xdr/portal/remoteSupport", headers=httpHeaders, body=json.dumps(body))

    return json.loads(r.data)

def getTrendRemoteSupportStatus(http, baseUrl, httpHeaders):

    r = http.request('GET', baseUrl + "/xdr/portal/remoteSupport", headers=httpHeaders)

    return True if json.loads(r.data)["code"] == "Success" else False

def checkWorkloadConnectionStatus(http, baseUrl, httpHeaders):
    
    connectionStatus = listSupportedProducts(http, baseUrl, httpHeaders)
        
    if connectionStatus["code"] == "Success":

        for connection in connectionStatus["data"]:

            if connection["productId"] == "sws":
                return True if connection["connectorStatus"] == 1 else False

def main(event, context):

    v1ApiEndpoint = str(os.environ.get("v1ApiEndpoint")) + str(os.environ.get("v1ApiVersion"))
    v1ApiAuthToken = str(os.environ.get("v1ApiAuthToken"))

    http = urllib3.PoolManager()

    headers = {
        "Content-Type": "application/json;charset=utf-8",
        "Authorization": "Bearer " + v1ApiAuthToken
    }

    print("enableTrendRemoteSupport - " + str(enableTrendRemoteSupport(http, v1ApiEndpoint, headers)))
    print("getTrendRemoteSupportStatus - " + str(getTrendRemoteSupportStatus(http, v1ApiEndpoint, headers)))

    print("checkWorkloadConnectionStatus - " + str(checkWorkloadConnectionStatus(http, v1ApiEndpoint, headers)))

    if (checkWorkloadConnectionStatus(http, v1ApiEndpoint, headers) != True):
        raise Exception("You haven't finished this challenge, because Workload Security Product Connector is not configured for your Vision One instance.")
        return(False)
    return(True)
