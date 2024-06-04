import pandas as pd

def main():
    aggData = pd.read_csv('./data/aggregated_results.csv')
    aggData = aggData[['Sample name', 'Classification', 'All genes']]

    #filter for breast cancer samples
    brCan = aggData[aggData['Sample name'].str.contains('BREAST')]
    
    #drop rows with NaN in 'Classification' column
    brCan = brCan.dropna(subset=['Classification'])
    print(brCan['Classification'])

    #filter for ecDNA classifications
    brCan = brCan[brCan['Classification'].str.contains('ecDNA')]
    print(brCan)

    dict = {}
    for c in brCan['All genes']:
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
    output = open('sortedGeneFreqECDNA.txt', 'w')
    for k in sortDict:
        output.write(k[0] +  ': ' + str(k[1]) + '\n')
        print(k)
    

if __name__ == "__main__":
    main()
