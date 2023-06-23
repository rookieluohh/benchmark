# Perform hifiasm with hifi reads

hifiasm="/path/to/hifiasm"
output_prefix="example"
input_fastq="/path/to/test.fastq"

# run hifiasm
${hifiasm} -o ${output_prefix} -t 30 ${input_fastq}
