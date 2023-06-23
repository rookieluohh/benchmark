# Perform hicanu with hifi reads

canu="/path/to/canu"
output_prefix="example"
output_dir="/path/to/output"
genome_size="392m"
input_fastq="/path/to/test.fastq"

# run hicanu
${canu} -p ${output_prefix} -d ${output_dir}  genomeSize=${genome_size} useGrid=false merylThreads=30 hapThreads=30 cormhapThreads=30 obtovlThreads=30 utgovlThreads=30 corThreads=30 ovbThreads=30 ovsThreads=30 redThreads=30 oeaThreads=30 batThreads=30 cnsThreads=30  -pacbio-hifi ${input_fastq}
