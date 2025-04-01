import random
from src.app.utilities.datetime import get_timestamp


def get_file_extension(filename: str | None) -> str:
    try:
        return filename.split(".")[-1]
    except:
        return None


def filename_generator(folder: str, filename: str | None):
    ts = get_timestamp()
    ts = str(ts).replace(".", "")
    rand = str(random.randint(0, 999)).zfill(3)
    file_extension = get_file_extension(filename)
    return f"{folder}/{ts}-{rand}.{file_extension}"
