import subprocess
import re
import hashlib
from tabulate import tabulate


def calculate_md5(filename):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

file_path=str(input("请输入需要扫描的目录："))

output = subprocess.run(["clamscan", "-r", file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
os_result=str(output.stdout)

check_av=re.findall("(.*): .* FOUND",os_result)
if check_av:
    av_list=[]
    for i in check_av:
        print("[+] 检测到病毒文件："+i)
        one_file=[]
        filename=str(i)
        file_md5=calculate_md5(i)
        one_file.append(filename)
        one_file.append(file_md5)
        av_list.append(one_file)
    headers=["文件名","MD5"]
    print(tabulate(av_list, headers))
else:
    print("[-] 未发现病毒文件")