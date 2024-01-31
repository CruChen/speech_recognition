import wave
import numpy as np


def split_audio(input_file, output_prefix, duration=30):
    # 打开wav文件
    with wave.open(input_file, 'r') as w:
        params = w.getparams()
        nchannels, sampwidth, framerate, nframes = params[:4]
        audio_data = w.readframes(nframes)
        audio_samples = np.frombuffer(audio_data, dtype=np.int16)

    # 计算需要分割的数量
    total_seconds = nframes / framerate
    chunks_count = int(total_seconds // duration) + (total_seconds % duration > 0)

    for i in range(chunks_count):
        start_index = i * duration * framerate
        end_index = min((i + 1) * duration * framerate, nframes)

        chunk_samples = audio_samples[start_index:end_index]

        # 创建新的wave文件并写入数据
        output_filename = f"{output_prefix}{i + 1:02}.wav"
        with wave.open(output_filename, 'w') as out_w:
            out_w.setparams(params)
            out_w.writeframes(chunk_samples.tobytes())


if __name__ == "__main__":
    input_file = r"D:\data\private_data\ambulance_data\1_30_03.wav"  # 原始wav文件路径
    output_prefix = r"D:\caching\python\cache\ModelScope\data\true_ambulance_data"  # 输出文件名前缀
    split_audio(input_file, output_prefix)