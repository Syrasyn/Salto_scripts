# This script will take 2 files and convert them to a single CSV file.
# The first file will contain a list of names (lastname, firstname) and the second file will contain a list of phone numbers. The script will combine the names and phone numbers into a single CSV file with two columns: "Name" and "Phone Number". It will also print out any lines that could not be formatted due to not containing 10 digits in the phone number file.
# Reserve blank lines and lines that do not contain 10 digits in the phone number file.
# The csv format will be: extID,KeyAudit,KeyExp.Unit,KeyExp.Period,MobileAppType,LastName,FirstName,PhoneNumber,UserExp.
# The extID will be a randomly generated 8 digit number, KeyAudit will be 1, KeyExp.Unit will be 0, KeyExp.Period will be 7, MobileAppType will be 2, UserExp will be a comma.. The LastName and FirstName will be extracted from the names file, and the PhoneNumber will be extracted from the phone numbers file and formatted to +1XXXXXXXXXX. If the phone number cannot be formatted, it will be left as is in the CSV file.


import os
import csv
import random
import re
import dotenv

dotenv.load_dotenv()  # Load environment variables from .env file

def convert_to_csv(names_file, phones_file, output_file):
    with open(names_file, 'r') as names, open(phones_file, 'r') as phones, open(output_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["extID", "KeyAudit", "KeyExp.Unit", "KeyExp.Period", "MobileAppType", "LastName", "FirstName", "PhoneNumber", "UserExp"])
        
        for name_line, phone_line in zip(names, phones):
            name_line = name_line.strip()
            phone_line = phone_line.strip()
            
            if not name_line:  # Preserve blank lines
                continue
            
            # Extract last name and first name
            if ',' in name_line:
                last_name, first_name = [part.strip() for part in name_line.split(',', 1)]
            else:
                print(f"Could not format name: {name_line} (does not contain a comma)")
                last_name, first_name = name_line, ""  # Preserve unformatted names
            
            # if last_name or first_name contains a space, encapsulate in quotes
            if ' ' in last_name:
                last_name = f"'{last_name}'"
            if ' ' in first_name:
                first_name = f"'{first_name}'"

            # Remove all non-digit characters from the phone number
            digits = re.sub(r'\D', '', phone_line)
            
            if len(digits) == 10:
                formatted_phone = f"+1{digits}"
            else:
                print(f"Could not format phone number for {name_line.strip()}: {phone_line} (INVALID PHONE NUMBER)")
                formatted_phone = phone_line  # Preserve unformatted phone numbers
            
            ext_id = random.randint(10000000, 99999999)
            csv_writer.writerow([ext_id, 1, 0, 7, 2, last_name, first_name, formatted_phone, " ", ""])

if __name__ == "__main__":
    names_file = os.getenv("NAMES_FILE")  # Change this to the path of your names file
    phones_file = os.getenv("PHONES_FILE")  # Change this to the path of your phone numbers file
    output_file = "output.csv"  # Change this to the desired output CSV file name
    convert_to_csv(names_file, phones_file, output_file)