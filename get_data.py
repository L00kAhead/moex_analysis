import requests
import csv
from api_params import stock_params, index_params

class DataFetcher:
    def fetch_data(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
        except requests.RequestException as e:
            print(f"Failed to fetch data from the API: {e}")
            return None

class DataWriter:
    def write_to_csv(self, data, filename):
        try:
            with open(filename, 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile, delimiter=';')
                csv_writer.writerow(data)
        except IOError as e:
            print(f"Failed to write to CSV file: {e}")

class DataProcessor:
    def __init__(self, start_date, end_date, stock_list):
        self.data_fetcher = DataFetcher()
        self.data_writer = DataWriter()
        self.start_date = start_date
        self.end_date = end_date
        self.stock_list = stock_list

    def fetch_and_write_data(self, url: str, output_file: str):
        for s in self.stock_list:
            base_url = f"{url}{s}.csv"
            print(f"Fetching {s}...")
            for start in range(0, 400, 100):
                f_url = f"{base_url}?from={self.start_date}&till={self.end_date}&start={start}"
                data = self.data_fetcher.fetch_data(f_url)
                if data:
                    try:
                        rows = data.strip().split('\n')
                        data_rows = [row.split(';') for row in rows[2:]]
                        for row in data_rows:
                            self.data_writer.write_to_csv(row, output_file)
                    except Exception as e:
                        print(f"Error processing data: {e}")

        print(f"All data written to {output_file}")

    @staticmethod
    def remove_header(input_file: str, output_file: str, header: str):
        try:
            with open(input_file, 'r') as f:
                lines = f.readlines()
            data_lines = [line for line in lines if not line.startswith("BOARDID")]
            #insert header in file 
            data_lines.insert(0, header)

            with open(output_file, 'w') as f:
                f.writelines(data_lines)
            print("Header removed successfully. Modified file saved as '{}'.".format(output_file))
        except IOError as e:
            print(f"Failed to read/write file: {e}")

def main():

    stock_data = DataProcessor(
        start_date=stock_params['start_date'],
        end_date=stock_params['end_date'],
        stock_list=stock_params['stock_list']
    )
    stock_data.fetch_and_write_data(
        url=stock_params['url'], 
        output_file=stock_params['output']
    )
    DataProcessor.remove_header(stock_params['output'], 'stocks_data.csv', stock_params['header'])

 
    index_data = DataProcessor(
        start_date=index_params['start_date'],
        end_date=index_params['end_date'],
        stock_list=index_params['index_name']

    )
    index_data.fetch_and_write_data(
        url=index_params['url'],
        output_file=index_params['output']
    )
    DataProcessor.remove_header(index_params['output'], 'index_data.csv', index_params['header'])
    

if __name__ == "__main__":
    main()
