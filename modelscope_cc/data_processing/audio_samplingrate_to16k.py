import os
from pydub import AudioSegment

# 定义函数用于将采样率从44.1k改为16k
def convert_sample_rate(input_file, output_file):
    sound = AudioSegment.from_file(input_file)
    new_sound = sound.set_frame_rate(16000)
    new_sound.export(output_file, format="wav")

# 获取文件夹中所有的wav文件
input_folder = "D:\caching\python\cache\ModelScope\data/true_ambulance_data03"
output_folder = "output_folder"

for filename in os.listdir(input_folder):
    if filename.endswith(".wav"):
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, filename)
        convert_sample_rate(input_file, output_file)

print("所有音频文件采样率转换完成")