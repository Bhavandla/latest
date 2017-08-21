#!/usr/local/bin/python

# script to Compare JSON data (Unicode) with CSV records (str)
import csv
import json
import unicodedata

# Converts unicode into byte string
def safe_str(obj):
    """ return the byte string representation of obj """
    try:
        return str(obj)
    except UnicodeEncodeError:
        # obj is unicode
        return unicode(obj).encode('unicode_escape')

# method to join list elements into single string
def get_notes(notes):
    notes = list(notes or "")
    new_notes = ""
    for note in notes:
        new_notes += "*" + note + ". "
    return new_notes

def check_notes(row, json_notes):
    """
    Compare JSON's Notes with CSV's Notes
    """
    with open('filename.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        l = list(reader)
        csv_notes = l[row]["Note Content"]
        encoded = decode('utf-8')
        if safe_str(csv_notes) == encoded:
            print("Record Number:" + str(i) + "Passed")
        else:
            print("Record Number:" + str(i) + "Failed")
            print("Server_Notes is: " + json_notes)
            print("CSV____Notes is: " + encoded)

if __name__ == "__main__":
    with open("filename.json") as f:
        data = json.load(f)
    for i, record in enumerate(data["record"]["field"]):
        try:
            a = record["notes"]  # Notes field in record and its a list
            if a:
                new_notes = get_notes(record["notes"])  # join a list of strings into a single string
                check_notes(i, new_notes)  # compare new_notes with CSV record
        except KeyError as e:
            new_notes = ""
            check_notes(i, new_notes)
