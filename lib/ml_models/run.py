'''
pip install assemblyai
'''
import assemblyai as aai

aai.settings.api_key = "548744b347e64e339ed76c94e035da50"
transcriber = aai.Transcriber()

#transcript = transcriber.transcribe("https://assembly.ai/news.mp4")
transcript = transcriber.transcribe("output_audio.wav")

print(transcript.text)