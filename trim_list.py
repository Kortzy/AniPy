# Remove Entries that have MAL ID
# imports
import os
import sys
import json
import importlib

# Import external 'func'
fMain = importlib.import_module("func.func")


# Paths for Files
PROJECT_PATH = os.path.dirname(sys.executable)
fMain.logString("Current path: " + PROJECT_PATH)

# Files
inputAnime = "anime.json"
inputManga = "manga.json"
outputAnime = "anime_NotInMal.json"
outputManga = "manga_NotInMal.json"
outputStats = "animemanga_stats.txt"

# App Properties
appVersion = '1.0.0.0'
appBuild = 1

# STATS variables
statScoreTotal = 0
statScoreCount = 0

# Delete prev files
fMain.deleteFile(outputStats)

# json objects
fMain.logString("Loading " + inputAnime + " into memory..")
with open(inputAnime, "r+", encoding='utf-8') as F:
    jsonAnime = json.load(F)
    fMain.logString("File: " + inputAnime + " is loaded!..")

fMain.logString("Loading " + inputManga + " into memory..")
with open(inputManga, "r+", encoding='utf-8') as F:
    jsonManga = json.load(F)
    fMain.logString("File: " + inputManga + " is loaded!..")

jsonOutputAnime = []
jsonOutputManga = []

for entry in jsonAnime:
    # Get each entry
    if (entry["idMal"] < 1):
        # If not in MAL, ID = 0
        jsonData = {}
        jsonData["idAnilist"] = entry["idAnilist"]
        jsonData["titleEnglish"] = entry["titleEnglish"]
        jsonData["titleRomaji"] = entry["titleRomaji"]
        jsonData["synonyms"] = entry["synonyms"]
        jsonData["format"] = entry["format"]
        jsonData["source"] = entry["source"]
        jsonData["status"] = entry["status"]
        jsonData["startedAt"] = entry["startedAt"]
        jsonData["completedAt"] = entry["completedAt"]
        jsonData["progress"] = entry["progress"]
        jsonData["totalEpisodes"] = entry["totalEpisodes"]
        jsonData["score"] = entry["score"]
        jsonData["notes"] = entry["notes"]
        # Append to JSON object
        jsonOutputAnime.append(jsonData)

    # Stats checker
    statScore = int(entry["score"])
    if (statScore > 0):
        statScoreTotal = statScoreTotal + statScore
        statScoreCount = statScoreCount + 1

# Write 'outputAnime'
fMain.logString("Writing file: " + outputAnime)
with open(outputAnime, "w+", encoding='utf-8') as F:
    F.write(json.dumps(jsonOutputAnime, ensure_ascii=False, indent=4).encode('utf8').decode())
    fMain.logString("File generated: " + outputAnime)

# Write stats for Anime
fMain.logString("Appending to file (Average Score stats): " + outputStats)
with open(outputStats, "a+", encoding='utf-8') as F:
    F.write("Anime stats:\nAverage Score (out of 100): " + str((statScoreTotal/statScoreCount)*10) + "\n")

# Reset vars
statScoreTotal = 0
statScoreCount = 0

# For MANGA
for entry in jsonManga:
    # Get each entry
    if (entry["idMal"] < 1):
        # If not in MAL, ID = 0
        jsonData = {}
        jsonData["idAnilist"] = entry["idAnilist"]
        jsonData["titleEnglish"] = entry["titleEnglish"]
        jsonData["titleRomaji"] = entry["titleRomaji"]
        jsonData["synonyms"] = entry["synonyms"]
        jsonData["format"] = entry["format"]
        jsonData["source"] = entry["source"]
        jsonData["status"] = entry["status"]
        jsonData["startedAt"] = entry["startedAt"]
        jsonData["completedAt"] = entry["completedAt"]
        jsonData["progress"] = entry["progress"]
        jsonData["progressVolumes"] = entry["progressVolumes"]
        jsonData["totalChapters"] = entry["totalChapters"]
        jsonData["totalVol"] = entry["totalVol"]
        jsonData["score"] = entry["score"]
        jsonData["notes"] = entry["notes"]
        # Append to JSON object
        jsonOutputManga.append(jsonData)

    # Stats checker
    statScore = int(entry["score"])
    if (statScore > 0):
        statScoreTotal = statScoreTotal + statScore
        statScoreCount = statScoreCount + 1

# Write 'outputManga'
fMain.logString("Writing file: " + outputManga)
with open(outputManga, "w+", encoding='utf-8') as F:
    F.write(json.dumps(jsonOutputManga, ensure_ascii=False, indent=4).encode('utf8').decode())
    fMain.logString("File generated: " + outputManga)

# Write stats for Manga
fMain.logString("Appending to file (Average Score stats): " + outputStats)
with open(outputStats, "a+", encoding='utf-8') as F:
    F.write("Manga stats:\nAverage Score (out of 100): " + str((statScoreTotal/statScoreCount)*10) + "\n")