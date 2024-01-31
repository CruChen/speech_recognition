import os
import shutil
import zipfile

# 指定要处理的文件夹路径
source_folder_path = 'mac_wav'

# 获取源文件夹的绝对路径
absolute_source_path = os.path.abspath(source_folder_path)

# 遍历指定文件夹下所有的.zip文件
for filename in os.listdir(absolute_source_path):
    if filename.endswith(".zip"):
        # 获取不带扩展名的文件名作为新文件夹名称
        base_name = os.path.splitext(filename)[0]

        # 创建与.zip文件同名的新文件夹，路径基于源文件夹
        new_folder_path = os.path.join(absolute_source_path, base_name)
        os.makedirs(new_folder_path, exist_ok=True)

        # 获取当前.zip文件的完整路径（使用绝对路径）
        zip_file_path = os.path.join(absolute_source_path, filename)
        target_zip_file_path = os.path.join(new_folder_path, filename)

        # 移动.zip文件到新创建的文件夹中
        shutil.move(zip_file_path, target_zip_file_path)

        # 在新创建的文件夹内解压.zip文件
        with zipfile.ZipFile(target_zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(new_folder_path)

        # 解压完成后，删除.zip文件
        os.remove(target_zip_file_path)

        print(f"成功解压并移动了 {filename} 到 {new_folder_path} 文件夹，并已删除压缩包。")

print("所有操作已完成。")