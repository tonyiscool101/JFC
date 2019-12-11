# Laing O'Rourke ENGG4064 Project

Web Application for social network analysis. 

Python Flask is required and a flask server can be made by running flask_server.py and then accessed at 127.0.0.1:5000/ in your browser.

The application is then used by making searches, the searches must be character correct.

  - Local/Global: Input needs to be from 'Sender' or 'Recipient' (eg. 61517f1dee116589b36c742cba2e32b5)
  - Department: Input needs to be from 'SendersDepartment' or 'RecipientsDepartment' (eg. Meeting Room)
  - City: Input needs to be from 'SendersCity' or 'RecipientsCity' (eg. Austrak)
  - Office: Input needs to be from 'SendersOffice' or 'RecipientsOffice' (eg. North Sydney - Mount Street)
  
Input file is SNA_Data.xlsx and can be replaced providing that the filename and column headings remain the same.

Search time is the greatest problem with the application and some searches that involve a large number of offices or cities take a large time to perform the analysis.
