# -*- coding: utf-8 -*-
import os, sys

print ("\033[1;32mMasukin Username dan Passwordnya!")
print ("\033[1;31;1mGa Tau? Contact Admin For WhatsApp")
print ("╭─MrDebo")
print ("╰─•> 081539279932")
Username = 'Buis'
Password = 'Paksu'

def restart():
        ngulang = sys.executable
        os.execl(ngulang, ngulang, *sys.argv)

def main():
        uname = raw_input("Username : ")
        if uname == Username:
                pwd = raw_input("Password : ")

                if pwd == Password:
                        sys.exit()

                else:
                        print "\n\033[1;36mPassword Salah!\033[00m"
                        print "Isi Yang Benar!\n"
                        restart()
        else:
                print "\n\033[1;36mUsername Salah!\033[00m"
                print "Isi Yang Benar!\n"
                restart()

try:
        main()
except KeyboardInterrupt:
        os.system('clear')
        restart()
