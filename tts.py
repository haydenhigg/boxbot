from google.cloud import texttospeech

VOICE = 'Neural2-D'
SLUG_TEXTS = {
    # 'jab': 'jab',
    # 'cross': 'cross',
    # 'left-hook': 'left hook',
    # 'right-hook': 'right hook',
    # 'left-uppercut': 'left uppercut',
    # 'right-uppercut': 'right uppercut',
    'one': 'one',
    'two': 'two',
    'three': 'three',
    'four': 'four',
    'five': 'five',
    'six': 'six'
    # 'slip-left': 'slip left',
    # 'slip-right': 'slip right',
    # 'roll-left': 'roll left',
    # 'roll-right': 'roll right',
    # 'duck': 'duck',
    # 'step-back': 'step back'
}

def synthesize_text(name: str, text: str):
    file_name = f'{VOICE}/{name}.mp3'

    input_text = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code='en-US',
        name=f'en-US-{VOICE}',
        ssml_gender=texttospeech.SsmlVoiceGender.MALE
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        pitch=-11,
        speaking_rate=2.2
    )

    response = texttospeech.TextToSpeechClient().synthesize_speech(
        request={
            'input': input_text,
            'voice': voice,
            'audio_config': audio_config
        }
    )

    with open(file_name, 'wb') as out:
        out.write(response.audio_content)
        print(f'Audio content "{text}" written to file {file_name}')

for slug, text in SLUG_TEXTS.items():
    synthesize_text(slug, text)
