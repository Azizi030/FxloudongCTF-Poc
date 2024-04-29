@echo off
echo 请先确认网络连接正常（登录校园网）
pause
echo 正在安装依赖
pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pyDes -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install paramiko -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install mysql-connector-python -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install gmssl -i https://pypi.tuna.tsinghua.edu.cn/simple
echo 脚本完成
pause