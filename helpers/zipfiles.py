
from typing import Dict, Any

EXPORT_PATH = "./data/exports"

def extract(path: str) -> Dict[str, Any]:
    if path.endswith(".zip"):
        return extract_zipfiles(path)
    if path.endswith(".gz"):
        return extract_gzip(path)
    return None

def extract_zipfiles(path: str) -> Dict[str, Any]:
    import zipfile

    directory = path.split("/") # ., data, requirements.zip
    folder = directory[len(directory) - 1][:-len(".zip")] # requirements.zip to requirements
    export = "/".join([EXPORT_PATH, folder]) # ./data/exports/requirements

    with zipfile.ZipFile(path, "r") as f:
        f.extractall(export)
        files = f.namelist() # ["test.txt"]
    
    for idx, file in enumerate(files):
        files[idx] = "/".join([export, file]) # ./data/exports/requirements/test.txt

    results = {
        "directory": export,
        "files": files
    }

    return results

def zipfile_info(path: str) -> Dict[str, Any]:
    import zipfile

    files = []

    with zipfile.ZipFile(path) as folder:
        for file in folder.filelist:
            datetime = "%d-%02d-%02d %02d:%02d:%02d" % file.date_time[:6]
            date, time = datetime.split(" ")
            year, month, day = date.split("-")
            hour, minute, seconds = time.split(":")
            bytes = file.file_size
            filename = file.filename
            files.append({
                "filename": filename,
                "year": int(year),
                "month": int(month),
                "day": int(day),
                "hour": int(hour),
                "minute": int(minute),
                "second": int(seconds),
                "bytes": int(bytes)
            })
    return files

def extract_gzip(path: str) -> Dict[str, Any]:
    import gzip
    
    # gzips are only for single files. Source: https://en.wikipedia.org/wiki/Gzip
    with gzip.open(path, "r") as f:
        contents = f.readlines()
    
    content = [str(x, 'utf-8') for x in contents]

    results = {
        # "directory": export, # No directory will be pushed
        "content": content
    }

    return results
