import json
import csv


class Converter:

    file_type = {"json" : 1, "csv" : 2}

    def __init__(self, filename, input_type, output_type):
        self.filename = filename
        self.convert(input_type, output_type)
        self.input_type = input_type
        self.output_type = output_type


    def convert(self, inp, out):
        if inp is 1 and out is 2:
            # convert json to csv
            with open(self.filename + '.json') as input_file:
                data_json = json.load(input_file)
                input_file.close()
            with open( self.filename + '.csv') as out_file:
                csv_f = csv.writer(out_file)
                # writing json array elements in csv rows
                for el in data_json:
                    csv_f.writerow(el)

                out_file.close()

        elif inp is 2 and out is 1:
            # create a dictionary
            data = {}

            # Open a csv reader called DictReader
            with open(self.filename + '.csv', encoding='utf-8') as csv_file:
                csv_reader = csv.DictReader(csv_file)

                # Convert each row into a dictionary
                # and add it to data
                for rows in csv_reader:
                    # Assuming a column named 'No' to
                    # be the primary key
                    key = rows['No']
                    data[key] = rows

            # Open a json writer, and use the json.dumps()
            # function to dump data
            with open(self.filename + '.json', 'w', encoding='utf-8') as json_file:
                json_file.write(json.dumps(data, indent=4))

            csv_file.close()
            json_file.close()
        else:
            raise IOError;

    def get_json(self):
        return self.filename + '.json'

    def get_csv(self):
        return self.filename + '.csv'


if __name__ == "__main__":
    filename = 'yelp_academic_dataset_review'
    converter = Converter('yelp_academic_dataset_review', 1, 2)
    print(converter.get_json() + " and " + converter.get_csv())
