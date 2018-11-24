import subprocess
# cmd = "ps -C sshd -o pid,cmd|wc -l"
# p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# stdout, stderr = p.communicate()
# print(stdout.decode('utf8'))
# if int(stdout) > 2:
#     print("sshd service is ok")
# else:
#     print("sshd service is not ok")


cmd = "ps -C sshd -o pid,cmd|wc -l"


def judgeservice(command):
    p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if int(stdout) > 2:
        print("service is ok")
    else:
        print("service is not ok")


if __name__ == '__main__':
    i = 0
    while i < 5:
        judgeservice(cmd)
        i = i + 1
