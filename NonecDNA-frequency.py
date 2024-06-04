import pandas as pd

def main():
    aggData = pd.read_csv('./data/aggregated_results.csv')
    aggData = aggData[['Sample name', 'Classification', 'All genes']]

    brCan = aggData[aggData['Sample name'].str.contains('BREAST')]

    # filter out ecDNA
    brCanNonEc = brCan[((brCan.Classification != 'ecDNA'))]
    print(brCanNonEc)

    dict = {}
    for c in brCanNonEc['All genes']:
        c = c[1:len(c) - 1]
        x = list(c.split(", ")) 

        for g in x:
            g = g[1:len(g) - 1]
            if g == '':
                continue
            if g not in dict:
                dict[g] = 1
            else:
                dict[g] += 1

    sortDict = sorted(dict.items(), key=lambda x: x[1], reverse = True)
    output = open('non-ecDNA-freq.txt', 'w')
    for k in sortDict:
        output.write(k[0] +  ': ' + str(k[1]) + '\n')
        print(k)
    

if __name__ == "__main__":
    main()