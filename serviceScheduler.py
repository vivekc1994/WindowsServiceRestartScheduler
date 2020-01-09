#Developer - Vivek Chavan (vivek.c1994@gmail.com)

import schedule
import time
import os

	def jobThread():
    		cmd = 'powershell -command "Restart-Service TeamViewer"'
    		os.system(cmd)
   		    print("Service Restarted")


schedule.every(5).seconds.do(Thread)

while True:
	schedule.run_pending()
	

