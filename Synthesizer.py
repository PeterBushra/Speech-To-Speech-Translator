from audioplayer import AudioPlayer
from gtts import gTTS
# Playback stops when the object is destroyed (GC'ed), so save a reference to the object for non-blocking playback.


def synthesize(text,language):
    try:
        tts = gTTS(text=text ,lang=language)
        tts.save("synthesized.mp3")
        AudioPlayer("./synthesized.mp3").play(block=True)
    except Exception as E:
        return "No Speech!"