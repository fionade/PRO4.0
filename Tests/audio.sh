# http://linuxconfig.org/how-to-test-microphone-with-audio-linux-sound-architecture-alsa
#
# Cant test die recording on the raspi with the microphones, the link above explains how to
# config if it doesnt work automatically. The script generates 10minute (600sec) wave files
# of the standard input in a loop and gives a name with incrementing id and timestamp
#
# Adding conversion from wave to flac saves 50% memory, will try to implement it in the future
#
#
while True
do
	arecord -d 600 -r 48000 --use-strftime "%v-%Y-%m-%d %H:%M:%S.wav" 
done