# contact-info-sweeper
Project to take comma separated values of phone numbers 
and email addresses as input and detect/print invalidities.

The primary script is sweeper.py

Input is assumed to be in the format of a text file containing
comma separated values. Acceptable values are phone numbers
and email addresses.

A valid phone number is in the format
XXX-XXX-XXXX where each X is an arbitrary number between
0 and 9 inclusive. 

A valid email address is in the format
emailaddress123@example.com with any finite amount of letters
and numbers, an "@", another finite amount of letters and
numbers, a ".", and a final sequence of finite letters and
numbers.

White space before, in the middle of, or after phone numbers
or email addresses is ignored, as well as new lines.
