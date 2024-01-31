from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
# from flask import Flask, request
# from flask_cors import CORS

def denoise(input_audio_file, output_audio_file):
    ans = pipeline(
        task=Tasks.acoustic_noise_suppression,
        model='model\speech_frcrn_ans_cirm_16k')
    result = ans(
        input_audio_file,
        output_path=output_audio_file)

# @app.route('/api/audio', methods=['POST'])
def recognize_audio(audio_in):
    inference_pipeline = pipeline(
        task=Tasks.auto_speech_recognition,
        model='model\speech_paraformer_asr_nat-zh-cn-16k-common-vocab8358-tensorflow1')
    rec_result = inference_pipeline(audio_in)
    return rec_result

# 输入待处理的语音文件
input_audio_file = r'D:\caching\python\cache\ModelScope\data\true_ambulance_data02\true_ambulance_data01.wav'

# 输出降噪后的语音文件
output_audio_file = 'output03.wav'

# 执行降噪并保存降噪后的语音文件
denoise(input_audio_file, output_audio_file)

# 对降噪后的音频进行语音识别
rec_result = recognize_audio(output_audio_file)

print(rec_result)

