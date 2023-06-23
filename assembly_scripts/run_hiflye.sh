# Perform hiflye with hifi reads

flye="/path/to/flye"
output_dir="/path/to/output"
genome_size="392m"
input_fastq="/path/to/test.fastq"

# run hiflye
${flye} --pacbio-hifi ${input_fastq} -o ${output_dir} --genome-size ${genome_size} --threads=30
