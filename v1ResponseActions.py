import json
import os
import urllib3
import time

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

def getResponseTaskDetails(http, baseUrl, httpHeaders, actionId=0):

    result = {}
    taskStatus = "pending"

    while (taskStatus == "pending"):

        r = http.request('GET', baseUrl + "/xdr/response/getTask?actionId=" + actionId, headers=httpHeaders)

        taskStatus = json.loads(r.data)["data"]["taskStatus"]

        print(str(taskStatus) + "...")

        if taskStatus != "pending":
            result = json.loads(r.data)
        else:
            time.sleep(5)

    return result

def getCollectedFileInfo(http, baseUrl, httpHeaders, actionId=0):

    r = http.request('POST', baseUrl + "/xdr/response/downloadInfo?actionId=" + actionId, headers=httpHeaders)

    return json.loads(r.data)

def main(event, context):

    v1ApiEndpoint = str(os.environ.get("v1ApiEndpoint")) + str(os.environ.get("v1ApiVersion"))
    v1ApiAuthToken = str(os.environ.get("v1ApiAuthToken"))

    http = urllib3.PoolManager()

    headers = {
        "Content-Type": "application/json;charset=utf-8",
        "Authorization": "Bearer " + v1ApiAuthToken
    }

    # print("isolateEndpoint - " + str(isolateEndpoint(http, v1ApiEndpoint, headers)))
    # print("restoreIsolatedEndpoint - " + str(restoreIsolatedEndpoint(http, v1ApiEndpoint, headers)))
    # print("terminateProcess - " + str(terminateProcess(http, v1ApiEndpoint, headers)))
    # print("collectFile - " + str(collectFile(http, v1ApiEndpoint, headers)))
    # print("getCollectedFileInfo - " + str(getCollectedFileInfo(http, v1ApiEndpoint, headers)))
    # print("getResponseTaskDetails - " + str(getResponseTaskDetails(http, v1ApiEndpoint, headers, "00000293")))
    # print("getResponseTaskDetails - " + str(getResponseTaskDetails(http, v1ApiEndpoint, headers, "00000297")))

    return {"statusCode": 200}
