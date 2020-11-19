'''
Author  : Luci MadMax
Version : 1.1a

This is Grub-Boot  Repair Tools
Seaf And Easy Way to Repair Grub Boot Loder
This is Alpah Version ...

'''

import subprocess as __SUB__
import re as __RE__
from time import sleep as __sp__
from os import geteuid as __EUID__
from os import _exit   as __Quit__
class Repair:

    def __init__(self):
        self.__CW = '\033[37;1m'
        self.__CR = '\033[00m'
        self.__CG = '\033[32;1m'

    def Check_Disk(self):
        try:
            if __EUID__() == 0:
                self.__CommandOutPut = __SUB__.check_output(['fdisk','-l']).decode()
                self.__GrubDrive = __RE__.findall(r'/[a-z]*/[a-z]*:',self.__CommandOutPut)[0].replace(':','')
                if self.__GrubDrive:
                    print(f"{self.__CW}* Found Grub-Installed Drive:{self.__CG} {self.__GrubDrive}\n")
                    __sp__(0.5)
                if self.__GrubDrive:
                    self.__DriveName = __RE__.findall(r'.*Linux.*',self.__CommandOutPut)
                    if 'swap' not in self.__DriveName[0] and len(self.__DriveName) > 0:
                        self.__linuxDrive = __RE__.findall(r'/dev.[a-zA-Z0-9]*',self.__DriveName[0])[0]
                        print(f"{self.__CW}* Found Installed Linux Drive:{self.__CG} {self.__linuxDrive}\n\033[00m")
                        __sp__(0.5)
                        return self.__GrubDrive,self.__linuxDrive

                else:
                    __Quit__(0)
            print(f'\033[31;1m\n\t\tRun As Root !\n\033[00m')
        except:
            print("\n\033[37;1m* \033[31;1mLinux Drive Not Found Maybe You Deleted Linux Drive Accidently!\n")
            __Quit__(0)

    def __Access_old_os(self,Drives):
        self.__MountDrive = Drives[1]
        self.__GrubDrive  = Drives[0]
        # Start TO Process Recover Grub Boot #
        print(f"{self.__CW}* Starting Accesss OS",end='')
        __SUB__.call(['mount',self.__MountDrive,'/mnt']);__sp__(0.5)
        __SUB__.call(['mount','-B','/dev','/mnt/dev']);__sp__(0.5)
        __SUB__.call(['mount','-B','/dev/pts','/mnt/dev/pts']);__sp__(0.5)
        __SUB__.call(['mount','-B','/proc','/mnt/proc']);__sp__(0.5)
        __SUB__.call(['mount','-B','/sys','/mnt/sys']);__sp__(0.5)
        __SUB__.call([f"echo 'os-prober && grub-install {self.__GrubDrive} && update-initramfs -u && update-grub '|chroot /mnt"],shell=True)
        __SUB__.call(['umount','/mnt/sys'])
        __SUB__.call(['umount','/mnt/proc'])
        __SUB__.call(['umount','/mnt/dev/pts'])
        __SUB__.call(['umount','/mnt/dev'])
        __SUB__.call(['umount','/mnt'])
        __SUB__.call(['clear'])
        print(f"""\033[32;1m
╔═╗╦═╗╦ ╦╔╗    ╔╗ ┌─┐┌─┐┌┬┐  ╦═╗┬─┐┌─┐┌─┐┬┬─┐┌─┐┌┬┐
║ ╦╠╦╝║ ║╠╩╗───╠╩╗│ ││ │ │   ╠╦╝├┬┘├─┘├─┤│├┬┘├┤  ││
╚═╝╩╚═╚═╝╚═╝   ╚═╝└─┘└─┘ ┴   ╩╚═┴└─┴  ┴ ┴┴┴└─└─┘─┴┘
""")
    def Action(self):
        print("""\033[32;1m
╔═╗╦═╗╦ ╦╔╗    ╔╗ ┌─┐┌─┐┌┬┐\033[33;1m
║ ╦╠╦╝║ ║╠╩╗───╠╩╗│ ││ │ │ \033[37;1m
╚═╝╩╚═╚═╝╚═╝   ╚═╝└─┘└─┘ ┴ \033[32;1m
    ╦═╗┌─┐┌─┐┌─┐┬┬─┐       \033[33;1m
    ╠╦╝├┤ ├─┘├─┤│├┬┘       \033[37;1m
    ╩╚═└─┘┴  ┴ ┴┴┴└─       

Author \033[33;1m: \033[32;1mLuci MadMax\033[37;1m
Versino\033[33;1m: \033[32;1m1.1a\033[37;1m
""")
        self.__Access_old_os(self.Check_Disk())
        print(f"{self.__CW}\n* Successfull To Repair......\n")


if __name__ == '__main__':
    if __EUID__() == 0:
        x = Repair()
        x.Action()
    else:
        print(f'\033[31;1m\n\tRun As Root User\n\n')
        __Quit__(0)


