import json
import time
# from datetime import datetime
import datetime
# import pytz
import uuid

# import sys

# Testing to supoprt creation and modification times
testVar = False
noteJsonSample = '''{{
  "content_type": "Note",
  "content": {{
    "title": "TEST TITLE",
    "text": "test text\\n\\n\\n\\n@testfile1.jpg\\n\\n@testfile2.jpg",
    "references": [],
    "appData": {{
      "org.standardnotes.sn": {{
        "client_updated_at": "2023-05-30T13:07:03.582Z"
      }}
    }}
  }},
  "created_at_timestamp": 1685451939831000,
  "created_at": "2023-05-30T13:05:39.831Z",
  "deleted": {testvar},
  "updated_at_timestamp": 1685452025076504,
  "updated_at": "2023-05-30T13:07:05.076Z",
  "uuid": "29111565-a050-49cb-a0f0-e3705a3d4cef"
}}'''  #.format(testvar = testVar)
# Full date version in SN seems to be in ISO format

# timezones in SN export is in Unix Timestamp
# timezone is not specified in rembkp but it seems to be local timezone

# timezone need to be adjusted from local to unix while converting notes

# \n has to be converted to \\n in JsonSample

# print(noteJsonSample)

# json_string = json.dumps(noteJsonSample)

# print(json_string)



#########  Working PoC #########

# # localDate = "Sat Sep 18 17:27:27 2021"
# localDate = "Sat May 30 18:35:39 2023" #testing with above jsonSample created date converted to local time
# localDate = localDate.partition(' ')[2] # remove Day from localDate
# print(localDate)

# # print(time.mktime(datetime.datetime.strptime(localDate, "%b %d %H:%M:%S %Y").timetuple()))

# localUnixTS = time.mktime(datetime.datetime.strptime(localDate, "%b %d %H:%M:%S %Y").timetuple())
# localUnixTS = int(localUnixTS) * 1000000 #SN stores it with microseconds so multiplying with 10^6 # would do it after adjusting localoffset

# #Adding 1000 to preserve 3 demcimal points in float later as 
# # localUnixTS = localUnixTS + 1000

# print(localUnixTS)
# # gives 1685451939000000 which is correct Unix time and matching the timestamp in jsonSample above

# # # There doesn't seem to be any need to adjust tz offset manually, above method seems to already automatically consider timezone while giving timetuple
# # # So localUnixTS is indeed UnixTS itself
# # localoffset = time.localtime().tm_gmtoff 

# # unixTS = int(time.time()) # time.time() returns time as float including microseconds

# # # adjustedUnixTS = 


# # localUnixTS = 1685452025076504

# # localUnixTSfloat = float("%.3f" % ( localUnixTS / 1000000 ))

# # print(localUnixTSfloat)

# # Below works exactly as required:
# # dt = datetime.datetime.utcfromtimestamp(1685451939.831000)
# dt = datetime.datetime.utcfromtimestamp(localUnixTS / 1000000)
# iso_format = dt.isoformat() + '.000Z'
# print(iso_format)

#########  End - Working PoC #########



def getUnixTSfromDate(dStamp):
  # Accepts dStamp in the format "Sat Sep 18 17:27:27 2021"
  localDate = dStamp
  localDate = localDate.partition(' ')[2] # remove Day from localDate
  # print(localDate)

  localUnixTS = time.mktime(datetime.datetime.strptime(localDate, "%b %d %H:%M:%S %Y").timetuple())
  localUnixTS = int(localUnixTS) * 1000000 #SN stores it with microseconds so multiplying with 10^6 # would do it after adjusting localoffset

  # print(localUnixTS)
  # d_UnixTS = localUnixTS
  return localUnixTS

def getISOformat(UnixTS):
  dt = datetime.datetime.utcfromtimestamp(UnixTS / 1000000)
  iso_format = dt.isoformat() + '.000Z'
  # print(iso_format)

  # return iso_format
  # d_iso = iso_format
  return iso_format

# testD = "Sun Jun 4 01:20:00 2023"
# testDiso = getUnixTSfromDate(testD)
# print(testDiso)


# # Replace variables in noteJsonSample
# tempNoteVars = {}
# tempNoteVars['testvar'] = testVar

# print(tempNoteVars)

# print(noteJsonSample.format(**tempNoteVars))

# print(uuid.uuid1())


def createSNjson():
  #requires variables inside the jsonFormat already set, so that it can be replaced
  jsonFormat = '''{{
  "content_type": "Note",
  "content": {{
    "title": "{noteName}",
    "text": "{noteText}",
    "noteType": "plain-text",
    "references": [],
    "appData": {{
      "org.standardnotes.sn": {{
        "client_updated_at": "{updated_d_iso}"
      }}
    }}
  }},
  "created_at_timestamp": {created_ts},
  "created_at": "{created_d_iso}",
  "deleted": false,
  "updated_at_timestamp": {updated_ts},
  "updated_at": "{updated_d_iso}",
  "uuid": "{uuid}"
}}'''
#leaving client_updated_at as it is around creation of this script to let SN know what it wants to know by this ( probably SN version associated with exported data, so that it can import accordingly )
#apparently, client_updated_at is used as modification time shown in a client (and for sorting). So it has to be updated to same as 'updated_at' (value of {updated_d_uso})

  noteVars = {}
  noteVars['noteName'] = noteName
  # noteVars['noteText'] = noteText
  # escape newlines and " characters to store in json
  noteVars['noteText'] = noteText.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n').replace('\r', '\\r').replace('\b', '\\b').replace('\f', '\\f').replace('\t', '\\t')
  #weirdly enough, SN does not escape / characters
  noteVars['created_ts'] = created_ts
  noteVars['created_d_iso'] = created_d_iso
  noteVars['updated_ts'] = updated_ts
  noteVars['updated_d_iso'] = updated_d_iso
  noteVars['uuid'] = uuid.uuid1()

  SNjson = jsonFormat.format(**noteVars)

  return SNjson


noteName = "Test Note"
noteText = """test
"note\\content"""

created_date = "Sun Jun 4 01:20:00 2023"
created_ts = getUnixTSfromDate(created_date)
created_d_iso = getISOformat(created_ts)

updated_date = "Sun Jun 4 01:25:03 2023"
updated_ts = getUnixTSfromDate(updated_date)
updated_d_iso = getISOformat(updated_ts)

# print(createSNjson())
SNjson = createSNjson()
# print(SNjson)

# out_file = open("sampleNote.json", "w")
# json.dump(SNjson, out_file, indent = 4)

SNjsonArr = []
# SNjsonArr[1] = SNjson #This won't work as You can only use indexing (e.g. obj[x]) to access or modify items that already exist in a list.
# ref: https://stackoverflow.com/questions/5544228/assigning-a-value-to-python-list-doesnt-work
SNjsonArr.append(json.loads(SNjson)) #if not used json.loads, SNjson is added entirely as a string
print(SNjsonArr)


#PoC for just one note
notesDict = {}
notesDict['items'] = []
# notesDict['items'][0] = SNjson
notesDict['items'] = SNjsonArr

# # json.dumps(notesDict, indent = 3)
# json.dump(notesDict, sys.stdout, indent = 3)

# out_file = open("sampleNote.json", "w")
# json.dump(notesDict, out_file, indent = 3)

print(notesDict)
# print(json.dumps(notesDict));
SNjsonContent = json.dumps(notesDict, indent = 3)
print(SNjsonContent)
# exit()

# f = open(noteName + ".txt", "w")
f = open("StandardNotes_json.txt", "w")
f.write(SNjsonContent)
f.close()


# # FYI
# {
#   "version": "004",
#   "items": [ ]
# }
# # items contain array of notes jsons