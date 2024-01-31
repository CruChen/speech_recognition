'''
import chardet


def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        return result['encoding']


print(detect_encoding('wav.scp'))
print(detect_encoding('targetwav.scp'))

'''
import codecs

def utf8_to_gbk(file_path_in, file_path_out):
    # 打开UTF-8编码的输入文件
    with codecs.open(file_path_in, 'r', encoding='utf-8') as f_in:
        content_utf8 = f_in.read()

    # 将内容写入GBK编码的输出文件
    with codecs.open(file_path_out, 'w', encoding='gbk') as f_out:
        f_out.write(content_utf8)

# 使用函数进行转换
utf8_to_gbk('wav.scp', 'targetwav.scp')
