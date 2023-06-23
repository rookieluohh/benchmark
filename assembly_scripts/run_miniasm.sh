# Perform miniasm with hifi reads

minimap2="/path/to/minimap2"
miniasm="/path/to/miniasm"
output_dir="/path/to/output"
input_fastq="/path/to/test.fastq"

# run miniasm
${minimap2} -t 30 -x ava-pb ${input_fastq} ${input_fastq} | gzip -1 > ${output_dir}/test.paf.gz
${miniasm} -f ${input_fastq} ${output_dir}/test.paf.gz > ${output_dir}/test.gfa
awk '/^S/{print ">"$2"\n"$3}' ${output_dir}test.gfa > ${output_dir}/test.fasta
