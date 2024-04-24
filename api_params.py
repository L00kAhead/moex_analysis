index_params = {
    "start_date" : "2022-10-01",
    "end_date" : "2023-12-31",
    "output" : "index_raw_data.csv",
    "url" : "http://iss.moex.com/iss/history/engines/stock/markets/index/boards/SNDX/securities/",
    "index_name": "IMOEX",
    "header" : "BOARDID;SECID;TRADEDATE;SHORTNAME;NAME;CLOSE;OPEN;HIGH;LOW;VALUE;DURATION;YIELD;DECIMALS;CAPITALIZATION;CURRENCYID;DIVISOR;TRADINGSESSION;VOLUME\n"
}

stock_params = {
    "start_date" : "2022-10-01",
    "end_date" : "2023-12-31",
    "output" : "stock_raw_data.csv", 
    "stocks_url" : "https://iss.moex.com/iss/history/engines/stock/markets/shares/boards/tqbr/securities/",
    "stock_list" : ["AFKS", "AFLT", "AGRO", "ALRS", "CBOM", "CHMF", "ENPG", "FEES", "FIVE", "FLOT",
                "GAZP", "GLTR", "GMKN", "HYDR", "IRAO", "LKOH", "MAGN", "MGNT", "MOEX", "MSNG",
                "MTLR", "MTLRP", "MTSS", "NLMK", "NVTK", "OZON", "PHOR", "PIKK", "PLZL", "POLY",
                "POSI", "QIWI", "ROSN", "RTKM", "RUAL", "SBER", "SBERP", "SELG", "SGZH", "SMLT",
                "SNGS", "SNGSP", "TATN", "TATNP", "TCSG", "TRNFP", "UPRO", "VKCO", "VTBR", "YNDX"],
    "header" : "BOARDID;TRADEDATE;SHORTNAME;SECID;NUMTRADES;VALUE;OPEN;LOW;HIGH;LEGALCLOSEPRICE;WAPRICE;CLOSE;VOLUME;MARKETPRICE2;MARKETPRICE3;ADMITTEDQUOTE;MP2VALTRD;MARKETPRICE3TRADESVALUE;ADMITTEDVALUE;WAVAL;TRADINGSESSION;CURRENCYID;TRENDCLSPR\n"
}

