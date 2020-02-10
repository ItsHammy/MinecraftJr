#Import Everything
from time import sleep, time

# Testing Variables (There's a lot uwu)
softwareVersion = '0.0.3'
updateAvailable = 'false'
updateVersion = '0.0.4'
firstStart = 'false'
gameVersion = '1.14.20'
playersOnline = '34'
playersMax = '150'
tps = '19.97'
usePerms = 'true'

# Working Variables



def statusBox():
    print("**************************************************")
    print("**************** Server Status: ******************")
    print("***                                            ")
    print("***                                            ")
    print("*** Online: {}/{}       ".format(playersOnline, playersMax))
    print("*** Game Version: {}                ".format(gameVersion))
    print("*** TPS: {} (Feels like 20!)                   ".format(tps))
    print("***                                            ")
    print("*** Found an Error? http://hammy.xyz/discord   ")
    print("***                                            ")
    print("**************************************************")

def awaitcmd():
    cmd = input(">".lower())
    #answercmd
    if cmd == 'help':
        #help
        print("***********************************************")
        print("**               Server Help                 **")
        print("**                                           **")
        print("**                                           **")
        print("**   CMD     -          USAGE                **")
        print("**                                           **")
        print("** crashnow   - Forcibly Crash the Server    **")
        print("** fullreset - RESET EVERYTHING (WARN)       **")
        print("** gc        - Server Information            **")
        print("** gm        - Change Gamemode               **")
        print("** help      - Shows this page               **")
        print("** op        - Give a player Operator Status **")
        print("** plugins   - List Server Plugins           **")
        print("** saveall   - Save the game data            **")
        print("** stop      - Stops the server              **")
        print("** version   - Gives version Information     **")
        print("***********************************************")
        awaitcmd()
    elif cmd == 'plugins':
        print("Plugins (0): ")
        print("Plugin missing or not working? Check it's dependinces and that it's on the right version ({})".format(softwareVersion))
        awaitcmd()
    elif cmd == 'saveall':
        print("Saving Game State!")
        awaitcmd()
    elif cmd == 'gc':
        statusBox()
        awaitcmd()
    elif cmd == 'stop':
        #Stop
        import stop
    elif cmd == 'version':
        print("")
        print("********************************************")
        print("Running Version {}".format(softwareVersion))
        print("Found a bug? Got an issue? Suggestion?")
        print("http://hammy.xyz/discord")
        print("********************************************")
        print("")
        awaitcmd()
    elif cmd == 'op':
        print("Please Enter XboxLive Username of New Operator")
        newOp = input(">")
        print("Making Changes")
        print("[Server] Made {} a server Operator".format(newOp))
        print("Saved all changes!")
        awaitcmd()
    elif cmd == 'crashnow':
        print("Please type 'acceptcrash' to activate an immediate crash of the server.")
        print("Crashing the server will result in all data since last save being lost.")
        crashVerify = input(">")
        if crashVerify == 'acceptcrash':
            print("fine")
            sleep(5)
            exit()
        else:
            print("Verification Failed, Ignoring Request")
            awaitcmd()
    elif cmd == 'fullreset':
        print("Please enter the command again to verify you want to do this")
        fresetVerify = input(">")
        if fresetVerify == 'fullreset':
            import setup
            awaitcmd()
        else:
            print("Verification Failed, Ignoring Request")
            awaitcmd()
    elif cmd == 'gm':
        print("Please Enter XboxLive Username of User or enter 'ALL' for all users")
        gmAdjustUser = input(">")
        print("Please select gamemode you wish to change into | c, a, s,")
        gmAdjustMode = input(">")
        if gmAdjustMode == 'c':
            gmAdjust = 'CREATIVE'
            print("Updating Gamemode for {} to {}".format(gmAdjustUser, gmAdjust))
            awaitcmd()
        elif gmAdjustMode == 's':
            gmAdjust = 'SURVIVAL'
            print("Updating Gamemode for {} to {}".format(gmAdjustUser, gmAdjust))
            awaitcmd()
        elif gmAdjustMode == 'a':
            gmAdjust = 'ADVENTURE'
            print("Updating Gamemode for {} to {}".format(gmAdjustUser, gmAdjust))
            awaitcmd()
        else:
            print("Error Finding Gamemode, Aborting GMSwitch!")
            awaitcmd()


        print("Making Changes")
        print("[Server] Made {} a server Operator".format(newOp))
        print("Saved all changes!")
        awaitcmd()
    else:
        print("Unknown Command :(")
        print("List all commands with the 'help' command")
        awaitcmd()



awaitcmd()
