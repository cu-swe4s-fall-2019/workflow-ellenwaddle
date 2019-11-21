This repository is a tool to help visualize a typical workflow. Input files are included, but due to the large size of the files, you can also try to download using wget:

"""
wget \https://storage.googleapis.com/gtex_analysis_v8/annotations/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt$ wget \https://github.com/swe4s/lectures/raw/master/data_integration/gtex/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz
"""

As visualized in the workflow attached, there are two steps that feed into a third step, which is a data visualization module:
The fisrt step



git filter-branch --tree-filter rm 'GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.gct' HEAD --ignore
