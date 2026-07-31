# task-3-on-AI
# Voice-to-Voice AI Assistant

## Project Overview

This project is a simple **Voice-to-Voice AI Assistant** built using Python.

The assistant performs three main tasks:

1. Converts the user's speech into text using **RealtimeSTT**.
2. Sends the text to the **Cohere Large Language Model** to generate an intelligent response.
3. Converts the generated response back into speech using **RealtimeTTS**.

---

# Code Explanation

## 1. Import Libraries

```python
import os
import cohere
from dotenv import load_dotenv
from RealtimeSTT import AudioToTextRecorder
from RealtimeTTS import TextToAudioStream, SystemEngine
```

### Explanation

The program imports all required libraries.

- `os` is used to read environment variables.
- `cohere` connects the application to the Cohere API.
- `load_dotenv()` loads the API key from the `.env` file.
- `AudioToTextRecorder` converts speech into text.
- `TextToAudioStream` and `SystemEngine` convert text into speech.

---

## 2. Load the API Key

```python
load_dotenv()

api_key = os.getenv("COHERE_API_KEY")
print("API Key:", api_key)

co = cohere.Client(api_key)
```

### Explanation

The API key is stored securely inside the `.env` file.

The program loads the key and creates a connection with the Cohere API.

---

## 3. Create the Main Function

```python
def main():
```

### Explanation

The `main()` function contains the complete workflow of the voice assistant.

---

## 4. Initialize Speech Recognition

```python
recorder = AudioToTextRecorder()
```

### Explanation

Creates the speech recognition object.

The assistant starts listening to the microphone waiting for the user to speak.

---

## 5. Continuous Loop

```python
while True:
```

### Explanation

Keeps the assistant running continuously so the user can ask multiple questions without restarting the program.

---

## 6. Convert Speech to Text

```python
text = recorder.text()
```

### Explanation

The assistant listens to the user's speech and converts it into text.

Example:

```
User:
What is AI?

↓

Text:
What is AI?
```

---

## 7. Display User Speech

```python
print("You:", text)
```

### Explanation

Prints the recognized speech in the terminal.

Example:

```
You: What is AI?
```

---

## 8. Exit the Program

```python
if text.lower() == "exit":
    break
```

### Explanation

If the user says **exit**, the program stops.

---

## 9. Send the Question to Cohere

```python
response = co.chat(
    model="command-a-03-2025",
    message=text
)
```

### Explanation

The recognized text is sent to the Cohere Large Language Model.

The AI processes the question and generates a suitable response.

---

## 10. Store the AI Response

```python
reply = response.text
```

### Explanation

Extracts the generated text from the Cohere response.

Example:

```
Artificial Intelligence is...
```

---

## 11. Display the AI Response

```python
print("AI:", reply)
```

### Explanation

Prints the generated response in the terminal.

Example:

```
AI: Artificial Intelligence is the simulation of human intelligence...
```

---

## 12. Convert Text to Speech

```python
engine = SystemEngine()

stream = TextToAudioStream(engine)

stream.feed(reply)

stream.play()
```

### Explanation

This section converts the generated text into speech.

- `SystemEngine()` uses the Windows speech engine.
- `TextToAudioStream()` prepares the speech.
- `feed()` sends the AI response to the speech engine.
- `play()` plays the voice through the computer speakers.

---

# Program Workflow

```
User Speaks
      │
      ▼
RealtimeSTT
      │
      ▼
Speech → Text
      │
      ▼
Cohere API
      │
      ▼
AI Response
      │
      ▼
RealtimeTTS
      │
      ▼
Speech Output
```

---

# Technologies Used

- Python 3.11
- Cohere API
- RealtimeSTT
- RealtimeTTS
- python-dotenv

---

# Project Features

- Voice-to-Text conversion.
- AI-generated responses using Cohere.
- Text-to-Speech conversion.
- Continuous conversation loop.
- Voice command (`exit`) to stop the assistant.

- ## Notes

- The `.env` file is not included in the repository for security reasons.
- Users must create their own `.env` file and add a valid Cohere API key before running the project.
