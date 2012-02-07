import csv
import zipfile

fp = 'data/FX_csv_2.zip'
outfp = 'data/consolidated.csv'
writer = csv.writer(open(outfp, 'w'))
writer.writerow(['Date', 'Rate', 'Currency', 'Frequency'])
zfo = zipfile.ZipFile(fp)
fo = zfo.open('FX_csv_2/README_SERIES_ID_SORT.txt')

def run_all_files():
    start = False
    end = False
    for line in fo.readlines():
        if start:
            if line.strip() == '':
                end = True
        if start and not end:
            parts = line.split(';')
            id_ = parts[0].strip()
            country = parts[1].split('/')[0].strip()
            if country == 'U.S.':
                country = parts[1].split('/')[1].strip().split(' ')[0].strip()
            freq = parts[3].strip()
            # we don't want trade-weighted exchange rates
            if ('TWEX' in id_ or
                country == 'Foreign Exchange Rate: Euro Community (DISCONTINUED SERIES)'
                ):
                continue
            try:
                extract(id_, country, freq)
            except Exception, inst:
                print id_, country
                raise
        if line.startswith('File'):
            start = True

iso_codes = {
    'Brazil': 'BRL',
    'Canada': 'CAD',
    'China': 'CNY',
    'Denmark': 'DKK',
    'Hong Kong': 'HKD',
    'India': 'INR',
    'Japan': 'JPY',
    'South Korea': 'KRW',
    'Malaysia': 'MYR',
    'Mexico': 'MXN',
    'Norway': 'NOK',
    'Austria': 'ATS',
    'Belgium': 'BEF',
    'Finland': 'FIM',
    'France': 'FRF',
    'Germany': 'DEM',
    'Greece': 'GRD',
    'Italy': 'ITL',
    'Netherlands': 'NLG',
    'Portugal': 'PTE',
    'Sweden': 'SEK',
    'South Africa': 'ZAR',
    'Singapore': 'SGD',
    'Sri Lanka': 'LKR',
    'Spain': 'ESP',
    'Switzerland': 'CHF',
    'Taiwan': 'TWD',
    'Thailand': 'THB',
    # Pre 2008 it was 'VEB'
    'Venezuela': 'VEF',
    'Australia': 'AUD',
    # New Zealand
    'New': 'NZD',
    'U.K': 'GBP',
    'Euro': 'EUR',
    'Ireland': 'IEP'
    }

def extract(id_, country, freq):
    fp = 'FX_csv_2/data/%s' % id_
    fo = zfo.open(fp)
    reader = csv.reader(fo)
    reader.next()
    for row in reader:
        outrow = row + [iso_codes[country], freq]
        writer.writerow(outrow)
    fo.close()


run_all_files()
