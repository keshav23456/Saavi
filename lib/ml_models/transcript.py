# Start by making sure the `assemblyai` package is installed.
# If not, you can install it by running the following command:
# pip install -U assemblyai
#
# Note: Some macOS users may need to use `pip3` instead of `pip`.

import assemblyai as aai

# Replace with your API key
aai.settings.api_key = "548744b347e64e339ed76c94e035da50"

# URL of the file to transcribe
# FILE_URL = "C:\Users\hp\OneDrive\Desktop\bytes\savi\sound record.py"

# You can also transcribe a local file by passing in a file path
FILE_URL = 'output_audio.wav'

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(FILE_URL)

if transcript.status == aai.TranscriptStatus.error:
    print(transcript.error)
else:
    print(transcript.text)
