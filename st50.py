import json

with open("data.json", encoding="utf-8") as file:
    with open('updated_data.json', 'w') as json_file:
        def process_data(data):
            data_type = type(data)
            if data_type == str:
                return data + '!'
            elif data_type == bool:
                return not data
            elif data_type == int:
                return data + 1
            elif data_type == list:
                return data + data
            elif data_type == dict:
                data.update(newkey=None)
                return data
            else:
                pass
        rows = file.read()
        result = []
        for i in json.loads(rows):
            if i == None:
                continue
            else:
                result.append(process_data(i))
        json.dump(result, json_file)
