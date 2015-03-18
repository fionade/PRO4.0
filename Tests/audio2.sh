while true
do
	arecord -D plughw:1,0 -d 6 -r 48000 --use-strftime "%v-%Y-%m-%d %H:%M:%S.wav"
done