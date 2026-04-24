# This script will format a textfile conataining a list of phone numbers to +1XXXXXXXXXX and return the formatted list in a variable.
# It will also print out any phone numbers that could not be formatted due to not containing 10 digits.
# It will reserve blank lines and lines that do not contain 10 digits.

import re

def format_phone_numbers(file_path):
    formatted_numbers = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:  # Preserve blank lines
                formatted_numbers.append('')
                continue
            
            # Remove all non-digit characters
            digits = re.sub(r'\D', '', line)
            
            if len(digits) == 10:
                formatted_number = f"+1{digits}"
                formatted_numbers.append(formatted_number)
            else:
                print(f"Could not format: {line} (does not contain 10 digits)")
                formatted_numbers.append(line)  # Preserve unformatted lines

    return formatted_numbers