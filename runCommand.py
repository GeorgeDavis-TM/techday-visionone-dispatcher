import os
import boto3

validAttacks = ["T15470061", "T11360015", "T10870012"]

# def InstallPowerShell(ssmClient):

#     installPowerShellResponse = ssmClient.send_command(
#         Targets=[
#             {
#                 'Key': 'tag:Product',
#                 'Values': [
#                     'TechDay2021-2',
#                 ]
#             },
#         ],
#         DocumentName='InstallPowerShell',
#         DocumentVersion='$LATEST',
#         TimeoutSeconds=600,
#         Comment='Run Command - Install PowerShell',        
#         MaxConcurrency='100%',
#         MaxErrors='0'        
#     )

#     return installPowerShellResponse

# def InstallAtomicsFolder(ssmClient):

#     installAtomicsFolderResponse = ssmClient.send_command(
#         Targets=[
#             {
#                 'Key': 'tag:Product',
#                 'Values': [
#                     'TechDay2021-2',
#                 ]
#             },
#         ],
#         DocumentName='InstallAtomicsFolder',
#         DocumentVersion='$LATEST',
#         TimeoutSeconds=600,
#         Comment='Run Command - Install Atomics Folder',        
#         MaxConcurrency='100%',
#         MaxErrors='0'        
#     )

#     return installAtomicsFolderResponse

# def InstallInvokeAtomicRedTeam(ssmClient):

#     installInvokeAtomicsRedTeamResponse = ssmClient.send_command(
#         Targets=[
#             {
#                 'Key': 'tag:Product',
#                 'Values': [
#                     'TechDay2021-2',
#                 ]
#             },
#         ],
#         DocumentName='InstallInvokeAtomicRedTeam',
#         DocumentVersion='$LATEST',
#         TimeoutSeconds=600,
#         Comment='Run Command - Install Invoke-AtomicRedTeam',        
#         MaxConcurrency='100%',
#         MaxErrors='0'        
#     )

#     return installInvokeAtomicsRedTeamResponse

# def RunWSSensorCheck(ssmClient):

#     runWSSensorCheckResponse = ssmClient.send_command(
#         Targets=[
#             {
#                 'Key': 'tag:Product',
#                 'Values': [
#                     'TechDay2021-2',
#                 ]
#             },
#         ],
#         DocumentName='RunWSSensorCheck',
#         DocumentVersion='$LATEST',
#         TimeoutSeconds=600,
#         Comment='Run Command - sendCommand to DS Agent',        
#         MaxConcurrency='100%',
#         MaxErrors='0'        
#     )

#     return runWSSensorCheckResponse

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

    if actionId:
    
        ssmClient = boto3.client('ssm')    
        
        # print("InstallPowerShell - " + str(InstallPowerShell(ssmClient)))
        # print("InstallAtomicsFolder - " + str(InstallAtomicsFolder(ssmClient)))
        # print("InstallInvokeAtomicRedTeam - " + str(InstallInvokeAtomicRedTeam(ssmClient)))
        print("Sent Command. Received response - " + str(runAttacks(ssmClient, actionId)))

        return { "statusCode": 200 }

    return { "statusCode": 400 }