import pytube
import sys

def getAmoutOfLines():
	qnt = 0
	links_list = open("links.txt", 'r')
	for line in links_list:
		read = line.split()
		qnt += 1
	return qnt

qnt_videos = getAmoutOfLines()

def downloadList():
	count = 0
	links_list = open("links.txt", 'r')
	for line in links_list:
		count += 1
		read = line.split()
		link = ""
		for char in read:
			if char != "'" or char != "]" or char != "[":
				link += char
			else: continue
		print("Downloading video " + str(count) + " of " + str(qnt_videos), end="")
		percent = ((count-1)*100)/qnt_videos
		print("  ("+str(percent)+"%)")
		yt = pytube.YouTube(link)
		vids = yt.streams.filter(progressive=True).all()
		vids[0].download()
	print("All videos downloaded  (100.0%)")

downloadList()
sys.exit()