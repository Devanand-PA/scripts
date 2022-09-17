#!/bin/bash
xdg-open $(du -a | fzf | awk '{$1="FileSizeInDu";print $0}' | awk -F "FileSizeInDu" '{print$2}')
