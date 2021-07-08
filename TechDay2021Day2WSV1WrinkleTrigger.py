import cfnresponse
import boto3
import os

def main(event, context):

    regionName = str(os.environ.get("REGION_NAME")) if 'REGION_NAME' in os.environ else None
    functionsList = str(os.environ.get("FUNCTIONS_LIST")).split(",") if 'FUNCTIONS_LIST' in os.environ else None

    if regionName and functionsList:

        lambdaClient = boto3.client('lambda', region_name=regionName)
        lambdaBundledResponse = {}

        for functionName in functionsList:

            print("Triggered - " + str(functionName))

            lambdaFunctionInvokeResponse = lambdaClient.invoke(
                FunctionName=functionName,
                InvocationType='RequestResponse',
                LogType='Tail'
            )

            tempDict = { lambdaFunctionInvokeResponse["ResponseMetadata"]["RequestId"]: lambdaFunctionInvokeResponse["StatusCode"] }        
            lambdaBundledResponse.update(tempDict)        

        responseObj = { "Output": str(lambdaBundledResponse) }
        
        cfnresponse.send(event, context, cfnresponse.SUCCESS, responseObj)

    responseObj = { "Output": "Environment variables are set or parsed incorrectly." }
    
    cfnresponse.send(event, context, cfnresponse.FAILED, responseObj)