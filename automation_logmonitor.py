import os
import re
import time
import logging

# configure logging in this script for debugging  a code
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

#log monitoring and send the lines in log to loganalysis function
def log_monitor(logfile):
    logging.info("Starting to monitor the logfile: %s", logfile)  # Fix here
    try:
        with open(logfile, 'r') as f:
            f.seek(0, os.SEEK_END)
            while True:
                line = f.readline().strip()
                if line:
                    log_analysis(line)
                else:
                    time.sleep(0.1)
    except KeyboardInterrupt:
        logging.info("Received Ctrl+C signal. Exiting...")
    except Exception as e:
        logging.error("An error occurred while monitoring the logfile: %s", str(e))
        
# analysis the logs in the file
def log_analysis(line):
    if 'error' in line.lower():
        error_count = line.lower().count('error')
        logging.error("Error occurred in this file: %s", error_count)
        logging.error("Error message: %s", line)
        get_report('error', error_count)
    status_codes = re.findall(r'\b\d{3}\b', line)
    if status_codes:
        for code in status_codes:
            logging.info("Status code: %s found in line: %s", code, line)
            get_report("Status code", code)

def get_report(error_line, status_code):
    if error_line:
        logging.error("Error occurred: %s", error_line)
    if status_code:
        logging.info("Status code: %s", status_code)

def main():
    logfile = input("Enter your log filename: ")
    log_monitor(logfile)

if __name__ == "__main__":
    main()
