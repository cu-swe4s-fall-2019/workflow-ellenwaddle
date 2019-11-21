import sys
import matplotlib
import argparse
import matplotlib.pyplot as plt
import get_gene_counts as genecounts
import get_tissue_samples as tissue_samps
matplotlib.use('Agg')

'''
this file should take tissues, genes from command line to create boxplot.
'''

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--tissues', type = str, help = 'tissues you want')
    parser.add_argument('--genes', type = str, help = 'genes you want')
    parser.add_argument('--out_file', type = str, help = 'output file name')
    args = parser.parse_args()

    #boxplot(out_file = args.out_file, genes = args.genes, tissues = args.tissues)

    genes = args.genes
    tissues = args.tissues
    out_file = args.out_file


    counts = []
    for i in range(len(genes)):
        gene = genes[i]
        tissue = tissues[i]
        sample_to_count_map = {}

        #generate required data from gene counts
        print(gene)
        genecounts.get_counts(gene, gene+'_counts.txt')

        f = open(gene + '_counts.txt')
        for l in f:
            A = l.rstrip().split()
            sample_to_count_map[A[0]] = int(A[1])
        f.close()

        count = []

        #generate required data from tissue
        tissue_samps.get_counts(tissue, tissue+'_samples.txt')

        f = open(tissue + '_samples.txt')
        for l in f:
            sample = l.rstrip()
            if sample in sample_to_count_map:
                count.append(sample_to_count_map[sample])
        f.close()

        counts.append(count)

    width=len(genes) * 3
    height=3
    fig = plt.figure(figsize=(width,height),dpi=300)

    for i in range(len(genes)):
        ax = fig.add_subplot(1,len(counts),1+i)
        ax.hist(counts[i])
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.set_title(genes[i] + ' ' + tissues[i])
    plt.savefig(out_file, bbox_inches='tight')



#python box.py --tissues [Brain] --genes [SDHB] --out_file test.png
#python box.py [--tissues Brain, Heart] [--genes SDHB, MEN1] --out_file test.png


#python box.py --tissues [Brain, Heart, Blood, Skin] \
#--genes [SDHB, MEN1] \
#--out_file Brain-Heart-Blood-Skin_SDHB-MEN1.png
