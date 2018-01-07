from cmd import *
import os
import sys
import time
from getpass import *
import traceback

class Cli(Cmd):
    prompt="[root@ifeng.com]"
    intro ="welcome to use my shell"

    def default(self,line):
        if 'EOF' in line.strip():
            sys.exit()
        else:
            self.do_start()

    def emptyline(self):
        pass

    def do_start(self):
        if self.check():
            self.show()
        else:
            self.do_chushihua()

    def check(self):
        count = 0
        pwd = False
        while count < 3:
            try:
                pwd = getpass("请输入您的安全密码")
            except(KeyboardInterrupt, SystemExit):
                print("^")
            except:
                pass
            if  pwd == 'zhangpczuishuai':
                return True
            else:
                count+=1
                print("您可能苏措了密码哈")
        print("密码输入错误超过3次")
        return False

    def show(self):
        print("1,2,3,4,5,6,7,8,9,0")

    def do_chushihua(self):
        pass
    def do_test(self,line):
        print("<test></test>")
    def do_hello(self,line):
        print ("hello",line)
    def do_ping(self,line):
        os.system("ping -n 1 {0}".format(line))

if __name__ == '__main__':
    try:
        cli = Cli()
        cli.cmdloop()
    except:
        pass