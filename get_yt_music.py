from __future__ import unicode_literals
from sys import argv
import os

#!pip install youtube_dl
import youtube_dl

def yt_download_mp3():
	
	# Save folder
	if not os.path.exists('yt_music'):
		os.mkdir('yt_music')
	else:
		os.chdir('yt_music')

	# Setup
	yt_settings =  {'format:': 'bestaudio/best',    # audio best format
					'outtmpl': '%(title)s.%(ext)s', #
					'notchecckcertificate': True,   # we trust yt
					'postprocessors': [{'key': 'FFmpegExtractAudio',
										'preferredcodec' : 'mp3',
										'preferredquality' :'192'}],} 

	# Download: 'python get_yt_music.py' text
	with youtube_dl.YoutubeDL(yt_settings) as ydl:
		with open('../' + argv[1], 'r') as f:
			for song_url in f:
				ydl.download([song_url])

if __name__ == '__main__':
	yt_download_mp3()