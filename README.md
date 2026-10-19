# Python Log Analyzer

## Objective

This project analyses authentication logs and identifies suspicious login activity.

## Tools Used

-Python 3 - log parsing and detection logic
-Regular expressions - extracting timestamps, usernames and source IPs from auth.log

## How It Works
The script parses Linux auth.log entries, extracts failed authentication attempts, and groups them by source IP. Any IP exceeding the configured attempt threshold is flagged as suspicious, with its attempt count reported.

## Sample Findings

Failed Logins: 4

Suspicious IPs:

- 192.168.1.5 (3 attempts)
- 10.10.10.2 (1 attempt)

## Skills Demonstrated

-Authentication log parsing and analysis
-Failed-login and brute-force pattern detection
-Security automation in Python
