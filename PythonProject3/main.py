import os
import cohere
from dotenv import load_dotenv
from RealtimeSTT import AudioToTextRecorder
import os
from dotenv import load_dotenv
from RealtimeTTS import TextToAudioStream, SystemEngine

load_dotenv()

api_key = os.getenv("COHERE_API_KEY")
print("API Key:", api_key)
co = cohere.Client(api_key)


def main():
    print("🎤 Speak now...")

    recorder = AudioToTextRecorder()

    while True:
        text = recorder.text()

        if text:
            print("You:", text)

            if text.lower() == "exit":
                break

            response = co.chat(
                model="command-a-03-2025",
                message=text
            )

            reply = response.text

            print("AI:", reply)

            engine = SystemEngine()
            stream = TextToAudioStream(engine)
            stream.feed(reply)
            stream.play()


if __name__ == "__main__":
    main()