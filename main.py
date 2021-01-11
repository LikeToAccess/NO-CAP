# -*- coding: utf-8 -*-
# filename          : main.py
# description       : No FPS cap for MCBE
# author            : LikeToAccess
# email             : liketoaccess@protonmail.com
# date              : 01-10-2021
# version           : v1.0
# usage             : "NO CAP.exe" [vsync value] [framecap value]
# notes             : For Windows 10, works on any Minecraft version, if no parameters are given vsync and framecap are set to 0
# license           : MIT
# py version        : 3.7.8 (must run on 3.6 or higher)
#==============================================================================
import os
import sys

args = sys.argv
if len(args) > 1:
	vsync = args[1]
	if len(args) == 3:
		max_framerate = args[2]
	else:
		max_framerate = 0
else:
	vsync = 0
	max_framerate = 0

path = os.getcwd()
with open("grab.cmd", "w") as file:
	file.write("cd \"%appdata%/../Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/LocalState/games/com.mojang/minecraftpe\"\ncopy options.txt %1\\options.txt\ncd %1")
os.system(f"grab.cmd {path}")
os.remove("grab.cmd")

with open("options.txt", "r") as file:
	lines = file.read().split("\n")

new_lines = []
for line in lines:
	if "gfx_vsync:" in line:
		line = f"gfx_vsync:{vsync}"
	elif "gfx_max_framerate:" in line:
		line = f"gfx_max_framerate:{max_framerate}"
	new_lines.append(line)

with open("options.txt", "w") as file:
	lines = "\n".join(new_lines)
	file.write(lines)

with open("send.cmd", "w") as file:
	file.write("cd \"%appdata%/../Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/LocalState/games/com.mojang/minecraftpe\"\ncopy %1\\options.txt options.txt\ncd %1")
os.system(f"send.cmd {path}")
os.remove("send.cmd")
os.remove("options.txt")
