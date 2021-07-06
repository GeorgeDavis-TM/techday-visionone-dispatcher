import cfnresponse
import boto3
import os

functionsList = [ "techday-visionone-dispatcher-prod-T11360015", "techday-visionone-dispatcher-prod-T15470061", "techday-visionone-dispatcher-prod-T10870012", "techday-visionone-dispatcher-prod-RunTestCommand" ]

def main(event, context):

    regionName = str(os.environ.get("REGION_NAME")) if 'REGION_NAME' in os.environ else None

    lambdaClient = boto3.client('lambda', region_name=regionName)

    lambdaBundledResponse = {}

    for functionName in functionsList:

        print(str(functionName))

        lambdaFunctionInvokeResponse = lambdaClient.invoke(
            FunctionName=functionName,
            InvocationType='RequestResponse',
            LogType='Tail'
        )

        tempDict = { lambdaFunctionInvokeResponse["ResponseMetadata"]["RequestId"]: lambdaFunctionInvokeResponse["StatusCode"] }        
        lambdaBundledResponse.update(tempDict)        

    responseObj = { "Output": str(lambdaBundledResponse) }
    
    cfnresponse.send(event, context, cfnresponse.SUCCESS, responseObj)