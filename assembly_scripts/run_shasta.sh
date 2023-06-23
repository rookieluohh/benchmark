# Perform shasta with hifi reads

shasta="/path/to/shasta"
output_prefix="example"
output_dir="/path/to/output"
genome_size="392m"
input_fastq="/path/to/test.fastq"

# run shasta
${shasta}  --config HiFi-Oct2021 --input ${input_fastq}  --assemblyDirectory ${output_dir}/${output_prefix}  --command assemble  --threads 30
