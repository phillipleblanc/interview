data_records = []

data_fields = ["time", "city", "population", "latitude", "longitude"]


def add_data_record(data: "dict[str]"):
    new_record = dict()

    for key in data:
        if key in data_fields:
            new_record[key] = data[key]

    if len(new_record) > 0:
        data_records.append(new_record)


def get_data_records():
    return data_records


def clear_records():
    data_records.clear()
