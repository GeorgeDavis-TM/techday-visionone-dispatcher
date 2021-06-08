import json
import os
import urllib3

validSourceTypes = ["endpointActivityData", "messageActivityData", "detections", "networkActivityData"]
validQueryFields = ["hostname" "macaddr" "ip"]

def listSupportedProducts(http, baseUrl, httpHeaders):

    r = http.request('GET', baseUrl + "/xdr/portal/connectors/saas", headers=httpHeaders)

    return json.loads(r.data)

def testEmailNotification(http, baseUrl, httpHeaders, testEmailAddress=""):

    body = {}
    body["email"] = str(testEmailAddress)

    r = http.request('POST', str(baseUrl) + "/portal/notifications/alerts/sendEmails", headers=httpHeaders, body=json.dumps(body))

    return json.loads(r.data)

def listNotificationWebhooks(http, baseUrl, httpHeaders):

    r = http.request('GET', baseUrl + "/xdr/portal/notifications/webhooks", headers=httpHeaders)

    return json.loads(r.data)

def getApiAuthConfig(http, baseUrl, httpHeaders):

    r = http.request('GET', baseUrl + "/xdr/portal/siem", headers=httpHeaders)

    return json.loads(r.data)

def isolateEndpoint(http, baseUrl, httpHeaders):

    body = {
        "computerId": "425EA4D8-01C9-7981-08BF-CEBB3AE4F01F",
        "productId": "sao",
        "description": "Isolate Endpoint"
    }

    r = http.request('POST', baseUrl + "/xdr/response/isolate", headers=httpHeaders, body=json.dumps(body))

    return json.loads(r.data)

def restoreIsolatedEndpoint(http, baseUrl, httpHeaders):

    body = {
        "computerId": "425EA4D8-01C9-7981-08BF-CEBB3AE4F01F",
        "productId": "sao",
        "description": "Restore Isolation of Endpoint"
    }

    r = http.request('POST', baseUrl + "/xdr/response/restoreIsolate", headers=httpHeaders, body=json.dumps(body))

    return json.loads(r.data)

def terminateProcess(http, baseUrl, httpHeaders):

    body = {
        "computerId": "425EA4D8-01C9-7981-08BF-CEBB3AE4F01F",
        "fileSha1": "",
        "productId": "sao",
        "description": "Terminate Process request",
        "filename": [
            "mimilove.exe"
        ]
    }

    r = http.request('POST', baseUrl + "/xdr/response/terminateProcess", headers=httpHeaders, body=json.dumps(body))

    return json.loads(r.data)

def collectFile(http, baseUrl, httpHeaders):

    body = {
        "description": "Collect File",
        "productId": "sao",
        "computerId": "D1C31A8E-8944-4317-9E62-9E8FE5EAAA52",
        "filePath": "C:\\Users\\Admin\\Desktop\\Mimi\\Win32\\mimilove.exe",
        "os": "windows"
    }

    r = http.request('POST', baseUrl + "/xdr/response/collectFile", headers=httpHeaders, body=json.dumps(body))

    return json.loads(r.data)

def getCollectedFileInfo(http, baseUrl, httpHeaders, actionId=0):

    r = http.request('POST', baseUrl + "/xdr/response/downloadInfo?actionId=" + actionId, headers=httpHeaders)

    return json.loads(r.data)

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

def enableTrendRemoteSupport(http, baseUrl, httpHeaders):

    body = {
        'enabled': True
    }

    r = http.request('PUT', baseUrl + "/xdr/portal/remoteSupport", headers=httpHeaders, body=json.dumps(body))

    return json.loads(r.data)

def getTrendRemoteSupportStatus(http, baseUrl, httpHeaders):

    r = http.request('GET', baseUrl + "/xdr/portal/remoteSupport", headers=httpHeaders)

    return True if json.loads(r.data)["code"] == "Success" else False

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
    print("listSupportedProducts - " + str(listSupportedProducts(http, v1ApiEndpoint, headers)))
    print("testEmailNotification - " + str(testEmailNotification(http, v1ApiEndpoint, headers, "george_davis@trendmicro.com")))
    print("listNotificationWebhooks - " + str(listNotificationWebhooks(http, v1ApiEndpoint, headers)))
    print("getApiAuthConfig - " + str(getApiAuthConfig(http, v1ApiEndpoint, headers)))
    # print("isolateEndpoint - " + str(isolateEndpoint(http, v1ApiEndpoint, headers)))
    # print("restoreIsolatedEndpoint - " + str(restoreIsolatedEndpoint(http, v1ApiEndpoint, headers)))
    # print("terminateProcess - " + str(terminateProcess(http, v1ApiEndpoint, headers)))
    # print("collectFile - " + str(collectFile(http, v1ApiEndpoint, headers)))
    # print("getCollectedFileInfo - " + str(getCollectedFileInfo(http, v1ApiEndpoint, headers)))
    print("searchEndpoint - " + str(searchEndpoint(http, v1ApiEndpoint, headers, "D1C31A8E-8944-4317-9E62-9E8FE5EAAA52")))
    print("searchMultipleEndpoints - " + str(searchMultipleEndpoints(http, v1ApiEndpoint, headers, ["D1C31A8E-8944-4317-9E62-9E8FE5EAAA52"])))
    print("queryAgentInfo - " + str(queryAgentInfo(http, v1ApiEndpoint, headers, "hostname", "UbuntuXDR")))
    # print("searchData - " + str(searchData(http, v1ApiEndpoint, headers)))

    return {"statusCode": 200}
