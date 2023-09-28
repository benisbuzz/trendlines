import pandas as pd
from findpeaks import findpeaks
from typing import Optional

def get_highs_lows(
        series_list: list, 
        window: Optional[int] = 50,
        minperc: Optional[int] = 5
        ) -> dict[str, pd.Series]:
    finder = findpeaks(method= "caerus", 
                       params_caerus= {"window" : window, 
                                       "minperc" : minperc})
    results = finder.fit(series_list)["df"]
    return {
        "highs" : results[results["peak"] == True]["y"]
        .rename(index = lambda x: series_list.index[x]),
        "lows" : results[results["valley"] == True]["y"]
        .rename(index = lambda x: series_list.index[x])
        }

