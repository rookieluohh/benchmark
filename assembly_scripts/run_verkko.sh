# Perform verkko with hifi reads

verkko="/path/to/verkko"
output_dir="/path/to/output"
input_fastq="/path/to/test.fastq"

# run verkko
${verkko} -d ${output_dir} --hifi ${input_fastq} --threads 30 --sto-run 30 100 24 --mer-run 30 100 24 --ovb-run 30 100 24 --ovs-run 30 100 24 --red-run 30 100 24 --mbg-run 30 100 24 --utg-run 30 100 24 --spl-run 30 100 24 --ali-run 30 100 24 --pop-run 30 100 24 --utp-run 30 100 24 --lay-run 30 100 24 --sub-run 30 100 24 --par-run 30 100 24 --cns-run 30 100 24
