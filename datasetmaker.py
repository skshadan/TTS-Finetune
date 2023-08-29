import os
import glob
import subprocess
import pandas as pd
from pathlib import Path
from textblob import TextBlob
import whisper  # Assuming you have this library imported for your specific use-case

def classify_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    subjectivity = analysis.sentiment.subjectivity
    
    if polarity > 0.2:
        return "[Happy] " + text
    elif polarity < -0.2:
        return "[Sad] " + text
    elif polarity < -0.1 and subjectivity <= 0.5:
        return "[Angry] " + text
    elif polarity < 0.1 and polarity > -0.1 and subjectivity > 0.5:
        return "[Confused] " + text
    elif polarity > 0.1 and subjectivity < 0.5:
        return "[Surprised] " + text
    else:
        return "[Neutral] " + text

# Specify the path to the directory containing audio files
upload_dir = 'E:\\MyWorks\\DatasetMaker\\dataset'

# Create the 'out' directory if it doesn't exist
output_dir = os.path.join(upload_dir, 'out')
os.makedirs(output_dir, exist_ok=True)

# Convert audio files to WAV format
audio_files = glob.glob(os.path.join(upload_dir, '*.mp3')) + glob.glob(os.path.join(upload_dir, '*.wav'))
for audio_file in audio_files:
    output_filename = os.path.splitext(os.path.basename(audio_file))[0] + '.wav'
    output_path = os.path.join(output_dir, output_filename)
    subprocess.run(['ffmpeg', '-i', audio_file, '-acodec', 'pcm_s16le', '-ar', '22050', '-ac', '1', output_path])

# Create the 'splits' directory if it doesn't exist
splits_dir = os.path.join(output_dir, 'splits')
os.makedirs(splits_dir, exist_ok=True)

# Split audio files using SoX
wav_files = glob.glob(os.path.join(output_dir, '*.wav'))
for wav_file in wav_files:
    subprocess.run(['sox', wav_file, os.path.join(splits_dir, os.path.basename(wav_file)), 'silence', '1', '0.5', '0.1%', '1', '0.5', '0.1%', ':', 'newfile', ':', 'restart'])

# Remove small audio files (less than 15KB)
small_files = glob.glob(os.path.join(splits_dir, '*.wav'))
for small_file in small_files:
    if os.path.getsize(small_file) < 15000:
        os.remove(small_file)

# Load the Whisper model
model = whisper.load_model("medium.en")

# Initialize lists to store filenames and transcript text
all_filenames = []
transcript_text = []

# Open the metadata.csv file for writing
metadata_path = 'E:\\MyWorks\\DatasetMaker\\metadata.csv'
with open(metadata_path, 'w', encoding='utf-8') as outfile:
    for filepath in glob.glob(os.path.join(splits_dir, '*.wav')):
        base = os.path.basename(filepath)
        all_filenames.append(base)
        result = model.transcribe(filepath)
        output = result["text"].lstrip()
        output = output.replace("\n", "")
        output_with_sentiment = classify_sentiment(output)
        
        outfile.write(base + '|' + output_with_sentiment + '|' + output_with_sentiment + '\n')
        print(base + '|' + output_with_sentiment + '|' + output_with_sentiment + '\n')

print("Audio splitting and transcription completed.")
