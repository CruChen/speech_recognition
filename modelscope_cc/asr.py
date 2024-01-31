# # 对单个文件进行语音识别
# from modelscope.pipelines import pipeline
# from modelscope.utils.constant import Tasks
#
#
# inference_pipeline = pipeline(
#     task=Tasks.auto_speech_recognition,
#     model='model\speech_paraformer_asr_nat-zh-cn-16k-common-vocab8358-tensorflow1')
#
# rec_result = inference_pipeline(audio_in='data/true_ambulance_data03/true_ambulance_data13.wav')
# print(rec_result)


# # 对一个文件夹中的文件进行语音识别
# from modelscope.pipelines import pipeline
# from modelscope.utils.constant import Tasks
# import os
#
# inference_pipeline = pipeline(
#     task=Tasks.auto_speech_recognition,
#     model='model\speech_paraformer_asr_nat-zh-cn-16k-common-vocab8358-tensorflow1')
#
# audio_dir = 'data/true_ambulance_data03/'
#
# for filename in os.listdir(audio_dir):
#     if filename.endswith(".wav"):
#         audio_path = os.path.join(audio_dir, filename)
#         rec_result = inference_pipeline(audio_in=audio_path)
#         print(rec_result)

# # 对一个文件夹中的文件进行语音识别，且知道是从哪个wav文件中识别出来的
# from modelscope.pipelines import pipeline
# from modelscope.utils.constant import Tasks
# import os
#
# inference_pipeline = pipeline(
#     task=Tasks.auto_speech_recognition,
#     model='model\speech_paraformer_asr_nat-zh-cn-16k-common-vocab8358-tensorflow1')
#
# audio_dir = 'data/true_ambulance_data03/'
#
# for filename in os.listdir(audio_dir):
#     if filename.endswith(".wav"):
#         audio_path = os.path.join(audio_dir, filename)
#         rec_result = inference_pipeline(audio_in=audio_path)
#
#         # 添加音频文件名到识别结果前面
#         output_text = f"{filename}: {rec_result['text']}"
#         print(output_text)

# # 处理异常的版本
# import logging
#
# # 设置日志级别
# logging.basicConfig(level=logging.INFO)
#
# from modelscope.pipelines import pipeline
# from modelscope.utils.constant import Tasks
# import os
#
# inference_pipeline = pipeline(
#     task=Tasks.auto_speech_recognition,
#     model='model\speech_paraformer_asr_nat-zh-cn-16k-common-vocab8358-tensorflow1')
#
# audio_dir = 'data/true_ambulance_data04/'
#
# for filename in os.listdir(audio_dir):
#     if filename.endswith(".wav"):
#         audio_path = os.path.join(audio_dir, filename)
#
#         try:
#             rec_result = inference_pipeline(audio_in=audio_path)
#
#             # 尝试获取识别文本，如果存在，则打印出来
#             text_key = 'text'  # 根据实际模型返回结果中的键名进行替换
#             if text_key in rec_result:
#                 output_text = f"{filename}: {rec_result[text_key]}"
#                 print(output_text)
#             else:
#                 logging.warning(f"Failed to get transcription for file '{filename}'. Skipping.")
#
#         except Exception as e:
#             # 捕获并记录所有其他可能发生的异常，然后继续处理下一个文件
#             logging.error(f"An error occurred while processing file '{filename}': {str(e)}")


# 此版本会把有用的信息存进一个txt文件中
import logging
import sys
from io import StringIO

# 设置日志级别为ERROR以过滤掉INFO级别的消息
logging.basicConfig(level=logging.ERROR)

from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
import os

inference_pipeline = pipeline(
    task=Tasks.auto_speech_recognition,
    model='model\speech_paraformer_asr_nat-zh-cn-16k-common-vocab8358-tensorflow1')

audio_dir = 'data/true_ambulance_data06/'
asr_texts = []

for filename in os.listdir(audio_dir):
    if filename.endswith(".wav"):
        audio_path = os.path.join(audio_dir, filename)

        # 创建一个新的输出流来捕获标准输出
        old_stdout = sys.stdout
        captured_output = StringIO()
        sys.stdout = captured_output

        try:
            rec_result = inference_pipeline(audio_in=audio_path)

            text_key = 'text'  # 根据实际模型返回结果中的键名进行替换
            if text_key in rec_result:
                print(f"{filename}: {rec_result[text_key]}")

                # 将识别出的文本添加到列表中
                asr_texts.append(f"{filename}: {rec_result[text_key]}")

        except Exception as e:
            # 恢复标准输出并记录错误信息
            sys.stdout = old_stdout
            logging.error(f"An error occurred while processing file '{filename}': {str(e)}")
            continue

        # 恢复标准输出
        sys.stdout = old_stdout
        captured_output.truncate(0)  # 清空缓冲区以便下一次循环使用

# 将所有有用的信息写入到txt文件中
with open('asr_result/asr_results.txt', 'w', encoding='utf-8') as output_file:
    for text in asr_texts:
        output_file.write(text + '\n')
