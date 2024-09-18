# pyNDI Made by CarlosFdez
# Example by Joel Luther-Braun / Github(@Hantoo)

#pyNDI Import
import finder
import receiver
import lib
#Other Import
import cv2
import imutils
import subprocess
find = finder.create_ndi_finder()
NDIsources = find.get_sources()

recieveSource = None; 
processes=[]
for idx,src in enumerate(NDIsources):
	cmd=["python","view.py","-s",str(idx)]
	process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	processes.append(process)

for process in processes:
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        print("成功:", stdout.decode())
    else:
        print("エラー:", stderr.decode())

