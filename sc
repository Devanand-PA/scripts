#!/bin/bash
FILENAME="$(du -a | awk '{$1="FileSizeInDu";print $0}' | awk -F "FileSizeInDu " '{print $NF}' | dmenu -i -l 30 -sb "#bb0000" -fn "monospace:size=14")"
FILETYPE="$(echo $FILENAME | awk -F "." '{print $NF}')"
echo $FILETYPE
if [ -z $FILETYPE ]
then
	exit
else
case $FILETYPE in
	pdf | epub | djvu)
		FILEPROGRAM="okular" ;;
	png | jpg | jpeg | webp)
		FILEPROGRAM="sxiv" ;;
	mp4 | webm | mkv | opus | mp3)
		FILEPROGRAM="mpv" ;;
	*)
		FILEPROGRAM="st -e vim" ;;

esac
$FILEPROGRAM "$FILENAME"
fi
