import os
import os.path
import subprocess
import platform

current_os = platform.system().lower()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if current_os == "darwin":
	SSHPASS_PATH = os.path.join(BASE_DIR, "bin", "darwin", "sshpass")
elif current_os == "linux":
	SSHPASS_PATH = os.path.join(BASE_DIR, "bin", "linux", "sshpass")
else:
	print("System is not supported!")
os.chmod(SSHPASS_PATH, 0o755)
# print(SSHPASS_PATH)
# Defining platform and sshpass

mount = [SSHPASS_PATH,
		"-p", "alpine",
		"ssh", "-o", "HostKeyAlgorithms=+ssh-rsa,ssh-dss", "-o", "PubkeyAcceptedKeyTypes=+ssh-rsa", "-p", "6414",
		"root@127.0.0.1",
		"mount.sh"
]
mount_result = subprocess.run(mount, capture_output=True, text=True)
# print(mount_result)
if mount_result.returncode == 0:
    print("Successfully mounted!")
else:
    print(f"Error: {mount_result.stderr}")
# Mounting device partitions

change = [SSHPASS_PATH,
		"-p", "alpine",
		"scp", "-o", "HostKeyAlgorithms=+ssh-rsa,ssh-dss", "-o", "PubkeyAcceptedKeyTypes=+ssh-rsa","-P","6414",
		"lockdownd",
		"root@127.0.0.1:/mnt1/usr/libexec/lockdownd"
]
change_result = subprocess.run(change, cwd=BASE_DIR, capture_output=True, text=True)
# print(change_result)
if change_result.returncode == 0:
    print("Successfully changed!")
else:
    print(f"Error: {change_result.stderr}")
# Moving lockdownd from PC to device

chmod = [SSHPASS_PATH,
		"-p", "alpine",
		"ssh", "-o", "HostKeyAlgorithms=+ssh-rsa,ssh-dss", "-o", "PubkeyAcceptedKeyTypes=+ssh-rsa", "-p", "6414",
		"root@127.0.0.1",
		"chmod 0755 /mnt1/usr/libexec/lockdownd"
]
chmod_result = subprocess.run(chmod, capture_output=True, text=True)
# print(chmod_result)
if chmod_result.returncode == 0:
    print("Successfully chmoded!")
else:
    print(f"Error: {chmod_result.stderr}")
# Making lockdownd executable

reboot = [SSHPASS_PATH,
		"-p", "alpine",
		"ssh", "-o", "HostKeyAlgorithms=+ssh-rsa,ssh-dss", "-o", "PubkeyAcceptedKeyTypes=+ssh-rsa", "-p", "6414",
		"root@127.0.0.1",
		"reboot_bak"
]
reboot_result = subprocess.run(reboot, capture_output=True, text=True)
# print(reboot_result)
if reboot_result.returncode == 0:
    print("Successfully reboot!")
else:
    print(f"Error: {reboot_result.stderr}")
# Rebooting :) Congrats!