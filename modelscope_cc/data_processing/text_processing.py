# 从文本文件中读取输入字符串
with open('train.text', 'r', encoding='utf-8') as file:
    input_str = file.read()

# 提取每行的中文部分并加空格
lines = input_str.split('\n')
processed_lines = []
for line in lines:
    parts = line.split(' ')
    if len(parts) > 1:
        chinese_part = parts[1]
        output_str = ' '.join(list(chinese_part))
        processed_line = line.replace(chinese_part, output_str, 1)
        processed_lines.append(processed_line)
    else:
        processed_lines.append(line)

# 将处理后的字符串写入新的文本文件
result = '\n'.join(processed_lines)
with open('new_train.text', 'w', encoding='utf-8') as file:
    file.write(result)

print("处理完成，并已将结果写入new_train.text文件。")