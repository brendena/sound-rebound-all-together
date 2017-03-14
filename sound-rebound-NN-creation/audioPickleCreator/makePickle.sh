#!/bin/bash
#removing extension http://unix.stackexchange.com/questions/180271/remove-a-specific-extension-from-all-the-files-in-a-directory

#this will convert all mp3 into wav and delete the mp3 files
# convert mp3 to wave
# mpg321 -w "$fileName" "$file"

# convert .m4a to wave
# http://superuser.com/questions/23930/how-to-decode-aac-m4a-audio-files-into-wav

#for file in *.m4a; do
#    
#    if [ "$file" != '*.m4a' ]; then
#	filename="${file%.*}"
#	wavextension=".wav"
#	filename=$filename$wavextension
#	echo "converting " $file
#	echo $filename
#	#avconv -i   "$file"  "$filename"
#	faad -o    "$filename" "$file" 
#	#chmod 777 fingerSnapping.wav
#	#rm $file
#    fi
#done

audioFileName="audioForNeuralNetwork"

#create the audioFileName.pickle
python3 createAudioPickle.py $audioFileName

#then copies it to the proper directory
cp ./$audioFileName.pickle ../NeuralNetwork/$audioFileName.pickle

rm $audioFileName.pickle

