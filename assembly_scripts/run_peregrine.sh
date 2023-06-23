# Perform peregrine with hifi reads

peregrine="/path/to/peregrine/target/release/pg_asm"
output_prefix="example"
output_dir="/path/to/output"
reads_path_file="/path/to/reads.lst" # the hifi reads path file

# run peregrine
${peregrine} ${reads_path_file} ${output_prefix} 30
