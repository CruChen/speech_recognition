from modelscope.outputs import OutputKeys
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

text = '今天杭州天气怎么样'
model_id = '..\model\speech_sambert-hifigan_tts_zhiyan_emo_zh-cn_16k'
sambert_hifigan_tts = pipeline(task=Tasks.text_to_speech, model=model_id)
output = sambert_hifigan_tts(input=text)
wav = output[OutputKeys.OUTPUT_WAV]
with open('output.wav', 'wb') as f:
    f.write(wav)
