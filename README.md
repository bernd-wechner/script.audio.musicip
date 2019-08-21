A simple Kodi Addon that generates playlists using a headless Music IP server.

To use this you will neeed:

Kodi: https://kodi.tv/

A Music IP headless server:  https://www.spicefly.com/article.php?page=musicip-software

To install the addon, you can clone this whole repo put it into a .zip file and then in Kodi install the addon from the zip file. Kodi supports that. Though it'll warn you lots about untrusted sources and jazz along the way. Perhaps one day this addon will be on the offical and downloadable list, and perhaps not, because it doesn't really offer anything to an average user, you need the savvy to download, and get running a headless MusicIP server befor it provides you with any utility.

If you have Kodi installed on Linux, you can just copy this whole repo to ~/.kodi/addons

This one for canmple resides in:  ~/.kodi/addons/script.audio.musicip

I hope to find time to add some more of the MusicIP features, and diagnose a most irritating feature this addon has. This is a list of things to fix:

1. It fetches a mix from the Music IP headless server and adds it tot he Kodi playlist fine. But on the Kodi web interface and the Kodi phone app (Kore) the playlist simply renders as a list of very long file paths that aren't useful. Only after the playlist is viewed in Kodi proper, does Kodi fetch metadata from all htose music files and then the web interface and the phone app show the play list as playlist, songs, artists and even covers. The open quesiton is, can a script ask Kodi to do this fetch.

2. I'd like an option to replace the current playlist. Currently it just inserts the mix after the playing song.

3. I'd like an option to do continuous mixes along with two song counts (M and N) . It should trigger when the Mth song from the end of the playlist starts playing and send the last N songs on the playlist to the Music IP headless server and append the results to the playlist. It might be prudent to remove the head of the playlist also to avoid endless growth. The idea though is that I can get an enless list rolling .... 
