# Importy thingys
from time import sleep, time

# Testing Variables (There's a lot uwu)
softwareVersion = '0.0.1'
updateAvailable = 'false'
updateVersion = '0.0.2'
firstStart = 'false'
gameVersion = '1.12.0'
playersOnline = '34'
playersMax = '150'
tps = '19.97'

# Working Variables

def awaitcmd():
    import main

###################################################
def startup():
    print("")
    print("*************************************")
    print("***  MinecraftJr Server Software  ***")
    print("*** Created & Maintained by Hammy ***")
    print("***  http://hammy.xyz/minecraft   ***")
    print("***      100% Open Source!        ***")
    print("*************************************")
    print("***        Version: 0.0.1         ***")
    print("*************************************")
    print("")
    sleep(5)
    #Check Update
    if updateAvailable == 'true':
        print("*************************************************")
        print("**           WARN: Update Available            **")
        print("** For Security Reasons I recommend you update **")
        print("**   THIS WILL NOT AFFECT YOUR GAME VERSION    **")
        print("**        http://hammy.xyz/go/mcupdate         **")
        print("*************************************************")
        sleep(2)
        print("*************************************************")
        print("**           WARN: Update Available            **")
        print("** For Security Reasons I recommend you update **")
        print("**   THIS WILL NOT AFFECT YOUR GAME VERSION    **")
        print("**        http://hammy.xyz/go/mcupdate         **")
        print("*************************************************")
        sleep(2)
        print("*************************************************")
        print("**           WARN: Update Available            **")
        print("** For Security Reasons I recommend you update **")
        print("**   THIS WILL NOT AFFECT YOUR GAME VERSION    **")
        print("**        http://hammy.xyz/go/mcupdate         **")
        print("*************************************************")
        sleep(2)
        print("")
    else:
        print("Server Version up to date!")
        print("Continuing with Startup!")
        print("")

    #Check First Start, if true, run setup
    if firstStart == 'true':
        sleep(3)
        import setup
        print("Done!")
        sleep(1)
        awaitcmd()

    else:
        sleep(3)
        print("Starting the Server!")
        awaitcmd()

startup()
