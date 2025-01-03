#!/bin/bash
ps -Ac -o pid,ppid,comm,args | awk "{ if (match(\$3, /bash/) && \$1 != "$$") print \$0 }" | grep -F "$(basename "$0")" > /dev/null && {
  echo "Script is already running";
  exit 1;
}

echo "script running..."
sleep 60
echo "script done"
exit

echo '
DESCRIPTION:
  This script checks if another instance of the same script is already running.
  If it is, the script will exit with an error message.
  Otherwise, the script will continue to run.

HOW IT WORKS:
  This script lists all running processes - outputting the process ID, parent process ID, command, and arguments.
  It then filters out the ones that are bash scripts and checks if the process ID is different from the current script''s process ID.
  If the script name is found in the list of running processes, the script will exit with an error message.

FURTHER UNDERSTANDING:
  • The script uses the ps command to list all running processes.
    • The -A option selects all processes, including those of other users.
    • The -o option specifies the output format.
  • The awk command filters out the processes that are bash scripts and have a different process ID.
  • The grep command checks if the script name is found in the list of running processes.
  • The > /dev/null discards the output of the pidof command.

NOTES:
-A                 Select all processes - including those of other users
-c                 Change the "command" column output to just contain the executable name
                   pid: process ID
                   ppid: parent process ID
                   comm: command
                   args: command and arguments
-o                 Specify the output format
$$                 Expands to the process ID of the shell.
$BASHPID           Expands to the process ID of the current Bash process
\$                 Scapes the dollar sign in the awk command between double quotes
"$(basename "$0")" Extracts the script name from its full path
> /dev/null        Discards the output of pidof

REFERENCE:
• Linux: Make your scripts safe, don''t run a script if an instance of the script is already run
  - https://lovethepenguin.com/linux-make-your-scripts-safe-dont-run-a-script-if-an-instance-of-the-script-is-already-run-54d6c0817f87
'
