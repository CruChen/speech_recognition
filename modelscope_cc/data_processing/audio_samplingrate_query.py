# 进行wav文件采样率的查询

import os
import soundfile as sf

def get_sample_rate(file_path):
    data, sample_rate = sf.read(file_path)
    return sample_rate

data_folder = r"D:\data\private_data\ambulance_data"

for filename in os.listdir(data_folder):
    if filename.endswith(".wav"):
        file_path = os.path.join(data_folder, filename)
        sample_rate = get_sample_rate(file_path)
        print(f"{filename}: {sample_rate} Hz")



# # 对单个m4a文件进行采样率的查询
# from mutagen import mp4
#
# def get_audio_sample_rate(file_path):
#     audio = mp4.MP4(file_path)
#     return audio.info.sample_rate
#
# # 使用函数获取M4A文件的采样率
# file_path = 'D:\data\私有数据集\救护车采集音频2.m4a'
# sample_rate = get_audio_sample_rate(file_path)
# print(f"Audio sample rate: {sample_rate} Hz")



# # 对文件夹中的m4a文件进行采样率的查询
# from mutagen import mp4
# import os
#
# def get_audio_sample_rate(file_path):
#     audio = mp4.MP4(file_path)
#     return audio.info.sample_rate
#
# def process_folder(folder_path):
#     for root, dirs, files in os.walk(folder_path):
#         for file in files:
#             if file.endswith('.m4a'):
#                 file_path = os.path.join(root, file)
#                 sample_rate = get_audio_sample_rate(file_path)
#                 print(f"File: {file_path}, Sample Rate: {sample_rate} Hz")
#
# # 使用函数处理包含M4A文件的文件夹
# folder_path = 'D:\caching\python\cache\ModelScope\data\m4a'
# # folder_path ='D:\data\电子病历\电子病历模板及字段赋值明细\sound_recording'
#
# process_folder(folder_path)
