import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
import datetime

start = datetime.datetime(2018,9,1)
end = datetime.datetime(2018,9,11)

df = web.DataReader("TESLA", "google", start, end)

print(df)
