# Register the Microsoft RedHat repository
curl https://packages.microsoft.com/config/rhel/7/prod.repo | sudo tee /etc/yum.repos.d/microsoft.repo

# Install PowerShell
sudo yum install -y powershell

# Start PowerShell
pwsh

# Get the Atomic Red Team 
IEX (IWR 'https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/install-atomicredteam.ps1' -UseBasicParsing);
Install-AtomicRedTeam

# Get the Atomics Folder
IEX (IWR 'https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/install-atomicsfolder.ps1' -UseBasicParsing);
Install-AtomicsFolder

# New Shell Import
Import-Module "/AtomicRedTeam/invoke-atomicredteam/Invoke-AtomicRedTeam.psd1" -Force
$PSDefaultParameterValues = @{"Invoke-AtomicTest:PathToAtomicsFolder"="/AtomicRedTeam/atomics"}

# List Atomic Tests
Invoke-AtomicTest All -ShowDetailsBrief

# Check Prerequisites
Invoke-AtomicTest T1003 -CheckPrereqs

# Trigger Atomic Tests and cleanup after
Invoke-AtomicTest T1218.010 -TestNumbers 1,2 -Cleanup

# T1547.006-1 Linux - Load Kernel Module via insmod
Invoke-AtomicTest T1547.006 -TestNumbers 1 -Cleanup

# T1136.001-5 Create a new user in Linux with `root` UID and GID
Invoke-AtomicTest T1136.001 -TestNumbers 5 -Cleanup

# T1087.001-2 View sudoers access
Invoke-AtomicTest T1087.001 -TestNumbers 2 -Cleanup