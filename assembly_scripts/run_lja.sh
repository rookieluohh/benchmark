lja="/path/to/lja"
input_fastq="/path/to/test.fastq"
output_dir="/path/to/output"

${lja} -t 30 --diploid --reads ${input_fastq} -o ${output_dir} 
