import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

# 用于单个文件的输入
ans = pipeline(
    Tasks.acoustic_noise_suppression,
    model='model/speech_frcrn_ans_cirm_16k')
result = ans(
    r'data/true_ambulance_data01/true_ambulance_data01.wav',
    output_path='output.wav')



# # 用于多个文件的输入
# data_folder = "D:\caching\python\cache\ModelScope\data/true_ambulance_data03"
#
# if not os.path.exists("output"):
#     os.makedirs("output")
#
#
# count = 1
#
# for filename in os.listdir(data_folder):
#     file_path = os.path.join(data_folder, filename)
#
#     if filename.endswith(".wav"):
#         print(f"Processing {filename}...")
#
#         ans = pipeline(
#             Tasks.acoustic_noise_suppression,
#             model='model\speech_frcrn_ans_cirm_16k')
#         result = ans(
#             file_path,
#             output_path=os.path.join("output", f"output{count}.wav"))
#
#         count += 1
