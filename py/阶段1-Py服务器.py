import socket
import http_vlue as hv
from gmssl.sm4 import CryptSM4, SM4_DECRYPT


def main():
    target_ip = "10.68.6.202"
    target_port = int(input("请输入端口:"))

    try:
        # 连接服务器
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((target_ip, target_port))
        print("[*] Connected to server")

        # 接收加密后的flag
        encrypted_flag = client_socket.recv(1024)

        # 解密flag
        decrypted_flag = decrypt_data(encrypted_flag)

        # 打印flag
        print("Decrypted Flag:", decrypted_flag.decode('utf-8'))

    except Exception as e:
        print("Error:", str(e))
    finally:
        client_socket.close()

def decrypt_data(data):
    key = b'3l5butlj26hvv313'
    crypt_sm4 = CryptSM4()
    crypt_sm4.set_key(key, SM4_DECRYPT)
    decrypted_value = crypt_sm4.crypt_ecb(data)  # bytes类型
    return decrypted_value

if __name__ == "__main__":
    print("物智学院CTF平台")
    print("课程：漏洞扫描与安全审计")
    print("阶段考1-Py服务器")
    if hv.get_qx():
        main()
        input("请按回车键继续...")
    else:
        print("失败，原因：权限不足！")
        input("请按回车键继续...")