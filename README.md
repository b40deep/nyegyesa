# Nyegyesa: a speech-based language-learning assistant!

## Scenario

pending update

## Why does this project exist?

I started this project to immerse myself in the world of open-source AI models. My goal is to use this to learn a language by practicing speaking the sentences I actually want to say, rather than the ones on the language-learning app.
It would entail:

- speech to text model
- language-to-language translation model
- text to speech model that will 'speak' the result to me in MY intonation [a voice cloning model] so I can directly copy that.

## How to set it up

### setting up a virtual envirionment

I'm using python Python 3.10.0rc2
I'm using python venv
setting up one venv on cmd
`python -m venv name_of_virtual_env`
to activate the venv, use `.\name_of_virtual_env\Scripts\Activate.ps1` on PowerShell and `.\name_of_virtual_env\Scripts\activate.bat` on CMD (though this might work for either?)
if you're using vscode, install the Python extension and set up the venv inside your project folder. This way, VS Code will run the venv automatically when you run a Python file.

### downloading the dependencies

I used a requirements file because it's cleaner for me to keep track of. I added comments to it to let me know which model needs which deps since I'm using more than one model.
`pip install -r .\requirements.txt`
I also added a `req_list_from_pip.txt` file that has all the versions, even of dependency dependencies.

### downloading the transformers

```
git clone https://github.com/huggingface/transformers.git
cd transformers
pip install -e .
```

<!-- ### installing an older torch version to avoid all the problems I ran into

`pip install torch==2.0.0 torchvision==0.15.1 torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/cu118`
from https://pytorch.org/get-started/previous-versions/

### symlink to move cache to another location

`mklink /J C:\users\.cache\huggingface E:\boyd_cache\huggingface` -->

### ffmpeg install for the text to speech [currently using bark]

https://www.wikihow.com/Install-FFmpeg-on-Windows to download and install
then `ffmpeg` and `ffmpeg-python` added to the deps

## thoughts / troubles / todos:

- ✅Finished setting up Whisper STT
- Whisper that I used seems to be old. I'm getting a `ERROR:    Exception in ASGI application` that doesn't stop the app from running but is definitely not happy. Other than that, it works fine.
- Example output:
  - Result: `STT result: Buenos días, buenos tardes, buenos noches, hola`
  - Time taken: `STT finished in 0.0136 minutes`
- \*️⃣Next step is to add keywords like `language='es'` so that whatever I speak is returned as spanish.

## snapshot of resource usage:
