from flask import Flask, render_template, request

app = Flask(__name__)

# Define the function before using it
def extract_text_after_sentence(input_string, separator_sentence):
    sentences = input_string.split(separator_sentence)
    if len(sentences) > 1:
        extracted_text = sentences[1].strip()
        return extracted_text
    return ""

@app.route('/')
def index():
    return render_template('uploads.html')

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['file']
    if uploaded_file:
        # Save the uploaded file temporarily as a WAV file
        temp_wav_path = 'temp.wav'
        uploaded_file.save(temp_wav_path)

        # Perform speech recognition
        import speech_recognition as sr
        recognizer = sr.Recognizer()

        with sr.AudioFile(temp_wav_path) as source:
            print("Processing audio...")
            audio_data = recognizer.record(source)  # Record the audio file

            # Recognize the audio using Google Web Speech API
            text = recognizer.recognize_google(audio_data)
            print("Transcribed text: ", text)

            # Define the particular sentence you want to use as a separator
            separator_sentence = "medications"

            # Extract and return the text
            extracted_text = extract_text_after_sentence(text, separator_sentence)

            # Render a template to display the extracted text
            return render_template('result.html', extracted_text=extracted_text)

    return "File not uploaded."

if __name__ == '__main__':
    app.run(debug=True)
