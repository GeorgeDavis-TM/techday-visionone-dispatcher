import os
import boto3
import time

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

    print(str(runAttacksResponse))

    return runAttacksResponse

def main(event, context):

    actionId = str(os.environ.get("ACTION_ID")) if 'ACTION_ID' in os.environ else None
    regionName = str(os.environ.get("REGION_NAME")) if 'REGION_NAME' in os.environ else None
    instanceId = str(os.environ.get("INSTANCE_ID")) if 'INSTANCE_ID' in os.environ else None
    sleepTimer = int(os.environ.get("SLEEP_TIMER")) if 'SLEEP_TIMER' in os.environ else 5

    if actionId and regionName:
    
        ssmClient = boto3.client('ssm', region_name=regionName)  

        runCommandResponse = runAttacks(ssmClient, actionId)
        print("Sent Command. Received response - " + str(runCommandResponse))

        commandId = runCommandResponse['Command']['CommandId']

        time.sleep(sleepTimer)
        
        waiter = ssmClient.get_waiter('command_executed')

        waiter.wait(
            CommandId=commandId,
            InstanceId=instanceId,
            WaiterConfig={
                'Delay': 5,
                'MaxAttempts': 60
            }
        )    

        getCommandInvocationResponse = ssmClient.get_command_invocation(
            CommandId=commandId,
            InstanceId=instanceId
        )
        
        print(str(getCommandInvocationResponse))

        if getCommandInvocationResponse["Status"] == "Success":
            print("Success: " + getCommandInvocationResponse["StandardOutputContent"] + " - " + getCommandInvocationResponse["StandardOutputUrl"])
            return(True)
        else:
            raise Exception("Error: " + getCommandInvocationResponse["StandardErrorContent"] + " - " + getCommandInvocationResponse["StandardErrorUrl"])
            return(False)