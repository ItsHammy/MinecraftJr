chat = open("chat.yml", "a")
chat.write("#\n#  __  __  _____     _ _____     _____ _           _\n# |  \/  |/ ____|   | |  __ \   / ____| |         | |\n# | \  / | |        | | |__) | | |    | |__   __ _| |_\n# | |\/| | |    _   | |  _  /  | |    | '_ \ / _` | __|\n# | |  | | |___| |__| | | \ \  | |____| | | | (_| | |_\n# |_|  |_|\_____\____/|_|  \_\  \_____|_| |_|\__,_|\__|\n#\n# TO USE THIS, PLEASE MAKE SURE mcjr-chat IS SET TO true IN options.yml\n# TO USE THIS, PLEASE MAKE SURE mcjr-chat IS SET TO true IN options.yml\n# TO USE THIS, PLEASE MAKE SURE mcjr-chat IS SET TO true IN options.yml\n# TO USE THIS, PLEASE MAKE SURE mcjr-chat IS SET TO true IN options.yml\n\n#Placeholders: %player%, %unique%, %online%, %rank%\n\n#Messages\nmessages:\n  first-join: '&bWelcome %player%, &bto the server! Member Number: &d%Unique!%'\n  join-msg: '&7[&a+&7] &b%player%'\n  leave-msg: '&7[&4-&7] &b%player%'\n  #MOTD is in MOTD.txt\n  motd-on-join: true\n\n#Chat Format:\n\n\n#AutoMessage Settings\nautomessage:\n  enabled: true\n  #If true, players must either be opped or have mcjr.automessage.see\n  requireperm: true\n  #Interval in seconds\n  interval: 90\n  #Messages in order\n  messages:\n    - 'Hi, welcome to my server'\n    - 'Running MinecraftJr by hammy.xyz/minecraft'\n    - '&bOh yeah! &d&lFormatting works too'\n    - 'Hi, welcome to my server'\n    - 'Running MinecraftJr by hammy.xyz/minecraft'\n    - '&bOh yeah! &d&lFormatting works too'")
chat.close()
print("Generated chat.yml")

motd = open("motd.txt", "a")
motd.write("&7&m-----------------------------------\n              &5hammy&8.xyz\n        &6&oWelcome to the server!\n&7&m-----------------------------------")
motd.close()
print("Generated motd.txt")
