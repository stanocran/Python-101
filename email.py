import os
import docx2txt
import re
import pandas as pd

# Replace with the name of your Word file
document_name = 'Customer Base.docx'

# Get the path to the user's downloads directory
downloads_dir = os.path.expanduser('~/Downloads')

# Construct the full path to your Word document
document_path = os.path.join(downloads_dir, document_name)

# Read the Word document
document_text = docx2txt.process(document_path)

# Use regular expression to find email addresses enclosed in "<>"
email_pattern = re.compile(r'<([^<>@]+@[^<>@]+\.[^<>@]+)>')
emails = email_pattern.findall(document_text)

# Create a DataFrame from the list of email addresses
df = pd.DataFrame(emails, columns=['Email'])

# Construct the full path to the output Excel file in the downloads directory
output_file_path = os.path.join(downloads_dir, 'output_file.xlsx')

# Write the DataFrame to an Excel file
df.to_excel(output_file_path, index=False)

print('Data written to Excel file:', output_file_path)