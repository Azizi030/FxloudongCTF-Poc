import requests
import re
from pyDes import des, CBC, PAD_PKCS5
import binascii
import http_vlue as hv

print("物智学院CTF平台")
print("课程：漏洞扫描与安全审计")
print("实验5_http-post-for-python-static")

url = 'http://10.68.6.202:'
port = input("请输入端口:")

headers = {
    'POST': '/altoro/bank/doTransfer',  
    'AltoroAccounts': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0360',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://10.68.6.202:'+port,
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1',
    'Referer': 'http://10.68.6.202:'+port,
    'Cookie': 'session=fce44c5c-fe48-41d1-960a-c0c9dab49f45.U_PGzLexSJAYZHOGRuEL1XZYvsc'
}
payload = {
    'transfer': '1',
    'fromAccount': '1',
    'toAccount': '2',
    'transferAmount': '123456'
}
if hv.get_qx():
    # 提交 POST 请求
    response = requests.post(url + port, headers=headers, data=payload)

    # 从响应文本中查找 Flag
    flag_match = re.search(r'Flag\{([\w-]+)\}', response.text)
    if flag_match:
        flag = flag_match.group(1).strip()
        print("已经找到密文:\n", flag)
        input("请按回车键进行解密...")

        # 进行DES解密
        key = b'mituhelo'
        iv = b'test__IV'
        encrypted_flag = binascii.unhexlify(flag)
        des_cipher = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)
        decrypted_flag = des_cipher.decrypt(encrypted_flag).decode()
        print("解密后的密文:", decrypted_flag)
        input("请按回车键继续...")
    else:
        print("未找到 Flag。")
        input("请按回车键继续...")
else:
    print("失败，原因：权限不足！")
    input("请按回车键继续...")
