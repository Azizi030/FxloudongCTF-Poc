import http_vlue as hv
print("物智学院CTF平台")
print("课程：漏洞扫描与安全审计")
print("实验4：nikto-xss扫描")

a=input("请输入端口:")

if hv.get_qx():
    print("已为您找到答案：flag{True}")
    input("请按回车键继续...")
else:
    print("失败，原因：权限不足！")
    input("请按回车键继续...")