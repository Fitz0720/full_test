import subprocess
import os, shlex

BASE_DIR = os.path.dirname(__file__)
while True:
    cmd_str = input(">>> ")
    # cmd_list = shlex.split(cmd_str)[0]
    cmd_list = cmd_str.split(" ")
    if cmd_list[0] == "cd":
        path_str = cmd_list[1]
        if path_str.startswith("/") or ((path_str[1] if len(path_str) > 2 else False)) == ":"):
            if os.path.isdir(path_str):
                os.chdir(path_str)
        for path in path_list:
            if path != "..":
                break
            else:
                BASE_DIR = os.path.dirname(BASE_DIR)
        os.chdir(BASE_DIR)
    else:
        cmd=subprocess.Popen(cmd_str,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        print("pid:", cmd.pid)
        cmd_res=cmd.stdout.read()

        if not cmd_res:

            cmd_res=cmd.stderr.read()

        if len(cmd_res)==0:

            cmd_res=bytes("result",encoding='gbk')
        print(cmd_res.decode('gbk'))