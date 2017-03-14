
# sound-rebound creative-matrix mic code#


Starting Point for this code was from [here](https://github.com/matrix-io/matrix-creator-alexa-voice-demo)

technical description [here](https://github.com/brendena/sound-rebound-matrix-creator/blob/master/howThisWorks.md)

## install pip dependencies
### there currently arn't any.  But there will be.
sudo pip install -r requirements.txt


## build micarray
cd ./micarray
sudo bash ./make.sh

## sync data

rsync -avz -e ssh username@10.42.0.1:/home/brendena/Downloads/syncRPI ~/Downloads/syncRPI

## include c++ library
[Libmfcc](https://github.com/wirahayy/libmfcc)
