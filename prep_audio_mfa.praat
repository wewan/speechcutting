# prep_audio_mfa.praat
# Written by E. Chodroff
# Oct 23 2018
# extract left channel and resample to 16 kHz for all wav files in a directory

### CHANGE ME! 
# don't forget the slash at the end of the path
main_dir$ = "C:\Users\axelb\Data Folders\MSc Thesis\data\input_video\"
###

Create Strings as directory list: "speakers", main_dir$
nSpeakers = Get number of strings

for j from 1 to nSpeakers
	selectObject: "Strings speakers"
	speaker$ = Get string: j
	dir$ = main_dir$ + speaker$ + "\"

	Create Strings as file list: "files", dir$ + "*.wav"
	nFiles = Get number of strings

	for i from 1 to nFiles
		# read in WAV file
		selectObject: "Strings files"
		filename$ = Get string: i
		Read from file: dir$ + filename$

		# extract left channel
		Extract one channel: 1

		# resample to 16kHz with 50 point precision (default)
		Resample: 16000, 50

		# save WAV file
		Save as WAV file: dir$ + filename$

		# clean up
		select all
		minusObject: "Strings files"
		Remove
	endfor