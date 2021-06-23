import boto3

validAttacks = ["T15470061", "T11360015", "T10870012"]

def InstallPowerShell(ssmClient):

    installPowerShellResponse = ssmClient.send_command(
        Targets=[
            {
                'Key': 'Product',
                'Values': [
                    'TechDay2021-2',
                ]
            },
        ],
        DocumentName='InstallPowerShell',
        DocumentVersion='$LATEST',
        TimeoutSeconds=600,
        Comment='Run Command - Install PowerShell',        
        MaxConcurrency='100%',
        MaxErrors='0'        
    )

    print(str(installPowerShellResponse))

def InstallAtomicsFolder(ssmClient):

    installAtomicsFolderResponse = ssmClient.send_command(
        Targets=[
            {
                'Key': 'Product',
                'Values': [
                    'TechDay2021-2',
                ]
            },
        ],
        DocumentName='InstallAtomicsFolder',
        DocumentVersion='$LATEST',
        TimeoutSeconds=600,
        Comment='Run Command - Install Atomics Folder',        
        MaxConcurrency='100%',
        MaxErrors='0'        
    )

    print(str(installAtomicsFolderResponse))

def InstallInvokeAtomicRedTeam(ssmClient):

    installInvokeAtomicsRedTeamResponse = ssmClient.send_command(
        Targets=[
            {
                'Key': 'Product',
                'Values': [
                    'TechDay2021-2',
                ]
            },
        ],
        DocumentName='InstallInvokeAtomicRedTeam',
        DocumentVersion='$LATEST',
        TimeoutSeconds=600,
        Comment='Run Command - Install Invoke-AtomicRedTeam',        
        MaxConcurrency='100%',
        MaxErrors='0'        
    )

    print(str(installInvokeAtomicsRedTeamResponse))

def runAttacks(ssmClient, attackId):

    runAttacksResponse = ssmClient.send_command(
        Targets=[
            {
                'Key': 'Product',
                'Values': [
                    'TechDay2021-2',
                ]
            },
        ],
        DocumentName=attackId,
        DocumentVersion='$LATEST',
        TimeoutSeconds=600,
        Comment='Run Command - Attack',        
        MaxConcurrency='100%',
        MaxErrors='0'        
    )

    print(str(runAttacksResponse))

def main(event, context):

    ssmClient = boto3.client('ssm')    
    
    print("InstallPowerShell - " + str(InstallPowerShell(ssmClient)))
    print("InstallAtomicsFolder - " + str(InstallAtomicsFolder(ssmClient)))
    print("InstallInvokeAtomicRedTeam - " + str(InstallInvokeAtomicRedTeam(ssmClient)))
    print("runAttacks - " + str(runAttacks(ssmClient, str(event["attackId"]))))
    # print("runAttacks - " + str(runAttacks(ssmClient, "T15470061")))
    # print("runAttacks - " + str(runAttacks(ssmClient, "T11360015")))
    # print("runAttacks - " + str(runAttacks(ssmClient, "T10870012")))

    return { "statusCode": 200 }