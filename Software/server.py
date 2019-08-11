#Importy thingys
import time

#Variables (There's a lot uwu)
softwareVersion = '0.0.1'
updateAvailable = 'false'
updateVersion = '0.0.2'
firstStart = 'false'
gameVersion = '1.12.0'

#I guess this is the actual display script that users see
def awaitcmd():
    cmd = input(">")
    #answercmd
    if cmd == 'help':
        #help
        print("*****************************************")
        print("**             Server Help             **")
        print("**                                     **")
        print("**                                     **")
        print("**   CMD   -          USAGE            **")
        print("**                                     **")
        print("** help    - Shows this page           **")
        print("** plugins - List Server Plugins       **")
        print("** stop    - Stops the server          **")
        print("** version - Gives version Information **")
        print("*****************************************")
        awaitcmd()
    elif cmd == 'plugins':
        print("Plugins (0): ")
        print("Plugin missing or not working? Check it's dependinces and that it's on the right version ({})".format(softwareVersion))
        awaitcmd()
    elif cmd == 'stop':
        #Stop
        print("**************************************************")
        print("Server Shutting Down :(")
        print("Closing all connections and addons then quitting")
        print("Goodbye cruel world")
        print("**************************************************")
        exit()
    elif cmd == 'version':
        print("Running Version {}".format(softwareVersion))
        print("Found a bug? Got an issue? Suggestion?")
        print("http://hammy.xyz/discord")
        awaitcmd()
    else:
        print("Unknown Command :(")
        print("List all commands with the 'help' command")
        awaitcmd()


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

    #Check Update
    if updateAvailable == 'true':
        print("*************************************************")
        print("**           WARN: Update Available            **")
        print("** For Security Reasons I recommend you update **")
        print("**   THIS WILL NOT AFFECT YOUR GAME VERSION    **")
        print("**        http://hammy.xyz/go/mcupdate         **")
        print("*************************************************")
        print("*************************************************")
        print("**           WARN: Update Available            **")
        print("** For Security Reasons I recommend you update **")
        print("**   THIS WILL NOT AFFECT YOUR GAME VERSION    **")
        print("**        http://hammy.xyz/go/mcupdate         **")
        print("*************************************************")
        print("*************************************************")
        print("**           WARN: Update Available            **")
        print("** For Security Reasons I recommend you update **")
        print("**   THIS WILL NOT AFFECT YOUR GAME VERSION    **")
        print("**        http://hammy.xyz/go/mcupdate         **")
        print("*************************************************")
        print("")
    else:
        print("Server Version up to date!")
        print("Continuing with Startup!")
        print("")

    #Check First Start, if true, run setup
    if firstStart == 'true':
        print("**************************************")
        print("**  Welcome to the Server Setup!    **")
        print("**  You only have to do this once   **")
        print("**  However if you wish,  you can   **")
        print("**  Repeat this setup at any time   **")
        print("** By running the FULLRESET command **")
        print("**        from this console!        **")
        print("**                                  **")
        print("**           Lets Start!            **")
        print("**************************************")

        print("")
        print("NOTE: PLEASE DO NOT CHANGE VARIABLES FROM THE PYTHON FILE MANUALLY, PLEASE RUN 'FULLRESET' OR 'CHANGESETTING' COMMANDS FROM THE CONSOLE. CHANGING IN FILE MAY MAKE SOME ERRORS OCCUR IN GAME")
        print("")

        #Setup
        print("")
        print("First, an easy one, please enter your XboxLive username")
        topadmin = input("")

        print("Great! Welcome {} to your Minecraft Server!".format(topadmin))
        print("{} is now considered the topadmin".format(topadmin))
        print("Read more about topadmin's here: http://hammy.xyz/go/mctopadmin")
        print("{} has now been given all operator permissions and top role by default".format(topadmin))

        print("Okay so now let's move on to the actual server!")

        print("Frick! I almost forgot! My name is MBot, the server helper, also the built in AntiCheat! Basically I'm very cool and will always be here to help you!")
        print("************************")

        print("")
        print("Server Setup:")
        print("First off, lets talk the basics, I'll ask a question and you'll answer it!")

        print("What would you like to call the server? (Max 32 Characters)")
        serverName = input("")

        print("Very very good, let's continue setting up {}".format(serverName))

        print("What do you want the default Gamemode to be? (CREATIVE, SURVIVAL, ADVENTURE)")
        defaultGamemode = input("")

        print("Great! Now what local IP do you want the server to run on?")
        print("Note: if you don't know, just click enter and I'll try localhost")
        localIp = input("")
        #adjust localIp
        if localIp == '':
            localIp = 'localhost'
        else:
            print("Changing localIp from localhost to {}".format(localIp))

        print("Cool, okay, so, uhhhh, oh right, server port (default is 19132)")
        print("Enter Server Port (leave blank for default)")
        port = input("")
        #adjust serverport
        if port == '':
            port = '19132'
        else:
            print("Changing Server Port from 19132 to {}".format(port))

        print("!!! The Fun y/n Section !!!")
        print("I ask you yes or no questions, you answer with y (yes) or n (no)")
        print("Ready?")
        print("Go!")

        print("***Toggling Server Settings***")
        print("")

        print("Do you want to announce player advancements?*")
        print("*look, i know they used to be achivements, i still call them achivements but Mojang changed them, i feel it's easier to comply and complain rather than comply and get a migraine")
        print("")
        print("            ewwww i made it rhyme i hate myself")
        print("")
        print("y - yes please, announce them advancements")
        print("n - no, keep it to yourself")
        announceAdvancements = input("")
        print("")

        print("Auto Updates")
        print("Do you wish to always update to the latest game version when available (I 100% recommend this as most players update within the first 2 days)")

        print("Do you wish to have a whitelist on initial startup? This means only {} can join on first start. This allows for more in game startup. More info: http://hammy.xyz/go/mcwhitelist".format(topadmin))
        whitelist = input("")

        print("Do you wish to allow non-XboxLive users? I recommend answering n to this because it makes for easier configuration.")
        nonxbl = input("")

        print("Do you wish to use the default op system. (I REALLY suggest you answer n and let MinecraftJr handle the perms and not Minecraft)")
        legacyPerms = input("")

        print("Okay so now I believe we have world generation settings. One second as I reload the script")

        print("Okay here we go...")
        print("")
        print("INITIAL WORLD GENERATION:")
        print("")
        print("World Type? | Superflat, Normal, Old")
        worldType = input("")

        print("Generation Seed? | Put 0 for random :)")
        seed = input("")

        print("Huh that easy? Okay then lets move on, next on this list is the fun stuff!!!")

        print("Let's bring her life!")
        print("Server 'Message of the Day'(MOTD)")
        print("We support colour codes/formatting codes using the & symbol! http://hammy.xyz/go/mcformatting")
        motd = input("")
        print("")

        print("Finally, do you want to have a custom 'server software' name?")
        print("Some server lists and status checkers display this, so i suggest something like 'Server.net v1.12' however use this however")
        print("Max 24 Characters, Leave blank for 'MinecraftJr'")
        serverSoftware = input("")

        print("Okay we're done")
        print("Well you are")
        print("This is the part where I go configure everything and bring your server life")
        print("After I do this, which normally takes 50-60s, I will ask you for the Maximum RAM you want the server to have access to as well as for you to set a override password")

        print("***********************************")
        print("*      HELL YEAH IT WORKS!!!      *")
        print("***********************************")
        print("Please enter the maximum amount of ram in MB (MUST BE ABOVE 500!!!)")
        print("For recommended server specs, see http://hammy.xyz/go/mcspecs")
        mxm = input("")

        print("Finally, I ask you enter an override password, this will give you access to commands like FULLRESET, only share with your most trusted!!!")
        overridePassword = input("")
        print("Encrypting, Please wait")

        print("")
        print("")
        print("")
        print("Okay, now I have one more request for you, please type 'stop' in the command field, and then restart the server.py script, this will boot your server")
        print("Also have a look at http://hammy.xyz/go/mcconfig for more configuration tools, tips and tricks!")
        endStartup = input(">")
        #Check stop command
        if endStartup == "stop":
            print("**************************************************")
            print("Server Shutting Down :(")
            print("Closing all connections and addons then quitting")
            print("Goodbye cruel world")
            print("**************************************************")
            exit()
        else:
            print("Unknown Command :(")
            endStartup = input(">")

    else:
        print("Starting the Server!")
        awaitcmd()

startup()
