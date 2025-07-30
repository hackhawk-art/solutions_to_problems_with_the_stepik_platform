from zipfile import ZipFile

def convert_bytes(size):
    if size == 0:
        return f"{''}".strip("")
    elif size < 1000:
        return f'{size} B'
    elif 1000 <= size < 1000000:
        return f'{round(size / 1024)} KB'
    elif 1000000 <= size < 1000000000:
        return f'{round(size / 1048576)} MB'
    else:
        return f'{round(size / 1073741824)} GB'

with ZipFile("desktop.zip") as zip_file:
    for i in zip_file.infolist():
        name = i.filename.strip("/").split("/")
        probel = '  ' * (len(name) - 1)
        print(f"{probel}{name[-1]} {convert_bytes(i.file_size)}")
