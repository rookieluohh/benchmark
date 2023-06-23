# ASSca5 Criteria for Completeness and Accuracy of Assemblies Assessment
## Assessment
ASSca5 is a software package for the completeness and accuracy assessment for genome assemblies.
ASSca5 concludes 5 criteria for the assessment of synthetic datasets, three criteria are used to measure completeness, namely completeness rate (CR), single-copy completeness rate (SCR), and duplicated completeness rate (DCR). To evaluate the assembly accuracy, we announces two criteria, the average proportion of the largest category (APLC), and the average distance difference (ADF). 
ASSca5 is a software package written in python. ASSca5 runs as a command-line program with a variety of user-options and is freely available for download below, compatible for Unix/Linux/Mac OS.

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
GCC version 4.8.1 or higher (for c++11) R version 3.2.3 or higher (for plotting)

## Installation
You can directly download the binary files here. If you want to install PRSice, all you have to do is (The binary file will located in PRSice)
git clone https://github.com/choishingwan/PRSice.gitcd PRSice
g++ --std=c++11 -I inc/ -isystem lib/ -DNDEBUG -O3 -march=native src/*.cpp -lz -lpthread -o PRSice
Or if you have CMake version 3.1 or higher, you can do (The binary file will located in PRSice/bin)
git clone https://github.com/choishingwan/PRSice.gitcd PRSice
mkdir buildcd build
cmake ../
make

## Rosalind users
You can compile a static version using the following command
git clone https://github.com/choishingwan/PRSice.gitcd PRSice
make

## Citation
If you ASSca5 in any published work, please cite the following manuscript:
xxxxxx

## Note to Self
PLINK PRS range is inclusive. e.g. 0 - 0.5 includes also SNPs with p-value of 0 and 0.5
