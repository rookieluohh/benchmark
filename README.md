# A benchmark assembly assessment script
# Introduction
Here is included a evaluation python scripts for simulated genome assembly, and we have five criterias to assess simulated assembly comprehensively. Three criterias are denoted for the completeness assessment for the simulated data, namely complete rate (CR), single-copy complete rate(SCR), and duplicated complete rate (DCR).The rest two criterias are denoted for accuracy assessment, one is the average proportion of the largest category (APLC), another is average distance difference (ADF).

The more information about the five criterias please refer this article:  
`Comprehensive benchmarking of de novo assemblers of HiFi sequencing data for complex eukaryotic genomes and metagenomes`

# Usage
    python Assessment.py [-h] -i INPUT -r REFERENCE [-k KMER_LENGTH] [-s SAMPLE] -o OUT_PREFIX
In order to run this script successfully, these parameters must be passed in. `-i` is a parament passes in the input file of the script, and the input file must be the assembly with fasta format; `-r` passes in the reference genome file with fasta format; `-k` means the k-mer length used in the script to assess the assembly, and the default value is 21; `-s` means the number of reference unique k-mer used in the the assessment, the default value is "all", using all reference unique kmers to evaluate the assembly will be slow for some complex genomes, so randomly sampling some reference unique kmers for evaluation will greatly speed up the script and memory consumption, and we recommend the k is 200,000; `-o` passes in the prefix of output file name.
