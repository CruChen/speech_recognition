import os
import json
import base64
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
from flask import Flask, request
from flask_cors import CORS
import processing_utils
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def denoise(input_audio_file, output_audio_file):
    ans = pipeline(
        task=Tasks.acoustic_noise_suppression,
        model='model\speech_frcrn_ans_cirm_16k')
    result = ans(
        input_audio_file,
        output_path=output_audio_file)


def recognize_audio(audio_in):
    inference_pipeline = pipeline(
        task=Tasks.auto_speech_recognition,
        model='model\speech_paraformer_asr_nat-zh-cn-16k-common-vocab8358-tensorflow1')
    rec_result = inference_pipeline(audio_in)
    return rec_result

@app.route('/api/audio', methods=['POST'])
def process_audio():
    datas = json.loads(request.get_data())
    audio_datas = datas.get("data")
    ret = []
    for audio_dict in audio_datas:
        audio_base64 = audio_dict.get("data")
        audio_base64 = audio_base64.split(",")[1]

        decoded_audio = base64.b64decode(audio_base64)
        audio_name = f"input_audio/" + audio_dict.get("name")
        audio_path = os.path.join(f"input_audio/", audio_name)
        os.makedirs(os.path.dirname(audio_path), exist_ok=True)  # 确保父目录存在，exist_ok=True表示如果目录已存在则不报错
        # 解码二进制数据写入文件
        with open(audio_path, "wb") as fb:
            fb.write(decoded_audio)
        # 将数据从文件中读出
        crop_min, crop_max = datas.get("crop_min", 0), datas.get("crop_max", 100)
        sample_rate, data = processing_utils.audio_from_file(
            audio_path, crop_min=crop_min, crop_max=crop_max
        )
        # 写入wav文件
        processing_utils.audio_to_file(
            sample_rate, data, audio_path, format="wav"
        )
        # 推理
        print(f"现在开始推理，audio_path:{audio_path}")
        ret.append(recognize_audio(audio_in=audio_path))
    # 在这里添加音频处理代码
    # 处理完毕后，可以选择将处理后的数据作为响应返回
    return ret



if __name__ == "__main__":
    app.run(port=3000, debug=True)

