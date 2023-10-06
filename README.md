# ASSca5 Criteria for Completeness and Accuracy of Assemblies Assessment
## Assessment
ASSca5 is a software package for the completeness and accuracy assessment for genome assemblies.  

ASSca5 concludes 5 criteria for the assessment of synthetic datasets, three criteria are used to measure completeness, namely completeness rate (CR), single-copy completeness rate (SCR), and duplicated completeness rate (DCR). To evaluate the assembly accuracy, we announces two criteria, the average proportion of the largest category (APLC), and the average distance difference (ADF).   

ASSca5 is a software package written in python. ASSca5 runs as a command-line program with a variety of user-options and is freely available for download below, compatible for Unix/Linux/Mac OS.  


## Synthetic Datasets
For linux user, all synthetic datasets could be obtained with the following script:  
``` wget -r -c -nH -np ftp://ftp.agis.org.cn/~panweihua/benchmark/ ```  
individual datasets could be gained from the following address:  
> Varying ploidy for eukaryotic genomes:  
``` ftp://ftp.agis.org.cn/~panweihua/benchmark/assembly_software_benchmark/eukaryotic_genomes/varying_ploidy/ ```  
Varying coverage for eukaryotic genomes:  
``` ftp://ftp.agis.org.cn/~panweihua/benchmark/assembly_software_benchmark/eukaryotic_genomes/varying_coverage/ ```  
Varying heterozygous for eukaryotic genomes:  
``` ftp://ftp.agis.org.cn/~panweihua/benchmark/assembly_software_benchmark/eukaryotic_genomes/varying_heterozygous/ ```  
Varying precious rate for eukaryotic genomes:  
``` ftp://ftp.agis.org.cn/~panweihua/benchmark/assembly_software_benchmark/eukaryotic_genomes/varying_precious_rate/ ``` 
Human diploid genomes:  
``` ftp://ftp.agis.org.cn/~panweihua/benchmark/assembly_software_benchmark/eukaryotic_genomes/human_diploid/ ```  
For metagenomes:  
``` ftp://ftp.agis.org.cn/~panweihua/benchmark/assembly_software_benchmark/metagenomes/ ```  

And for windows user, you can access all synthetic datasets with following URL:  
``` http://ftp.agis.org.cn:8888/~panweihua/benchmark/ ```


## Prerequisite
> * Python v3 (tested with Python v3.7.12) or higher
> * pandas v1.1.4
> * shell

## Installation
You can compile a static version using the following command:  
``` git clone https://github.com/rookieluohh/benchmark ```  
``` cd benchmark ``` 

## Usage
`Assessment.py` is a python script used a reference genome and a assembly to assess synthetic datasets, which contains 5 parameters:  

    python Assessment.py [-h] -i INPUT -r REFERENCE [-k KMER_LENGTH] [-s SAMPLE] -o OUT_PREFIX  

where `-i` sets a input file of fasta format in use; `-r` sets the reference genome of assembly with fasta format; `-k` specifies the k-mer length used to assess the assembly, and the default value is `21`; `-s` means the number of reference unique k-mer used in the the assessment, the default value is `"all"`, using all reference unique kmers to assess the assembly will be slow for some complex genomes, so randomly sampling some reference unique kmers for assessment will greatly speed up the script and memory consumption, and we recommend the k is `200,000`; `-o` specifies the prefix of output files. 

For example, a typical assessment command line looks like:  

    python Assessment.py -i haplotype.fasta -r haplotype_ref.fasta -o test  

If the process of this script is running out of memory or too slow, we recommend you to use `-s` parameter:

    python Assessment.py -i haplotype.fasta -r haplotype_ref.fasta -s 200000 -o test 


## Citation
If you ASSca5 in any published work, please cite the following manuscript:  
***Comprehensive Assessment of Eleven de novo HiFi Assemblers on Complex Eukaryotic Genomes and Metagenomes***

