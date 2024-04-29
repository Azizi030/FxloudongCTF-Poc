import paramiko
import http_vlue as hv
print("物智学院CTF平台")
print("课程：漏洞扫描与安全审计")
print("实验8_sqli数据库")

# SSH连接参数
ssh_host = '10.68.6.202'
ssh_port = int(input("请输入SSH端口："))
ssh_username = 'root'
ssh_password = 'P@ssw0rd'

if hv.get_qx():
    # 连接远程主机
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_client.connect(hostname=ssh_host, port=ssh_port, username=ssh_username, password=ssh_password)

        # 执行MySQL查询
        try:
            # 执行SQL查询命令
            stdin, stdout, stderr = ssh_client.exec_command("mysql -u root -pP@ssw0rd -e \"USE security; SELECT * FROM emails WHERE email_id REGEXP 'Flag{[^}]+}';;\"")

            # 输出查询结果
            for line in stdout:
                print(line.strip())
            input("请按回车键继续...")
        except Exception as e:
            print("An error occurred while executing MySQL query:", e)
            input("请按回车键继续...")

        # 关闭SSH连接
        ssh_client.close()

    except Exception as e:
        print("An error occurred while connecting via SSH:", e)
        input("请按回车键继续...")
else:
    print("失败，原因：权限不足！")
    input("请按回车键继续...")