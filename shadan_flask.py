from flask import Flask, request, send_file
from TTS.api import TTS
import os

app = Flask(__name__)

# Initialize TTS model
tts = TTS(model_name="tts_models/en/jenny/jenny", progress_bar=True, gpu=True)

@app.route('/voice', methods=['POST'])
def synthesize():
    try:
        data = request.json
        text = data.get('text', '')
        emotion = data.get('emotion', '')
        speed = data.get('speed', 1.5)

        output_path = "output.wav"  # Set your desired output file path

        # Generate TTS audio
        tts.tts_to_file(text=text, file_path=output_path, emotion=emotion, speed=speed)

        # Send the generated audio file in the response
        return send_file(output_path, mimetype='audio/wav')

    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
