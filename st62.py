from zipfile import ZipFile
from datetime import datetime

with ZipFile("workbook.zip") as zip_file:
    my_dict = {}
    for i in zip_file.infolist():
        d = i.date_time
        data = datetime.strptime(f"{d[0]}-{d[1]}-{d[2]} {d[3]}:{d[4]}:{d[5]}", "%Y-%m-%d %H:%M:%S")
        if i.is_dir() is False:
            mod_size = f"  Дата модификации файла: {data}"
            int_size = f"  Объем исходного файла: {i.file_size} байт(а)"
            comp_file = f"  Объем сжатого файла: {i.compress_size} байт(а)"
            my_dict.update({i.filename.split("/")[-1]: [mod_size, int_size, comp_file, ""]})
    for k, v in sorted(my_dict.items(), key=lambda x: x[0]):
        print(k)
        for i in v:
            print(i)

