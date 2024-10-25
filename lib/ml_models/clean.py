import csv

# Define the input and output file names
input_file = 'all_data1.csv'  # Replace with your input CSV file name
output_file = 'all_data2.csv'  # Output file for cleaned data

# Function to clean CSV
def clean_csv(input_file, output_file):
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            # Remove extra commas and empty fields
            cleaned_row = [field.strip() for field in row if field.strip()]

            # Only write non-empty rows
            if cleaned_row:
                writer.writerow(cleaned_row)

# Run the cleaning function
clean_csv(input_file, output_file)

print(f'Cleaned CSV has been saved to {output_file}.')
