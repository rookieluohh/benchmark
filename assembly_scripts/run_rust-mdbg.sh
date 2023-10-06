rust_mdbg="/path/to/rust-mdbg"
output_prefix="example"
input_fastq="/path/to/test.fastq"

${rust_mdbg} -k 21 --density 0.003 -l 14 --prefix ${output_prefix} --threads 30 ${input_fastq}
