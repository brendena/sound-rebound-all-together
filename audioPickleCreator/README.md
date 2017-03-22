## Labels
each label type has a location and label number.

you can find the labelLocation in labelLocation.txt

Ex:
    babyCrying 1
    ..........

    So you can find babyCrying has a labelnumber of 1
    and you can find the labels data inside 
    ./labels/babyCrying/__files__

Uses:
    Its going to be used in getAudio to put the right 
    audio file in the in right subdirectory

    Its used in audioPickleClass.py to tell it what label to apply
    to a given filie based on its location.



### quick guide to audacity labeling data
(basic info)[http://manual.audacityteam.org/man/creating_and_selecting_labels.html]

CTRL + B = add label at mark


### virtualBox
The raspberry pie is a 32 bit operating system, so many of the of the 64 bit sklearn 
stuff doesn't not work on 32 bit version.  Also if you do all the compile over on 
32 bit os you don't have t worry about float64 which tensorflow doesn't like.


### tips to sharing virtualbox

(document)[http://stackoverflow.com/questions/26740113/virtualbox-shared-folder-permissions]

Add yourself to the vboxsf group.

Solution 1

Edit the file /etc/group. Look for the line vboxsf:x:999 and add at the end :yourusername

Solution 2

sudo adduser yourusername vboxsf
