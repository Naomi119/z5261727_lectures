""" yf_example2.py

Example of a function to download stock prices from Yahoo Finance.
"""

import yfinance as yf
import os


def yf_prc_to_csv(tic, pth, start=None, end=None):
    """ Downloads analysts recommendation from Yahoo Finance and saves the
    information in a CSV file

    Parameters
    ----------
    tic : str
        Ticker

    pth : str
        Location of the output CSV file

    start: str, optional
        Download start date string (YYYY-MM-DD)
        If None (the default), start is set to '1900-01-01'

    end: str, optional
        Download end date string (YYYY-MM-DD)
        If None (the default), end is set to the most current date available
    """
    df = yf.download(tic, start=start, end=end)
    df.to_csv(pth)


# print(f"The value of __name__ is: '{__name__}'")  # if import from python console, the name is module name

# Example
# if __name__ == "__main__":
#     tic = 'QAN.AX'
#     pth = 'qan_stk_prc.csv'
#     yf_prc_to_csv(tic, pth)


if __name__ == "__main__":
    import os
    import toolkit_config as cfg
    tic = 'QAN.AX'
    pth = os.path.join(cfg.DATADIR, 'qan_stk_prc.csv')
    yf_prc_to_csv(tic, pth)


# How to reuse the module outside
# import yf_example2
# yf_example2.yf_prc_to_csv("QAN.AX", "qan_stk_prc.csv")
