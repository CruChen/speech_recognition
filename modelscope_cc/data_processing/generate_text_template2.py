import datetime

import numpy as np

# 单纯的生成数字，就是将#换成数字
# def generate_sentences(template):
#     def replace_hash_with_numbers(text, start=1, end=120, step=1):
#         # numbers = [f"{number:.1f}" for number in np.arange(start, end + step, step)]
#         numbers = [f"{number}" for number in np.arange(start, end + step, step)]
#         return [text.replace('#', str(number)) for number in numbers]
#
#     sentences = []
#     if '[' not in template and '(' not in template:
#         if '#' in template:
#             numbers_templates = replace_hash_with_numbers(template)
#             for numbers_template in numbers_templates:
#                 sentences.extend(generate_sentences(numbers_template))
#         else:
#             sentences.append(template)
#     else:
#         while '[' in template:
#             start = template.index('[')
#             end = template.index(']')
#             options = template[start + 1:end].split('|')
#             prefix = template[:start]
#             suffix = template[end + 1:]
#             for option in options:
#                 sentences.extend(generate_sentences(prefix + option + suffix))
#             template = prefix + suffix
#
#         while '(' in template:
#             start = template.index('(')
#             end = template.index(')')
#             options = template[start + 1:end].split('|')
#             prefix = template[:start]
#             suffix = template[end + 1:]
#             for option in options:
#                 sentences.extend(generate_sentences(prefix + option + suffix))
#             template = prefix +(suffix)
#
#         if '#' in template:
#             numbers_templates = replace_hash_with_numbers(template)
#             for numbers_template in numbers_templates:
#                 sentences.extend(generate_sentences(numbers_template))
#
#     return sentences


# 单纯的生成数字，就是将#换成时间
import itertools

def generate_sentences(template):
    def replace_hash_with_times(text):
        times = ["{:02d}:{:02d}".format(h, m) for h in range(24) for m in range(60)]
        return [text.replace('#', time) for time in times]

    sentences = []
    if '[' not in template and '(' not in template:
        if '#' in template:
            times_templates = replace_hash_with_times(template)
            for times_template in times_templates:
                sentences.extend(generate_sentences(times_template))
        else:
            sentences.append(template)
    else:
        while '[' in template:
            start = template.index('[')
            end = template.index(']')
            options = template[start + 1:end].split('|')
            prefix = template[:start]
            suffix = template[end + 1:]
            for option in options:
                sentences.extend(generate_sentences(prefix + option + suffix))
            template = prefix + suffix

        while '(' in template:
            start = template.index('(')
            end = template.index(')')
            options = template[start + 1:end].split('|')
            prefix = template[:start]
            suffix = template[end + 1:]
            for option in options:
                sentences.extend(generate_sentences(prefix + option + suffix))
            template = prefix + suffix

        if '#' in template:
            times_templates = replace_hash_with_times(template)
            for times_template in times_templates:
                sentences.extend(generate_sentences(times_template))

    return sentences


template = "[患者|病人]给药时间[为|是]#"
sentences = generate_sentences(template)

# 将生成的句子追加写入TXT文件中
with open('output1.txt', 'a', encoding='utf-8') as f:
    for sentence in sentences:
        f.write(sentence + '\n')