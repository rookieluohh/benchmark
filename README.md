# ASSca5 Criteria for Completeness and Accuracy of Assemblies Assessment
## Assessment
ASSca5 is a software package for the completeness and accuracy assessment for genome assemblies.  

&ensp;&ensp;&ensp;&ensp;ASSca5 concludes 5 criteria for the assessment of synthetic datasets, three criteria are used to measure completeness, namely completeness rate (CR), single-copy completeness rate (SCR), and duplicated completeness rate (DCR). To evaluate the assembly accuracy, we announces two criteria, the average proportion of the largest category (APLC), and the average distance difference (ADF).   
&ensp;&ensp;&ensp;&ensp;ASSca5 is a software package written in python. ASSca5 runs as a command-line program with a variety of user-options and is freely available for download below, compatible for Unix/Linux/Mac OS.  

## Synthetic Datasets
All synthetic datasets could be obtained with the following script  
``` wget -r -c -nH -np ftp://ftp.agis.org.cn/~panweihua/benchmark/ ```  
individual datasets could be gained from the following address:  
> Varying ploidy for eukaryotic genomes:  
``` ftp://ftp.agis.org.cn/~panweihua/benchmark/eukaryotic_genomes/varying_ploidy/ ```  
Varying coverage for eukaryotic genomes:  
``` ftp://ftp.agis.org.cn/~panweihua/benchmark/eukaryotic_genomes/varying_coverage/ ```  
Varying heterozygous for eukaryotic genomes:  
``` ftp://ftp.agis.org.cn/~panweihua/benchmark/eukaryotic_genomes/varying_heterozygous/ ```  
Varying precious rate for eukaryotic genomes:  
``` ftp://ftp.agis.org.cn/~panweihua/benchmark/eukaryotic_genomes/varying_precious_rate/ ```  
For metagenomes:  
``` ftp://ftp.agis.org.cn/~panweihua/benchmark/metagemones/ ```  

## Prerequisite
> * Python v3 (tested with Python v3.7.12) or higher
> * R v4 (tested with R v4.1.2) or higher (for plotting)
> * shell

## Installation
You can compile a static version using the following command  
``` git clone https://github.com/rookieluohh/benchmarke.gitcd benchmark ```  
``` make ``` 

## Usage
python Assessment.py [-h] -i INPUT -r REFERENCE [-k KMER_LENGTH] [-s SAMPLE] -o OUT_PREFIX  

In order to run this script successfully, these parameters must be passed in. `-i` is a parament passes in the input file of the script, and the input file must be the assembly with fasta format; `-r` passes in the reference genome file with fasta format; `-k` means the k-mer length used in the script to assess the assembly, and the default value is 21; `-s` means the number of reference unique k-mer used in the the assessment, the default value is "all", using all reference unique kmers to evaluate the assembly will be slow for some complex genomes, so randomly sampling some reference unique kmers for evaluation will greatly speed up the script and memory consumption, and we recommend the k is 200,000; `-o` passes in the prefix of output file name.

## Citation
If you ASSca5 in any published work, please cite the following manuscript:  
***Comprehensive Assessment of Eleven de novo HiFi Assemblers on Complex Eukaryotic Genomes and Metagenomes***

