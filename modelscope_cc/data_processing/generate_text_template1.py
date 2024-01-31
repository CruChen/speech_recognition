# 将excel中的一列数据生成一段问文字模板


import pandas as pd
import itertools

def generate_sentences(template):
    sentences = []
    if '[' not in template and '(' not in template:
        return [template]
    else:
        # 处理可选项
        while '[' in template:
            start = template.index('[')
            end = template.index(']')
            options = template[start+1:end].split('|')
            prefix = template[:start]
            suffix = template[end+1:]
            for option in options:
                sentences.extend(generate_sentences(prefix + option + suffix))
            template = prefix + suffix

        # 处理必选项
        while '(' in template:
            start = template.index('(')
            end = template.index(')')
            options = template[start+1:end].split('|')
            prefix = template[:start]
            suffix = template[end+1:]
            for option in options:
                sentences.extend(generate_sentences(prefix + option + suffix))
            template = prefix + suffix

    return sentences

def write_to_file(sentences, filename):
    with open(filename, 'a', encoding='utf-8') as f:
        for sentence in sentences:
            f.write(sentence + '\n')

# 读取Excel文件中的第三列数据
df = pd.read_excel('创伤类data1.xlsx', usecols=[2])

# 遍历第三列数据并生成句子
for index, template in enumerate(df.iloc[:, 0]):
    sentences = generate_sentences(template)
    write_to_file(sentences, 'output.txt')

print("All sentences have been written to output.txt file.")