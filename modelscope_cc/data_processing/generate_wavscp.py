import os

def generate_wav_scp(upper_dir, output_path):
    with open(output_path, 'w', encoding='utf-8') as f_out:
        for root, dirs, files in os.walk(upper_dir):
            # 只处理包含.wav文件的子目录
            if any(file.endswith('.wav') for file in files):
                for file in files:
                    if file.endswith('.wav'):
                        audio_id = os.path.splitext(file)[0]
                        audio_path = os.path.join(root, file)
                        f_out.write(f"{audio_id} {audio_path}\n")

# 使用函数生成wav.scp文件，这里假设顶层目录下直接包含了音频子文件夹
upper_audio_dir = r'../data/finetune_data/train'
output_path = r'trainwav.scp'
generate_wav_scp(upper_audio_dir, output_path)