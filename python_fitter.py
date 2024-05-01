import pandas as pd
import sys
def modify_file(fileName):
    df = pd.read_csv(fileName+'.csv')
    df['Year'] = df['Year'].astype(str).str.split('.').str[0]
    df.drop_duplicates(subset='Year', inplace=True)
    df.to_csv(fileName+ '_modified.csv', index=False)
if __name__ == '__main__':
    try:
        modify_file(sys.argv[1])
    except:
        print('File not found')