'''
going to convert getAUdio.sh to py
'''

from subprocess import call
import numpy as np
import json
import re
f = open("audioLocation.json")
a = json.loads(f.read())
labelLocation = list(a["labelLocation"])


#call(["ls", "-l"])


'''
seems to work just have to load it into a differnt directory
'''

for video in a["fileLocations"]:
	
	call(["youtube-dl", 
		'--audio-format',
		'wav',  
		'-x', 
		'--audio-quality',
		'0', 
		'-o' + video[0] + '.%(ext)s" ',
		video[1]])
	
	dirLocation = "labels/" + re.sub(r'\d+', '', video[0])
	waveFile = video[0] + ".wav"

	
	call(["mv",waveFile, dirLocation + "/"+waveFile])


