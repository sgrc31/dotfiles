#!/usr/bin/env bash

# Define the filename with date and time
FILEPATH=~/Documents/Screenshots/$(date +"%d-%m-%y_%H-%M").png
DIRPATH=$(dirname "$FILEPATH")
FILENAME=$(basename "$FILEPATH")

# Create the Screenshots directory if it doesn't exist
#mkdir -p ~/Pictures/Screenshots

# Take the screenshot
maim -s "$FILEPATH"

# If the screenshot was taken successfully, show a notification
if [ -f "$FILEPATH" ]; then
    dunstify "Success!" "Screenshot $FILENAME saved in \n $DIRPATH"
fi
