import asyncio
import edge_tts
import os

VOICE = "hi-IN-SwaraNeural"

async def speak(text):
    output_file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "assistant_voice.mp3"
    )

    communicate = edge_tts.Communicate(
        text,
        VOICE,
        rate="+15%",
        volume="+0%"
    )

    await communicate.save(output_file)
    os.startfile(output_file)


asyncio.run(
    speak(
        "नमस्ते सौरव मैं तुम्हारी AI असिस्टेंट हूँ। "
        "अब मैं तुमसे साफ और अच्छी हिंदी में बात कर रही हूँ।"
    )
)