# Read data function
def read_data(raw_data):

    return pd.read_csv(raw_data, sep='\t',parse_dates=True)
