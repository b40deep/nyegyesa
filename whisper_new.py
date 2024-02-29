from transformers import WhisperProcessor, WhisperForConditionalGeneration
from datasets import Audio, load_dataset
# for gradio
import gradio as gr



# load model and processor
processor = WhisperProcessor.from_pretrained("openai/whisper-base")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-base")
forced_decoder_ids = processor.get_decoder_prompt_ids(language="french", task="translate")

def runSTT(audio):
    # load streaming dataset and read first audio sample
    # ds = load_dataset("common_voice", "fr", split="test", streaming=True)
    ds = load_dataset("mozilla-foundation/common_voice_11_0", "en")
    ds = ds.cast_column("audio", Audio(sampling_rate=16_000))
    print(f'ds {type(ds)}')
    input_speech = next(iter(ds))["audio"]
    print(f'inp {type(input_speech)}')
    # input_speech = audio
    input_features = processor(input_speech["array"], sampling_rate=input_speech["sampling_rate"], return_tensors="pt").input_features

    # generate token ids
    predicted_ids = model.generate(input_features, forced_decoder_ids=forced_decoder_ids)
    # decode token ids to text
    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)



#####################################################################
#####################     default function      #####################
#####################################################################

def runCombined(mic, text, models):
    print('╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦     runCombined     ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦')
    # if len(models)>0:
    #     for item in models:
    #         loadSTT() if item == 'STT' else loadLLM() if item == 'LLM' else loadTTS() if item == 'TTS' else None
    # loadSTT()
    
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