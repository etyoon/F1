from pytrends.request import TrendReq


def google_trends(sponsor_lst, date):
    '''
    INPUTS:
    sponsor_lst: (List) list of at most five sponsors that we want to see
    the trends for
    dates
    date: (String) string of dates in YYYY-MM-DD format, with oldest date first
    seperated by space character

    OUTPUTS:
    df: returns pandas dataframes of daily searches
    '''

    if len(sponsor_lst) > 5:
        raise ValueError("The sponsor list is more then five words")

    pytrends = TrendReq(hl='en-US', tz=360)

    pytrends.build_payload(sponsor_lst, cat=0, timeframe=date, geo='', gprop='')

    df = pytrends.interest_over_time()
    df.drop("isPartial", axis = 1, inplace = True)

    return df
