import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from client_scripts.codejam_admin_cmd import CodejamAdminCmd

if __name__ == '__main__':
    prompt = CodejamAdminCmd()
    prompt.cmdloop()
