# general
import time

# for whisper stt
from transformers import pipeline
# for gradio
import gradio as gr


#####################################################################
#################     modularise model imports    ###################
#####################################################################

llm_tokenizer = None
llm_model = None
whisper_model = None
start_time = None
bark_processor = None
voice_preset = None

def loadSTT():
    print('loading STT works')
    global whisper_model
    whisper_model = pipeline("automatic-speech-recognition", model="openai/whisper-base")
# , language='en'



#####################################################################
#####################     whisper stt      ##########################
#####################################################################

def runSTT(audio):
    print('╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦     runSTT     ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦')
    tic = time.perf_counter()
    result = whisper_model(audio)["text"]
    toc = time.perf_counter()
    print(f"################ stt result: { result}")
    print(f"████████████████ STT finished in {(toc - tic)/60:0.4f} minutes ████████████████")
    return result




#####################################################################
#####################     default function      #####################
#####################################################################

def runCombined(mic, text, models):
    print('╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦     runCombined     ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦')
    # if len(models)>0:
    #     for item in models:
    #         loadSTT() if item == 'STT' else loadLLM() if item == 'LLM' else loadTTS() if item == 'TTS' else None
    loadSTT()
    
    to_llm = runSTT(mic)
    # to_tts = runLLM(to_llm)
    # result = runTTS2(to_tts)
    result = to_llm
    return result




#####################################################################
#####################     gradio UI     #############################
#####################################################################

in_mic = gr.Audio(sources=["microphone"],type="filepath", label="Mic Input")
in_text = gr.Textbox(placeholder="Record with the mic, or type here instead.", label="Text Input")
in_models = gr.CheckboxGroup(["STT", "LLM", "TTS"], label="Models", info="Which model to load?")
iface = gr.Interface(fn=runCombined,inputs=[in_mic, in_text, in_models],outputs="text",live=False)
iface.launch(debug=True)