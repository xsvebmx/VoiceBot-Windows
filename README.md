# VoiceBot for Windows
[![Typing SVG](https://readme-typing-svg.demolab.com?font=&weight=600&size=41&pause=1000&color=F70000&background=A37AFF00&center=true&vCenter=true&random=false&width=500&height=60&lines=VoiceBot+for+Windows)](https://git.io/typing-svg)
## About
A neural network voice model that executes commands on demand, like a voice assistant, but very crude


### Authors:

<a href="https://t.me/Mirya53">
    <img src="https://img.icons8.com/?size=512&id=63306&format=png"width="30" height="30"/>
</a> 


## Screenshots

![App Screenshot](https://github.com/xsvebmx/VoiceBot/blob/main/demo.png)


## Run Locally

Clone the project

```bash
  git clone https://github.com/xsvebmx/VoiceBot.git
```

Go to the project directory

```bash
  cd VoiceBot
```

Install requirements

```bash
  pip install -r requirements.txt
```

Start main.py

```bash
  python main.py
```


## Usage/Examples

```python
import json, pyaudio
from vosk import Model, KaldiRecognizer

model = Model('vosk-model-small-ru-0.4')
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

def listen():
	while True:
		data = stream.read(4000, exception_on_overflow=False)
		if (rec.AcceptWaveform(data)) and (len(data) > 0):
			answer = json.loads(rec.Result())
			if answer["text"]:
				yield answer["text"]

for text in listen():
	if text == "кеша":
		print("Hello")
	elif text == "пока":
		quit()
	else:
		print(text)
```


## Tech Stack

**Client:** Mem usage 6-8gb



