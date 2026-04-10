### This code intends to streamline the process of data sanitization and formatting for Salto CSV synchronization jobs ###

convert_to_csv.py:

    - This function takes 2 textfiles, one containing a list of names (first & last), 
      and the other containing the list of phone numbers.

    - Update the '.env.example' variables to the names/filepaths of your target files.
      Rename the file to '.env' ... This is ignored by git and will not sync with your commits.

    - All blank spaces are reserved, so if line 96 of the name file exists and line 96 of the phone file is a blank line, 
      the space is reserved and continues on.

    - If a first or last name contains a space, it is encapsulated within single quotes ( ' ' ), 
      check your text indicator on your salto job to ensure you use single quote, not double-quote.

    - Phone numbers must contain 10 numeric digits each, all non-digits are removed and
      the international code (+1) is appended to the front. This returns the proper format +1XXXXXXXXXX.
      
    - The default format for the output file is: 
    
        [extID],[KeyAudit],[KeyExp.Unit],[KeyExp.Period],[MobileAppType],[LastName],[FirstName],[PhoneNumber],[UserExp]

    - extID will be a unique randomly generated numbers

    - KeyAudit will be '1'. This sets the user profile to collect audit trail

    - KeyExp.Unit will be '0', signifying the unit of period is Days.

    - KeyExp.Period will be '7', setting the user authentication to expire in 7 days.

    - MobileAppType is set to '2' by default, setting the user as a justinMobile credential

    - LastName and FirstName will be taken from the names.txt file specified in .env

    - PhoneNumber will be taken from the phones.txt file specified in .env
      - Blank lines are reserved and will be appended to the corresponding line from the names.txt

    - UserExp should be EMPTY, setting the user expiration to 'never' by default.


phone_format.py:

    - This function is specifically for sanitizing phone numbers into the proper salto format (+1XXXXXXXXXX)

    - The return is simply a list of the formatted phone numbers

    i.e.:

        formatted_numbers = phone_format('phones.txt')