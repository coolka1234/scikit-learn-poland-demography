import pandas as pd
import sys
import csv
def modify_file(fileName):
    df = pd.read_csv(fileName+'.csv')
    df['Year'] = df['Year'].astype(str).str.split('.').str[0]
    df.drop_duplicates(subset='Year', inplace=True)
    df.to_csv(fileName+ '_modified.csv', index=False)
    with open(fileName+'_modified.csv','a', newline='') as fd:
        writer = csv.writer(fd)
        writer.writerow(["2013", 59.918070533034])
        writer.writerow(["2014", 59.71473307938753])
        writer.writerow(["2015", 59.51039562574106])
        writer.writerow(["2016", 59.30605817209459])
        writer.writerow(["2017", 59.10172071844812])
        writer.writerow(["2018", 58.89738326480165])
        writer.writerow(["2019", 58.69304581115518])
        writer.writerow(["2020", 58.48870835750871])
        writer.writerow(["2021", 58.28437090386224])
        writer.writerow(["2022", 58.08003345021577])
if __name__ == '__main__':
    try:
        modify_file(sys.argv[1])
    except:
        print('File not found')