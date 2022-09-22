#!/bin/bash
FILENAME="$(du -a | fzf | awk '{$1="FileSizeInDu";print $0}' | awk -F "FileSizeInDu " '{print $NF}')"
FILETYPE="$(echo $FILENAME | awk -F "." '{print $NF}')"
echo $FILETYPE

case $FILETYPE in
	pdf | epub | djvu)
		FILEPROGRAM="okular" ;;
	png | jpg | jpeg | webp)
		FILEPROGRAM="sxiv" ;;
	mp4 | webm | mkv | opus | mp3)
		FILEPROGRAM="mpv" ;;
	*)
		FILEPROGRAM="vim" ;;
esac
$FILEPROGRAM "$FILENAME"
