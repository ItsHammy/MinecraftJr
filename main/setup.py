from time import sleep, time

#SETUP Script!
def awaitend():
    endcmd = input(">")
    if endcmd == 'save':
        print("**************************************************")
        print("Server Starting!!!")
        print("This could take a while")
        print("Please wait")
        print("**************************************************")
        sleep(20)
    else:
        print("An error occured, please try again!")
        awaitend()

print("**************************************")
print("**  Welcome to the Server Setup!    **")
print("**  You only have to do this once   **")
print("**  However if you wish,  you can   **")
print("**  Repeat this setup at any time   **")
print("**  By running 'FULLRESET' in this  **")
print("**             terminal.            **")
print("**                                  **")
print("**           Lets Start!            **")
print("**************************************")
print("")
print("There may be some delay as I change things around, please do not exit. | If you do, or I crash, read this: http://hammy.xyz/go/mcsetupcrash")
print("")
sleep(5)
#Generate Files (FUN!)

#Setup
print("")
print("First, an easy one, please enter your XboxLive username")
topadmin = input(">")
sleep(1)
print("Great! Welcome {} to your Minecraft Server!".format(topadmin))
print("{} is now considered the topadmin".format(topadmin))
print("Read more about topadmin's here: http://hammy.xyz/go/mctopadmin")
print("{} has now been given all operator permissions and top role by default".format(topadmin))
sleep(1)
print("Okay so now let's move on to the actual server!")
sleep(1)
print("Frick! I almost forgot! My name is MBot, the server helper, also the built in AntiCheat! Basically I'm very cool and will always be here to help you!")
sleep(1)
print("************************")
sleep(4)
print("")
print("Server Setup:")
print("First off, lets talk the basics, I'll ask a question and you'll answer it!")
sleep(1)
print("What would you like to call the server? (Max 32 Characters)")
serverName = input(">")
sleep(1)
print("Very very good, let's continue setting up {}".format(serverName))
sleep(1)
print("What do you want the default Gamemode to be? (CREATIVE, SURVIVAL, ADVENTURE)")
gamemode = input(">")
print("Cool, okay, so, uhhhh, oh right, server port (default is 19132)")
print("Enter Server Port (leave blank for default)")
port = input(">")
#adjust serverport
if port == '':
    port = '19132'
else:
    print("Changing Server Port from 19132 to {}".format(port))
sleep(3)
print("!!! The Fun y/n Section !!!")
print("I ask you yes or no questions, you answer with y (yes) or n (no)")
print("Ready?")
print("Go!")
sleep(1)
print("***Toggling Server Settings***")
print("")
sleep(1)
print("Do you want to announce player advancements?*")
print("*look, i know they used to be achivements, i still call them achivements but Mojang changed them, i feel it's easier to comply and complain rather than comply and get a migraine")
print("")
print("            ewwww i made it rhyme i hate myself")
print("")
print("y - yes please, announce them advancements")
print("n - no, keep it to yourself")
announceAdvancements = input(">")
print("")
sleep(1)
print("Auto Updates")
print("Do you wish to always update to the latest game version when available (I 100% recommend this as most players update within the first 2 days)")
autoUpdate = input(">")
sleep(1)
print("Do you wish to have a whitelist on initial startup? This means only {} can join on first start. This allows for more in game startup. More info: http://hammy.xyz/go/mcwhitelist".format(topadmin))
whitelist = input(">")
sleep(1)
print("Do you wish to allow non-XboxLive users? I recommend answering n to this because it makes for easier configuration.")
nonxbl = input(">")
sleep(1)
print("Do you wish to use the default op system. (I REALLY suggest you answer n and let MinecraftJr handle the perms and not Minecraft)")
legacyPerms = input(">")
sleep(1)
print("Okay so now I believe we have world generation settings. One second as I reload the script")
sleep(1)
print("Okay here we go...")
print("")
print("INITIAL WORLD GENERATION:")
print("")
print("World Type? | Superflat, Normal, Old")
worldType = input(">")
sleep(1)
print("Generation Seed? | Put 0 for random :)")
seed = input(">")
sleep(1)
print("Huh that easy? Okay then lets move on, next on this list is the fun stuff!!!")
sleep(1)
print("Let's bring her life!")
print("Server 'Message of the Day'(MOTD)")
print("We support colour codes/formatting codes using the & symbol! http://hammy.xyz/go/mcformatting")
motd = input(">")
print("")
sleep(1)
print("Finally, do you want to have a custom 'server software' name?")
print("Some server lists and status checkers display this, so i suggest something like 'Server.net v1.12' however use this however")
print("Max 24 Characters, Leave blank for 'MinecraftJr'")
serverSoftware = input(">")
sleep(1)
print("Okay we're done")
print("Well you are")
print("This is the part where I go configure everything and bring your server life")
print("After I do this, which normally takes 50-60s, I will ask you for the Maximum RAM you want the server to have access to")
print("")
print("")
print("Please wait (Time Remaining: ~55s)")
sleep(25)
print("Please wait (Time Remaining: ~30s)")
sleep(30)
print("***********************************")
print("*      HELL YEAH IT WORKS!!!      *")
print("***********************************")
print("")
sleep(5)
print("Please enter the maximum amount of ram in MB (MUST BE ABOVE 500!!!)")
print("For recommended server specs, see http://hammy.xyz/go/mcspecs")
mxm = input(">")
sleep(6)
print("")
print(".")
sleep(1)
print("..")
sleep(1)
print("...")
sleep(1)
print(".")
sleep(1)
print("..")
sleep(1)
print("...")
sleep(15)
print("")
print("********************************************")
print(" FIRST START SETTINGS:")
print(" Settings for {}".format(serverName))
print(" {}".format(motd))
print("")
print(" Port: {}".format(port))
print(" Gamemode: {}".format(gamemode))
print(" World: {},{}".format(worldType, seed))
print("********************************************")
print("")
print("Please wait...")
print("")
sleep(15)
print("Okay, now I have one more request for you, please type 'save' in the command field, The entire script will then restart and boot your server!!!")
print("Also have a look at http://hammy.xyz/go/mcconfig for more configuration tools, tips and tricks!")
awaitend()