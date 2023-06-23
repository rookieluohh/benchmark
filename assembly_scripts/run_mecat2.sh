# Perform mecat2 with hifi reads

mecat2="/path/to/mecat.pl"
config_file="/path/to/config_file"

# run mecat2
${mecat2} correct ${config_file}
${mecat2} trim ${config_file}
${mecat2} assemble ${config_file}
