import requests
import csv

class StockDataFetcher:
    def __init__(self, start_date, end_date, stock_list):
        self.start_date = start_date
        self.end_date = end_date
        self.stock_list = stock_list

    def fetch_data(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
        except requests.RequestException as e:
            print(f"Failed to fetch data from the API: {e}")
            return None

    def write_to_csv(self, data, filename):
        try:
            with open(filename, 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile, delimiter=';')
                csv_writer.writerow(data)
        except IOError as e:
            print(f"Failed to write to CSV file: {e}")

    def fetch_and_write_data(self, url: str, filename:str):
        for s in self.stock_list:
            base_url = f"{url}{s}.csv"
            for start in range(0, 400, 100):
                url = f"{base_url}?from={self.start_date}&till={self.end_date}&start={start}"
                data = self.fetch_data(url)
                if data:
                    try:
                        rows = data.strip().split('\n')
                        data_rows = [row.split(';') for row in rows[2:]]
                        for row in data_rows:
                            self.write_to_csv(row, filename)
                    except Exception as e:
                        print(f"Error processing data: {e}")

        print(f"All data written to {filename}")

def remove_header(input_file, output_file, header: str):
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
    start_date = "2022-10-01"
    end_date = "2023-12-31"
    stock_output = "raw_data.csv" 
    stocks_url = "https://iss.moex.com/iss/history/engines/stock/markets/shares/boards/tqbr/securities/"

    stock_list = ["AFKS", "AFLT", "AGRO", "ALRS", "CBOM", "CHMF", "ENPG", "FEES", "FIVE", "FLOT",
                  "GAZP", "GLTR", "GMKN", "HYDR", "IRAO", "LKOH", "MAGN", "MGNT", "MOEX", "MSNG",
                  "MTLR", "MTLRP", "MTSS", "NLMK", "NVTK", "OZON", "PHOR", "PIKK", "PLZL", "POLY",
                  "POSI", "QIWI", "ROSN", "RTKM", "RUAL", "SBER", "SBERP", "SELG", "SGZH", "SMLT",
                  "SNGS", "SNGSP", "TATN", "TATNP", "TCSG", "TRNFP", "UPRO", "VKCO", "VTBR", "YNDX"]
    
    stock_data_fetcher = StockDataFetcher(start_date, end_date, stock_list)
    stock_data_fetcher.fetch_and_write_data(stocks_url, stock_output)

    header = "BOARDID;TRADEDATE;SHORTNAME;SECID;NUMTRADES;VALUE;OPEN;LOW;HIGH;LEGALCLOSEPRICE;WAPRICE;CLOSE;VOLUME;MARKETPRICE2;MARKETPRICE3;ADMITTEDQUOTE;MP2VALTRD;MARKETPRICE3TRADESVALUE;ADMITTEDVALUE;WAVAL;TRADINGSESSION;CURRENCYID;TRENDCLSPR\n"
    remove_header('raw_data.csv', 'stocks_data.csv', header)

    #moscow index
    index_output = "imoex_index_r.csv" 
    index_data_fetcher = StockDataFetcher(start_date, end_date, ['IMOEX'])
    index_url = "http://iss.moex.com/iss/history/engines/stock/markets/index/boards/SNDX/securities/"
    index_data_fetcher.fetch_and_write_data(index_url, index_output)

    index_header = "BOARDID;SECID;TRADEDATE;SHORTNAME;NAME;CLOSE;OPEN;HIGH;LOW;VALUE;DURATION;YIELD;DECIMALS;CAPITALIZATION;CURRENCYID;DIVISOR;TRADINGSESSION;VOLUME\n"
    remove_header('imoex_index_r.csv', 'imoex_index.csv', index_header)
    

if __name__ == "__main__":
    main()
