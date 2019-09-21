# Read data function
def read_data(raw_data):

    data = pd.read_csv(raw_data, sep='\t',parse_dates=True)

    return data
