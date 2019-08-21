# Import XBMC module
import xbmc,re, os, urllib,urllib2
from string import split, replace, find
from urllib2 import quote

import xbmcplugin
import xbmcgui
import xbmcaddon

# Script constants
__scriptname__ = "MusicIP MIX"

addon=xbmcaddon.Addon()
language = addon.getLocalizedString
icon = addon.getAddonInfo('icon')

# Get User Settings
debug = addon.getSetting('debug')
mixsize=addon.getSetting('mixsize')
mixstyle=addon.getSetting('style')
mixvariety=addon.getSetting('variety')
mipipaddress=addon.getSetting('ipaddress')
mipipport=addon.getSetting('ipport')
mipdpc=addon.getSetting('dynamicpathconversion')
mipdpc1f=addon.getSetting('dpc1_from')
mipdpc1t=addon.getSetting('dpc1_to')
mipdpc2f=addon.getSetting('dpc2_from')
mipdpc2t=addon.getSetting('dpc2_to')
mipdpc3f=addon.getSetting('dpc3_from')
mipdpc3t=addon.getSetting('dpc3_to')

if debug=="true":
	print "Starting MusicIP MIX Add-on"

if xbmc.Player().isPlayingAudio() == False:
	xbmc.executebuiltin('Notification(No playlist generated, a song must be playing,5000,%s)' %(icon))
	self.close()

currentlyPlaying = unicode(xbmc.Player().getMusicInfoTag().getURL(),'utf-8')
if debug=="true":
	print "Currently Playing Song:"
	print currentlyPlaying

#tag = xbmc.Player().getMusicInfoTag()
#artist = tag.getArtist()
#title = tag.getTitle()

size=str(mixsize)
mipstyle=str(mixstyle)
mipvariety=str(mixvariety)
#apiPath = 'http://192.168.0.206:10002/api/mix?song='
apiPath = 'http://%s:%s/api/mix?song=' %(mipipaddress,mipipport)
options = '&size='+size+'&sizeType=tracks&content=text&style='+mipstyle+'&variety='+mipvariety

dpc1active=dpc2active=dpc3active=False
if (mipdpc1f != "") and (mipdpc1f != "Find and replace this in the Kodi filepath"):
	dpc1active=True
if (mipdpc2f != "") and (mipdpc2f != "Second find and replace set"):
	dpc2active=True
if (mipdpc3f != "") and (mipdpc3f != "Third find and replace set"):
	dpc3active=True

if mipdpc=="true":
	if dpc1active==True:
		currentlyPlaying = currentlyPlaying.replace(mipdpc1f,mipdpc1t)
	if dpc2active==True:
		currentlyPlaying = currentlyPlaying.replace(mipdpc2f,mipdpc2t)
	if dpc3active==True:
		currentlyPlaying = currentlyPlaying.replace(mipdpc3f,mipdpc3t)

if debug=="true":
	print "Currently Playing After Dynamic Path Conversion:"
	print currentlyPlaying

# The url in which to use
Base_URL = apiPath + quote(currentlyPlaying.encode('iso-8859-1')) + options
if debug=="true":
	print "MIP request:"
	print Base_URL

#Pre-define global Lists
LinkURL = []
try:
	WebSock = urllib2.urlopen(Base_URL,None,30)  # Opens a 'Socket' to URL
	WebHTML = WebSock.read()            # Reads Contents of URL and saves to Variable
	WebSock.close()                     # Closes connection to url
except:
	xbmc.executebuiltin('Notification(MusicIP call failed, no playlist generated.,5000,%s)' %(icon))
	WebHTML=""

if debug=="true":
	print "MIP Response:"
	print WebHTML

if mipdpc=="true":
	if dpc1active==True:
		WebHTML = WebHTML.replace(mipdpc1t,mipdpc1f)
	if dpc2active==True:
		WebHTML = WebHTML.replace(mipdpc2t,mipdpc2f)
	if dpc3active==True:
		WebHTML = WebHTML.replace(mipdpc3t,mipdpc3f)

if debug=="true":
	print "MIP Response After Dynamic Path Conversion:"
	print WebHTML

LinkURL = WebHTML.split("\n")

if len(LinkURL)>0:
	playList = xbmc.PlayList(0)
	currentPos = playList.getposition()

	if playList.size()>1 and currentPos < playList.size()-1: #Since Kodi, playlist clear would leave the new play list playing at oldplaylist.position, this code fixes that
		for i in range (currentPos+1, playList.size()):
			playList.remove(playList[currentPos+1].getfilename())

	first = True #first item returned from musicIP is the item currently playing, so don't add that to playlist.

	for l in LinkURL:
		if not l == "":
			if not (first):
				playList.add(url=l)
			first=False
 
	xbmc.executebuiltin('Notification(Playlist Generated,'+size +' songs like the current coming up...,5000,%s)' %(icon))
