import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np

# 读取音频文件
audio_file = '../output/output1.wav'
data, sample_rate = sf.read(audio_file)

# 计算频谱
spectrum = np.abs(np.fft.fft(data))

# 计算频率轴
freqs = np.fft.fftfreq(len(spectrum), d=1/sample_rate)

# 只显示正频率部分
plt.plot(freqs[:len(freqs)//2], spectrum[:len(freqs)//2])

# 设置图形标题和标签
plt.title('音频频谱')
plt.xlabel('频率 (Hz)')
plt.ylabel('波幅')

# 显示图形
plt.show()