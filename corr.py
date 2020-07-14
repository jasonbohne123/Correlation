#This program was constructed within a Quantopian Notebook

import numpy as np
import pandas as pd
import scipy
import numpy
from quantopian.research import prices, symbols

StocksTicker=["V","MA","AAPL","MSFT","GOOG","AMZN","FB","BRK-B","BABA","JPM","XOM","BAC","MCD","WMT","HD","CMG","GM","F","TGT","KO","GIS","MRO","PSX","AXP","GS","NDAQ","ABC","CELG","CVS","AAL","BA","GE","LUV","CTXS","SHW","AMT","REG","AEE","EXC","PCG","UNP","WM"]
#StocksTicker=['BTC',"ETH","LTC","BCH","EOS",'LINK','TRX']
Prices=[]
CurrentPrices=[]
DayBefore=[]
Mean=[]
Correlation=[]
Order=[]

df = pd.DataFrame(columns=StocksTicker)
for x in StocksTicker:
    y = prices(
        assets=symbols(x),
        start='2019-04-24',
        end='2019-09-24',
        frequency='minute'
        )
    df[x]=pd.Series(np.gradient(np.gradient(scipy.signal.savgol_filter(y,31, 2, 0, 1.0, -1, 'interp', 0.0))))

corr = df.corr()

#corr.describe() useless for us rn

#can make it more legible if needed,
#it will be much more easier from this to see the correlation
ax = sns.heatmap(
    corr, 
    vmin=-1, vmax=1, center=0,
    square=True
)
#less number of negative correlation. bit shocking though. 
