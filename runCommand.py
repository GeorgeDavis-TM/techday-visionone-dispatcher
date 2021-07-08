import os
import boto3

validAttacks = ["T15470061", "T11360015", "T10870012"]

def runAttacks(ssmClient, actionId):

    runAttacksResponse = ssmClient.send_command(
        Targets=[
            {
                'Key': 'tag:Product',
                'Values': [
                    'TechDay2021-2',
                ]
            },
        ],
        DocumentName=actionId,
        DocumentVersion='$LATEST',
        TimeoutSeconds=600,
        Comment='Run Command - Attack',        
        MaxConcurrency='100%',
        MaxErrors='0'        
    )

    return runAttacksResponse

def main(event, context):

    actionId = str(os.environ.get("ACTION_ID")) if 'ACTION_ID' in os.environ else None
    regionName = str(os.environ.get("REGION_NAME")) if 'REGION_NAME' in os.environ else None

    if actionId and regionName:
    
        ssmClient = boto3.client('ssm', region_name=regionName)  
        
        print("Sent Command. Received response - " + str(runAttacks(ssmClient, actionId)))

        return { "statusCode": 200 }

    return { "statusCode": 400 }