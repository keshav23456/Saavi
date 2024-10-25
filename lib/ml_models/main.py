
import subprocess
import pandas as pd

# Load threatening words from a CSV file
def load_threatening_words(csv_file):
    df = pd.read_csv(csv_file, header=None)  # Assuming no header
    # Convert all entries to string and drop any NaN values
    return df[0].dropna().astype(str).tolist()  # Flatten the DataFrame to a list of words/phrases

# Check if there are any threatening words in the transcribed text
def check_threatening_words(transcribed_text, threatening_words):
    detected_threats = []
    # Make the transcribed text lowercase for case-insensitive comparison
    transcribed_text_lower = transcribed_text.lower()
    
    for word in threatening_words:
        if word.lower() in transcribed_text_lower:  # Case insensitive check
            detected_threats.append(word)
    
    if detected_threats:
        print(f"Threats detected: {', '.join(detected_threats)} found in the audio.")
        return True
    else:
        print("No threats detected in the audio.")
        return False

# Check if the transcribed text is in any of the columns of the CSV file
def check_text_in_csv(text, csv_file):
    df = pd.read_csv(csv_file)
    # Check if the transcribed text is in any of the columns
    for column in df.columns:
        if df[column].astype(str).str.contains(text, case=False).any():
            return True
    return False

# Run the sound recording script
subprocess.run(['python', 'sound record.py'])

'''# Run the transcription script and capture the output
result = subprocess.run(['python', 'transcript.py'], capture_output=True, text=True)
transcribed_text = result.stdout.strip()  # Get the transcribed text and remove any extra whitespace
'''

# Step 2: Run the transcription script and capture the output
result = subprocess.run(['python', r'C:\Users\hp\OneDrive\Desktop\bytes\savi\transcript.py'], capture_output=True, text=True)
transcribed_text = str(result.stdout).strip()   # Get the transcribed text and remove any extra whitespace

# Ensure transcribed_text is a string
if isinstance(transcribed_text, float):
    transcribed_text = str(transcribed_text)
elif not isinstance(transcribed_text, str):
    transcribed_text = ""  # Assign an empty string if it's not a valid type

# Convert to lowercase for further processing
transcribed_text = transcribed_text.lower()
print(transcribed_text)

# Check if the transcribed text is valid
if not transcribed_text:  # Check for empty string
    print("Transcribed text is empty.")
else:
    print(f"Transcribed Text: {transcribed_text}")

    # Load threatening words from CSV
    csv_file = 'all_data2.csv'
    threatening_words = load_threatening_words(csv_file)

    # Check for threatening words
    is_threatening = check_threatening_words(transcribed_text, threatening_words)
'''
    # Optionally, check if the transcribed text is present in the CSV
    if check_text_in_csv(transcribed_text, csv_file):
        print("The transcribed text was found in the CSV file.")
    else:
        print("The transcribed text was not found in the CSV file.")
'''