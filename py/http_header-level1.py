import requests
import http_vlue as hv

print("物智学院CTF平台")
print("课程：漏洞扫描与安全审计")
print("header-level1")

url = 'http://10.68.6.202:'
port = input("请输入端口:")

headers = {
    'X-Forwarded-For': '1.2.3.4',
}

if hv.get_qx():
    # 提交 GET 请求
    response = requests.get(url + port, headers=headers)

    # 从响应头中查找 Flag
    flag = response.headers.get('hereisflag')  # 假设 Flag 在响应头中以 'Flag' 字段表示

    if flag:
        print("这个似乎是答案：", flag)
        input("请按回车键继续...")
    else:
        print("未找到 Flag。")
        input("请按回车键继续...")
else:
    print("失败，原因：权限不足！")
    input("请按回车键继续...")