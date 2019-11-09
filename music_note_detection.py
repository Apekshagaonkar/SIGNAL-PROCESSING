## Mocking Bot - Task 1.1: Note Detection

#  Instructions
#  ------------
#
#  This file contains Main function and note_detect function. Main Function helps you to check your output
#  for practice audio files provided. Do not make any changes in the Main Function.
#  You have to complete only the note_detect function. You can add helper functions but make sure
#  that these functions are called from note_detect function. The final output should be returned
#  from the note_detect function.
#
#  -------------


## Library initialisation

# Import Modules
# related to Audio Processing here
import numpy as np
import math
import wave
import os
import struct
import matplotlib.pyplot as plt



def find_notes(freq):
	detect_note=''
	
	list_notes=[[127.60,134.70,"C3"],[134.71,142.70,"C#3"],[142.71,151.20,'D3'],[151.21,160.20,'Eb3'],[160.21,169.70,'E3'],[169.71,179.80,'F3'],[179.81,165.5,'F#3'], [165.51,201.85,'G3'],[201.86,213.85,'G#3'],[213.86,226.50,'A3'],[226.51,240,'Bb3'],[240.1,254.25,'B3'],[254.25,269.4,"C4"],[269.41,285.45,'C#4'],[285.46,302.4,'D4'],[302.41,320.35,'Eb4'],[302.36,339.4,'E4'],[339.41,359.6,'F4'],[359.61,381.0,'F#4'],[381.1,403.6,'G4'],[403.61,427.6,'G#4'],[427.61,453.1,'A4'],[453.11,480.05,'Bb4'],[480.06,508.6,'B4'],[508.61,538.8,"C5"],[538.81,570.85,'C#5'],[570.86,604.8,'D5'],[604.81,640.8,'Eb5'], [640.81,678.9,'E5'],[678.91,719.25,'F5'],[719.26,762,'F#5'],[762.1,807.3,'G5'],[807.31,855.3,'G#5'],[855.31,906.15,'A5'],[906.16,960.05,'Bb5'],[960.06,1017.4,'B5'],[1017.41,1078,"c6"],[1078.1,1142,'C#6'],[1142.1,1210,'D6'],[1210.1,1282,'Eb6'],[1282.1,1358,'E6'],[1358.1,1438.5,'F6'],[1438.6,1524,'F#6'],[1524.01,1614.5,'G6'],[1614.51,1715.5,'G#6'],[1715.51,1814.5,'A6'],[1814.51,1925.5,'Bb6'],[1925.51,2034.5,'B'],[16,16.99,'C0'],[17,17.99,'C#0'],[18,19,'D0'],[19.01,20.05,'Eb0'],[20.06,22.01,'E0'],[22.01,22.80,'F0'],[22.81,23.99,'F#0'],[24,25,'G0'],[25.01,26.08,'G#0'],[26.09,28.3,'A0'],[28.31,30.00,'Bb0'],[30.01,31.50,'B0'],[31.51,33.50,'C1'],[33.51,35.5,'C#1'],[35.50,37.70,'D1'],[37.01,39.6,'Eb1'],[39.61,42.40,'E1'],[42.41,44.80,'F1'],[44.81,47.50,'F#1'],[47.51,50.50,'G1'],[50.51,53.50,'G#1'],[53.01,56.5,'A1'],[56.51,60.0,'Bb1'],[60.01,63.05,'B1'],[63.51,67.40,'C2'],[67.41,71.3,'C#2'],[71.31,75.6,'D2'],[75.61,79.5,'Eb2'],[79.51,84.50,'E2'],[84.51,89.50,'F2'],[89.51,95.75,'F#2'],[95.78,100.30,'G2'],[100.31,107.50,'G#2'],[107.51,113.0,'A2'],[113.01,119.5,'Bb2'],[119.51,126.50,'B2'],[126.51,134.7,'C3'],[134.71,142.70,'C#3'],[142.71,151.2,'D3'],[151.21,160.2,'Eb3'],[160.21,169.7,'E3'],[169.71,179.8,'F3'],[179.81,190.5,'F#3'],[190.51,201.85,'G3'],[201.86,213.85,'G#3'],[213.86,226.55,'A3'],[226.56,240.00,'Bb3'],[240.01,254.25,'B3'],[2034.5,2155,'C7'],[2155,2283,'C#7'],[2283,2419,'D'],[2419,2563,'Eb'],[2563,2715.5,'E7'],[2715.5,2877,'F7'],[2877,3048,'F#7'],[3048,3229,'G7'],[3229,3421,'G#7'],[3421,3624.5,'A7'],[3624.5,3840,'Bb7'],[3840,4068.5,'B7'],[4068.5,4310.5,'C8'],[4310.5,4567,'C#8'],[4567,4838.5,'D8'],[4838.5,5126,'Eb8'],[5126,5431,'E8'],[5431,5745,'F8'],[5745,6096,'F#8'],[6096,6458.5,'G8'],[6458.5,6842.5,'G#8'],[6842.5,7249.5,'A8'],[7249.5,7680.5,'Bb8'],[7680.5,7800.0,'B8']]
	
	for i in range(108):
		if(list_notes[i][0]<=freq and list_notes[i][1]>=freq):
			detect_note=list_notes[i][2]
			print(detect_note)	
			
	return detect_note
	
def get_samples(audio):
	
	file_length = audio.getnframes()
	#print(file_length)
	sound = np.zeros(file_length)
	for i in range(file_length):
		data = audio.readframes(1)	
		data = struct.unpack("<h", data)
		sound[i] = int(data[0])
		#print(sound[i])
	sound = np.divide(sound, float(2**15))
	
	return	sound
	
def max_value(list):
	imax=0
	for i in range(20000):
		if(list[i]>list[imax]):
			imax=i

	return imax

############################### Your Code Here ##############################################

def note_detect(audio_file):

	#   Instructions
	#   ------------
	#   Input   :   audio_file -- a single test audio_file as input argument
	#   Output  :   Detected_Note -- String corresponding to the Detected Note
	#   Example :   For Audio_1.wav file, Detected_Note = "A4"

	Detected_Note = ""
	
	sound=get_samples(audio_file)
	#plt.plot(sound)
	#plt.show()
	fs=audio_file.getframerate()  #Sampling frequency
	#print(fs)
	transform_array=np.fft.fft(sound)
	n=len(transform_array)
	for i in range(n-1):
		transform_array[i]=abs(transform_array[i])
	#print(n)
	#plt.plot(frequency_array)
	#plt.show()
	#a=np.argsort(frequency_array)
	
	imax=max_value(transform_array)
	
	#print(imax)
	freq=(fs * imax)/n
	
	print("freq",freq)
	Detected_Note=find_notes(freq)
	
	# Add your code here
	#Detected_Note=notes(frequency)
	return Detected_Note


############################### Main Function ##############################################

if __name__ == "__main__":


	# code for checking output for single audio file
	path = os.getcwd()
	
	file_name = path + "\Task_1.1_Audio_files\Audio_1.wav"
	audio_file = wave.open(file_name)

	Detected_Note = note_detect(audio_file)

	print("\n\tDetected Note = " + str(Detected_Note))

	# code for checking output for all audio files
	x = raw_input("\n\tWant to check output for all Audio Files - Y/N: ")
	
	if x == 'Y':

		Detected_Note_list = []

		file_count = len(os.listdir(path + "\Task_1.1_Audio_files"))

		for file_number in range(1, file_count):

			file_name = path + "\Task_1.1_Audio_files\Audio_"+str(file_number)+".wav"
			audio_file = wave.open(file_name)

			Detected_Note = note_detect(audio_file)
			
			Detected_Note_list.append(Detected_Note)

		print("\n\tDetected Notes = " + str(Detected_Note_list))
	