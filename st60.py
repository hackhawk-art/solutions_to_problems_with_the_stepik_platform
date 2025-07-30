from zipfile import ZipFile

with ZipFile("workbook.zip") as zip_file:
    my_dict = {}
    info = zip_file.infolist()
    for i in info:
        if i.is_dir() is False:
            k = (i.compress_size / i.file_size) * 100
            my_dict.update({i.filename.split("/")[-1]: k})
    print(min(my_dict.items(), key=lambda x: x[1])[0])