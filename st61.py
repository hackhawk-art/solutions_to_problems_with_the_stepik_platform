from zipfile import ZipFile
from datetime import datetime

with ZipFile("workbook.zip") as zip_file:
    res = []
    for i in zip_file.infolist():
        d = i.date_time
        data = datetime.strptime(f"{d[0]}-{d[1]}-{d[2]} {d[3]}:{d[4]}:{d[5]}", "%Y-%m-%d %H:%M:%S")
        if data > datetime.strptime("2021-11-30 14:22:00", "%Y-%m-%d %H:%M:%S"):
            if i.is_dir() is False:
                res.append((i.filename.split("/")[-1]))
    print(*sorted(res), sep="\n")