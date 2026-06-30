# ios6-autobypass
Python script for semi-automated icloud lock bypass on iOS 6

## Friendly reminder
__Linux is not supported for now. Fixes incoming! Use macOS if you can__

__Feel free to report any bugs! This is my first project of this kind__

_As for now, my tool does not support devices running coolbooter. For some reason i don't have any suitable devices. I'll try to make bypass for coolbooter too, but not now. **Sorry for that**_

## What this tool does?
This tool makes process of icloud bypass on iOS 6 _a little bit easier._ You still need Legacy iOS kit to enter ssh ramdisk to proceed with bypass

It's based on icloud bypass instruction found on web, and just automates only this part. You no longer need to manually mount partitions, copy patched lockdownd and chmod this lockdownd :D

## Why you need this tool?
As for me and my friend, we have a bunch of locked iPhones 4/4S or iPads 2. And it's pretty boring to do bypass process manually. So, it's much more easier when you can just run one script and bypass will be done

## How to use?
First of all, you MUST have three things installed:
1. Python3
2. [Legacy iOS Kit](https://github.com/LukeZGD/Legacy-iOS-Kit/releases/tag/latest)
3. ~~Any linux distro~~ or macOS (it must be higher than 10.11 because of legacy kit and python3 support)

When you got all things prepaired you can start bypass process. I won't describe process of entering SSH Ramdisk, you can get all info on Legacy iOS Kit wiki.
After you entered ssh ramdisk you just need to run my script:
`python3 main.py` OR `python main.py` if python3 is your main version

## Supported devices
Technically, this tool supports any device that can run iOS 6 natively. _Coolbooter variant will be soon_ :D

## Credits
[LukeZGD](https://github.com/LukeZGD) creator of [Legacy iOS Kit](https://github.com/LukeZGD/Legacy-iOS-Kit/)

[Darwin and Linux sshpass binaries](https://sshpass.com/)

[Patched lockdownd](https://github.com/iPh0ne4s/iOS-5-6-Hacktivation) bypass instruction from there too

## Special thanks
Special thanks for my friend that gave me this idea, and __huge thanks to LukeZGD, creator of Legacy iOS Kit.__
