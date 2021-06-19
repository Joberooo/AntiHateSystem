import json

if __name__ == '__main__':
    try:
        f = open('data.json', )
        # returns JSON object as
        # a dictionary
        json_data = json.load(f)
    except FileNotFoundError:
        json_data = {"data":[
            {
                "name": "name",
                "surname": "surname"
            },
            {
                "name": "name",
                "surname": "surname"
            }
        ]}
    with open('data.json', 'w') as f:
        json.dump(json_data, f)
