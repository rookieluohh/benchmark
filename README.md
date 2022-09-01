# Benchmark assembly assessment script
# Introduction
Here is included a evaluation python scripts for simulated genome assembly, and we have five criterias to assess simulated assembly comprehensively. 
Three criterias are denoted for the completeness assessment for the simulated data, namely complete rate (CR), single-copy complete rate(SCR), and duplicated complete rate (DCR).
The rest two criterias are denoted for accuracy assessment, one is the average proportion of the largest category (APLC), another is average distance difference (ADF).

# Usage
    python Assessment.py [-h] -i INPUT -r REFERENCE [-k KMER_LENGTH] [-s SAMPLE] -o OUT_PREFIX
