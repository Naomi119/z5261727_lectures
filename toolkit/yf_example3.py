"""
yf_example3.py
Quiz 4 example of download stock prices from Yahoo Finance.
"""

import os
import toolkit_config as cfg
import yf_example2


def qan_prc_to_csv(year):
    """
    Download stock price data for Qantas for a given year and save into a CSV file

    Parameters
    ----------
    year:int

    Returns
    ----------
    """

    start = f"{year}-01-01"
    end = f"{year}-12-31"

    file_pth = os.path.join(cfg.DATADIR, f'qan_prc_{year}.csv')

    yf_example2.yf_prc_to_csv("QAN.AX",  file_pth, start, end)



if __name__ == "__main__":
    qan_prc_to_csv(2020)





