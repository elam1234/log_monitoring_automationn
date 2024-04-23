Automating Log Monitoring and Analysis Using Python

Introduction
Hello, I am Elamparithi M, a DevOps Engineer. I have developed a Python script to automate log monitoring and analysis as part of a DevOps intern assessment. 
In this document, I will explain the purpose, functionality, and implementation details of the script. 

Project Explanation
The goal of this project is to automate the monitoring and analysis of application log files using Python. The script contains two primary functionalities:
log monitoring and log analysis.

Importing Modules

The script imports the following modules:

time: For time-related functions.
re: For regular expressions.
logging: For debugging and logging purposes.
os: For interaction with the operating system.
Log Monitoring Function

The log_monitor function continuously monitors a log file for new entries. Here's an overview of its implementation:

Open the log file programmatically using Python's with open statement.
Continuously monitor new entries in the log file using an infinite loop (while True).
If a new log entry is detected, send it to the log_analysis function for further analysis.
Pause execution to prevent unnecessary CPU usage using the time.sleep(0.1) function.
Implement error handling using a try-except block to handle interruptions and execution errors gracefully.
Log Analysis Function

The log_analysis function analyzes log entries for errors and status codes. Here's a summary of its functionality:

Check for the presence of error messages in log lines and count the occurrences.
Log error messages and counts using the logging.error function.
Extract status codes from log lines using regular expressions.
Log status codes using the logging.info function.
Send analyzed log entries to the get_report function.

Get Report Function
The get_report function generates a report based on analyzed log entries. It logs error occurrences and status codes.

Conclusion
This document provides an overview of the automated log monitoring and analysis script developed using Python. By automating these processes, 
we can continuously monitor our application logs and detect errors and bugs earlier to efficiently improve the application performance.
