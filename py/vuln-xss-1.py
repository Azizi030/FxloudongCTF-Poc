import requests
import re
import http_vlue as hv

print("物智学院CTF平台")
print("课程：漏洞扫描与安全审计")
print("实验4：vuln-xss1扫描 ")

url = "http://10.68.6.202:"
dk = input("请输入端口：")
if hv.get_qx():
    fs = requests.get(url + dk+"/flag.php")
    flag_pattern = r'Flag\{([\w-]+)\}'
    flag = re.search(flag_pattern, fs.text)

    if flag:
        print("已经找到答案：Flag{" + flag.group(1) + "}")
        input("请按回车键继续...")
    else:
        print("未找到答案。")
        input("请按回车键继续...")
else:
    print("失败，原因：权限不足！")
    input("请按回车键继续...")
