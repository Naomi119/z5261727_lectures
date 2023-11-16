import yfinance                                           # (1)
tic = "QAN.AX"                                            # (2)
start = '2020-01-01'                                      # (3)
end = None                                                # (4)
df = yfinance.download(tic, start, end, ignore_tz=True)   # (5)
print(df)                                                 # (6)
df.to_csv('qan_stk_prc.csv')                              # (7)

import yfinance as yf

def yf_prc_to_csv(tic, pth, start=None, end=None):
    df = yf.download(tic, start=start, end=end, ignore_tz=True)
    df.to_csv(pth)

    