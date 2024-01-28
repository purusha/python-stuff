import pandas as pd
import time

def csvToXml(csv, xml):
    df = pd.read_csv(csv)
    df.to_xml(xml)

if __name__ == '__main__':
    start_time = time.time()
    csvToXml('People_data.csv', 'People_data.xml')
    print("XML generation complete!")
    print("--- %s seconds ---" % (time.time() - start_time))
