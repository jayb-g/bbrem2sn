# BB10 Remember -> Standard Notes plaintext(/super note) import format Converter
A simple python program to convert BlackBerry10 Remember Notes backup(backed-up using Runisoft Ultimate Backup on BB10) to Standard Notes importable format with attachments support and preserved formatting.

# Overview & Prep
   - Script works completely offline and no data leaves your device whatsoever.
   - It's assumed at this point that you already have the backup(using Ultimate Backup) of your Remember notes; if not, do it.
   - Go to the Runisoft Backup folder location(usually under [Device or Media Card]/documents/Runisoft) > "Remember_Bkp_XXXXXXXXXX" that contains date wise folders for notes backups taken at different times. Choose any one(preferably latest) to import from, and copy that folder to a system.
   - This folder contains an "ATTXXXXXXX" folder that contains all attachments from all the notes in Remember app. You'd want to upload these files to Standard Notes right away. Although you can upload these later after importing the notes but it would be a better experience if you do it earlier.
   - Convert your notes by following Usage instructions below. After the script is done converting, be sure to check a few notes randomly for formatting etc are in the way you'd prefer. If something is not right, modify the script according to your need and start conversion again. Because if you import wrongly formatted notes to SN in bulk, it would be cumbersome to delete large number of notes in SN before you start over and import again. So be sure the first time you import.

# Usage:
   - Download and place the `convert.py` file to the same directory containing the backup file(.rembkp)
      - If you prefer, copy both these files to a completely new folder to avoid messing up with your existing folder contents.
   - (Create a venv if you prefer and) Install requirements by running `pip install -r requirements.txt` or `pip3 install -r requirements.txt`
   - Run program as `python3 convert.py filename.rembkp`
   - All the notes will be exported as txt files inside "Standard Notes - Importables" folder inside current working directory by default.
   - Go to Standard Notes > Account > Import, then select all files inside "Standard Notes - Importables", SN will start importing all notes files one by one. The import process also works well on mobile(tested on Android).
   - Note that this program adds the attachments(if any) as @filename.ext list at the end of each corresponding note in the importable notes.
      + For attachments to show up in SN once all files are imported, open SN and open any of the imported notes with attachements and change note type to Super( > click convert ). Then click on @filename inside the note(preferably, place the cursor at the end of '@foo.bar' to avoid similar filename suggestions/adding wrong file by mistake/leaving residue text after selection), and SN will show you exactly that file to select and attach from: click on it and you're done.
      + All your attachments can be added back to their respective notes this way. I know this is not ideal but for now this seems to be best workable solution. 
      + You don't have to do this step for all the notes right after importing. You can do this any time for any note as and when required in the future as long as you have already uploaded all the attachments to SN beforehand as mentioned in previous section.

# Why .rembkp?
   - First of all, Runisoft Ultimate Backup is the most reliable way to manually backup stuff(including Remember Notes) on BB10, and out of all backup formats it supports(.csv,.html,.rembkp), .rembkp is the only format that seems to contain all the metadata about notes such as tags/attachments/creation and modification times.
   - Although this program currently does not support preserving tags/creation/modification times but can be implemented to support those in near future by converting .rembkp to compatible json - similar to what [simplenote2standardnote](https://github.com/edas/simplenote2standardnote/blob/master/simplenote2standardnote.rb) does. Seems like this is going to be a very short lived project as BB10 has already reached its EOL since Jan 2022 and most would have already moved to other devices.


# ENJOY all your BB10 notes with preseved formatting and attachments inside Standard Notes.!