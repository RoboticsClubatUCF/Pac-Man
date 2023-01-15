import os
import sys


def main():
    if os.name == "posix":
        stream = os.popen('nmap -p 3306 172.17.0.*')
        out = stream.read()
        print(out)
        ind = out.index("open  mysql")
        print(ind)
        ip = out[ind-75:ind-65]
        print(ip)
        with open("./etc/mysql/my.cnf", "r") as f:
            lines = f.readlines()
            i = -2
            for line in lines:
                try:
                    i+=1
                    ind = line.index("host")
                except:
                    pass
        print(lines)
        print(i)
        print("Making changes")
        lines[i] = "host = " + ip + "\n"
        print(lines)
        with open("./etc/mysql/my.cnf", "w") as f:
            for line in lines:
                f.write(line)
