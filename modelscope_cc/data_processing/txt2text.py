import os

# 指定要合并的文件所在的目录
directory = 'D:\data\私有数据集\wav/finetune_data/validation'

# 新文件的路径
new_file_path = 'text.text'

# 打开新文件用于写入，假设我们使用UTF-8编码
with open(new_file_path, 'w', encoding='utf-8') as outfile:
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            # 获取完整文件路径
            file_path = os.path.join(directory, filename)

            # 打开每个文本文件并读取内容，尝试使用UTF-8编码
            with open(file_path, 'r', encoding='utf-8') as infile:
                try:
                    content = infile.read()
                except UnicodeDecodeError:
                    print(f"无法以UTF-8编码读取文件 {file_path}，请检查其编码格式")
                else:
                    # 将内容追加到新文件中
                    outfile.write(content + '\n' * 2)  # 在每个文件之间添加两行空行以便区分

# 确保所有内容都已写入新文件，并且在脚本结束时会自动关闭outfile



# 将.text文件中，如果这一行没有文字，则删除此行
# 打开并读取原始.text文件
with open('text.text', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 删除空白行，并创建一个新的内容列表
filtered_lines = [line for line in lines if line.strip()]

# 写入新的不包含空白行的.text文件
with open('validation.text', 'w', encoding='utf-8') as file:
    file.writelines(filtered_lines)