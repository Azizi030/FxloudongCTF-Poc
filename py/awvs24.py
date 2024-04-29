import http_vlue as hv
print("物智学院CTF平台")
print("课程：漏洞扫描与安全审计")
print("awvs24扫描器 ")

a=input("请输入端口号：")

if hv.get_qx():
    print("已找到答案：Flag{https}")
    input("请按回车键继续...")
else:
    print("失败！原因：权限不足！")
    input("请按回车键继续...")