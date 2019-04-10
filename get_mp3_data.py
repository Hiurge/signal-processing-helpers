
from __future__ import unicode_literals
from sys import argv
import os

import mutagen

import pandas as pd
from pydub import AudioSegment

def get_mp3_data():
	''' 
	Terminal:
	example -> 'python get_mp3_data.py music'
	Run     -> 'python get_mp3_data.py ARG'
	ARG     ->  YOUR_MP3_FOLDER.txt
	'''

	# Wat u look for
	dtypes = ['Name', 'Hz', 'Time', 'rms', 'dBFS','amax' ]

	# Helper
	def abspath(name): return os.path.abspath(name)

	# Get folder wit music
	mp3_dir_path = abspath(argv[1])
	mp3_files = os.listdir(mp3_dir_path)

	SAMPLES_DATA = {}
	for sample_name in mp3_files:
		sample_path =  abspath(argv[1] + '/' + sample_name)
		sample = AudioSegment.from_mp3(sample_path)
		mp3_data = {
					'Name'       : sample_name,
					#'bytestring': sample.raw_data, # Dat is LONG
					'Hz' : sample.frame_rate,
					'Time'    : round(sample.duration_seconds, 2),
					#'size'      : sample.sample_width, # bytes
					#'channels'  : sample.channels,
					'rms'        : sample.rms,
					'dBFS'		 : sample.dBFS,
					#'max'		 : sample.max,
					'amax'       : sample.max_possible_amplitude,
					# more: https://www.pydoc.io/pypi/pydub-0.9.5/autoapi/audio_segment/index.html
					}
		SAMPLES_DATA[sample_name] = mp3_data
		
		# Terminal raport
		print('Name:', mp3_data['Name'])
		print('Hz  :', mp3_data['Hz'])
		print('Time:', mp3_data['Time'])
		print('rms :', mp3_data['rms'])
		print('dBFS:', mp3_data['dBFS'])
		print('amax:', mp3_data['amax'])
		print('--------------------')
		print()

	# Save 2 da script folda
	df = pd.DataFrame(SAMPLES_DATA, index=dtypes)
	path = 'songs_data.csv'
	df = df.T
	df.to_csv(path, sep=',', index=False)

	print('\nSaved raport to: {}'.format(abspath(path)))

if __name__ == '__main__':
	get_mp3_data()
