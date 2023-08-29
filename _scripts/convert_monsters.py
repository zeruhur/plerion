import pandas as pd
import io
import re

# Read input table data from a markdown file
input_file_path = 'input_table.md'
with open(input_file_path, 'r') as file:
    table_data = file.read()

# Find the start and end of the table
table_start = table_data.find('|')
table_end = table_data.rfind('|')

# Extract the table portion from the markdown data
table_content = table_data[table_start:table_end + 1]

# Convert the table to a pandas DataFrame
df = pd.read_csv(io.StringIO(table_content), sep='|', skipinitialspace=True)

# Remove formatting from column names
df.columns = [re.sub(r'\*+', '', col).strip() for col in df.columns]

# Initialize a list to store transformed records
transfixed_records = []

# Process each row in the DataFrame
for index, row in df.iterrows():
    record = {
        'Nome': row['Nome'],
        'Armatura': row['Armatura'],
        'Dadi Vita': row['Dadi Vita'],
        'Descrizione': row['Descrizione']
    }
    # Transform record and add to the list
    transformed_record = f"### {record['Nome']}\nArmatura: {record['Armatura']}\nDadi Vita: {record['Dadi Vita']}\nDescrizione: {record['Descrizione']}"
    transfixed_records.append(transformed_record)

# Write the transformed records to an output file
output_file_path = 'output_entries.md'
with open(output_file_path, 'w') as file:
    for record in transfixed_records:
        file.write(record)
        file.write('\n\n')
