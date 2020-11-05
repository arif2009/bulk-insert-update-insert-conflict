import os
import sys
import json


class Helper:

    def read_file(self, file_path):
        try:
            data_array = []
            items = json.load(open(file_path))

            for item in items:
                data_array.append({
                    'uuid': item['uuid'],
                    'data': item['data'],
                    'min': item['min'],
                    'max': item['max'],
                    'avg': item['avg']
                })

            return data_array

        except Exception as e:
            print("read_file Error: %s \n" % str(e))
            sys.exit(1)
