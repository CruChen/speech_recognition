import itertools

def generate_sentences(template, data_file):
    def replace_hash_with_txt_data(text):
        data = read_data_from_txt(data_file)
        return [text.replace('#', value) for value in data]

    sentences = []
    if '[' not in template and ('(' not in template or ')' not in template) and '#' in template:
        txt_templates = replace_hash_with_txt_data(template)
        for txt_template in txt_templates:
            sentences.extend(generate_sentences(txt_template, data_file))
    elif '[' not in template and ('(' not in template or ')' not in template):
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
                sentences.extend(generate_sentences(prefix + option + suffix, data_file))
            template = prefix + suffix

        # 检查是否存在必选项
        if '(' in template and ')' in template:
            start = template.index('(')
            end = template.index(')')
            options = template[start+1:end].split('|')
            prefix = template[:start]
            suffix = template[end+1:]
            for option in options:
                sentences.extend(generate_sentences(prefix + option + suffix, data_file))
            template = prefix + suffix

    return sentences

def read_data_from_txt(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.read().splitlines()
    return data

def write_to_file(sentences, filename):
    with open(filename, 'a', encoding='utf-8') as f:
        for sentence in sentences:
            f.write(sentence + '\n')

template = "联系人[姓名][为|是]#"
data_file = '../data/data3.txt'  # 替换为您的文本文件名

sentences = generate_sentences(template, data_file)
write_to_file(sentences, 'output1.txt')

print("All sentences have been written to output.txt file.")