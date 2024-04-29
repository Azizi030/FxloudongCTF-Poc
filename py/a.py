import os
import subprocess

# 指定待封装的Python文件所在的目录
source_directory = "D:\Python项目\loudongCTF"

# 获取目录中所有的Python文件
python_files = [file for file in os.listdir(source_directory) if file.endswith(".py")]

# 循环处理每个Python文件
for py_file in python_files:
    # 构建PyInstaller命令
    command = f"pyinstaller --onefile {os.path.join(source_directory, py_file)}"

    # 执行PyInstaller命令
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Successfully packaged {py_file} to exe.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to package {py_file}: {e}")
