import json
import os
import urllib3

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

def main(event, context):

    v1ApiEndpoint = str(os.environ.get("v1ApiEndpoint")) + str(os.environ.get("v1ApiVersion"))
    v1ApiAuthToken = str(os.environ.get("v1ApiAuthToken"))

    http = urllib3.PoolManager()

    headers = {
        "Content-Type": "application/json;charset=utf-8",
        "Authorization": "Bearer " + v1ApiAuthToken
    }

    print("testEmailNotification - " + str(testEmailNotification(http, v1ApiEndpoint, headers, "george_davis@trendmicro.com")))
    print("listNotificationWebhooks - " + str(listNotificationWebhooks(http, v1ApiEndpoint, headers)))
    print("getApiAuthConfig - " + str(getApiAuthConfig(http, v1ApiEndpoint, headers)))

    return getApiAuthConfig(http, v1ApiEndpoint, headers)