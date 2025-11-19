def update_records(record, album_id, property, value):
    album_id = str(album_id)
    if album_id not in record:
        return record
    if value == "":
        record[album_id].pop(property, None)
    elif property != "tracks":
        record[album_id][property] = value
    else:
        record[album_id].setdefault("tracks", []).append(value)

    return record


value = input()
try:
    updates = value.split("}} | ")
    record = eval(updates[0] + "}}")  

    if not isinstance(record, dict):
        raise ValueError

    for update in updates[1:]:
        try:
            album_id, property, value = map(str.strip, update.split("|"))
            album_id = int(album_id) 
        except Exception:
            raise ValueError
        if album_id < 0:
            raise ValueError
        if property not in ["artist", "albumTitle", "tracks"]:
            raise ValueError
        record = update_records(record, album_id, property, value)
    output = record
except Exception:
    output = "Invalid"

print(output)
