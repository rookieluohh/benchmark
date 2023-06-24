# -*- coding: UTF-8 -*-

import argparse
import time
from pandas import *
from random import *
import os


def ArgParse():
    group = argparse.ArgumentParser(description='A python script for genome assessment.')
    group.add_argument('-i', '--input', help='assemble result with fasta format.', required=True)
    group.add_argument('-r', '--reference', help='reference sequence with fasta format.', required=True)
    group.add_argument('-k', '--kmer-length', type=int, help='the kmer length used in assessment, default=21.',default=21)
    group.add_argument('-o', '--out-prefix',help='prefix of output files.',required=True)
    group.add_argument('-s', '--sample', help='the number of ref unique kmer sampled, default=all.', default="all")

    return group.parse_args()

def integrateReadLine(fa, prefix):
    file_name = fa.split("/")[-1]
    fi = open(fa, "r")
    lines = fi.readlines()
    fi.close()
    fo = open(prefix + "_" + file_name, "w")
    n = "1"
    for line in lines:
        if line[0] == ">":
            if n == "1":
                fo.write(line)
            else:
                fo.write("\n" + line)
        else:
            n = "larger than 1"
            line = line.strip()
            fo.write(line)
    fo.close()
    print("[INFO] " + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + ", " + "Integrate read lines in " + fa + " file done.")

def reverseCompleKmer(kmer):
    reverse_complementary_kmer_list = []
    base_dic = {"A":"T","T":"A","C":"G","G":"C","N":"N","a":"T","t":"A","c":"G","g":"C"}
    for base in list(kmer[::-1]):
        reverse_complementary_kmer_list.append(base_dic[base])
    reverse_complementary_kmer = "".join(reverse_complementary_kmer_list)
    return min([kmer, reverse_complementary_kmer])

def refUniqueKmerSearch(ref, kmer_length):
    fi = open(ref, "r")
    lines = fi.readlines()
    fi.close()
    sumKmer_dic = {}
    for line in lines:
        line = line.strip()
        if line[0] != ">":
            for i in range(len(line) - kmer_length + 1):
                sumKmer_dic[reverseCompleKmer(line[i:i + kmer_length])] = sumKmer_dic.get(
                    reverseCompleKmer(line[i:i + kmer_length]), 0) + 1
    unique_kmer = {}
    for key, value in sumKmer_dic.items():
        if value == 1:
            unique_kmer[key] = 0
    external_dic = {}
    internal_dic = {}
    chr_name = ""
    for line in lines:
        line = line.strip().split()[0]
        if line != "":
            if line[0] == ">":
                chr_name = line[1:]
                internal_dic = {}
            else:
                for i in range(len(line) - kmer_length + 1):
                    kmer = line[i:i + kmer_length]
                    kmer = reverseCompleKmer(kmer)
                    if kmer in unique_kmer.keys():
                        internal_dic[kmer] = (i + 1, i + kmer_length)
                external_dic[chr_name] = internal_dic
    refChr_uniKmer = {}
    for K, V in external_dic.items():
        mydic = {}
        for key, value in V.items():
            if key in unique_kmer:
                mydic[key] = 1
        refChr_uniKmer[K] = mydic  # refChr_uniKmer = {"chr01":{"ATCG":1,...,"ATCG":1}...}
    print("[INFO] " + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + ", " + "Unique kmer count in " + ref + " file done.")
    with open("refUniKmer", "w") as fi:
        fi.write("{}\t{}\t{}\t{}\n".format("Chr", "Kmer", "Start", "End"))
        for key, value in external_dic.items():
            for k, v in value.items():
                fi.write("{}\t{}\t{}\t{}\n".format(key, k, v[0], v[1]))
            fi.write("\n")
    fi.close()
    return [refChr_uniKmer, unique_kmer]

def getRefUniKmerPos(ref, kmer_length):
    eachchr_unikmer = refUniqueKmerSearch(ref, kmer_length)[0]
    data = open(ref, "r")
    lines = data.readlines()
    data.close()
    kmerpos_dic = {}
    chr_name = ""
    for line in lines:
        line = line.strip().split()[0]
        if line[0] == ">":
            chr_name = line[1:]
            kmerpos_dic[chr_name] = {}
    for line in lines:
        line = line.strip().split()[0]
        if line[0] == ">":
            chr_name = line[1:]
        else:
            for i in range(len(line) - kmer_length + 1):
                if reverseCompleKmer(line[i:i + kmer_length]) in eachchr_unikmer[chr_name].keys():
                    kmerpos_dic[chr_name][(i + 1, i + kmer_length)] = 0
    print("[INFO] " + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + ", " + "Get reference unique kmer position done.")
    return kmerpos_dic  # kmerpos_dic={"chr1":{(1,21):0,...,(41,51):0},...}

def removeOverlapKmer(classed_kmer_dic):
    set_option('display.max_columns', None)
    set_option('display.max_rows', None)
    external_dic = {}
    internal_dic = {}
    for key, value in classed_kmer_dic.items():
        internal_dic = {}
        value_list = list(value.items())
        value_list.sort(key=lambda x: x[0][0], reverse=False)
        mydic = {}
        mydic["start_pos"] = [value_list[0][0][0]]
        mydic["end_pos"] = [value_list[0][0][1]]
        mydic["front_end_pos"] = [0]
        last_end_pos = value_list[0][0][1]
        for i in range(1,len(value_list)):
            mydic["start_pos"].append(value_list[i][0][0])
            mydic["end_pos"].append(value_list[i][0][1])
            mydic["front_end_pos"].append(last_end_pos)
            last_end_pos = value_list[i][0][1]
        mydataframe = DataFrame(mydic)
        mydataframe = mydataframe[(mydataframe["front_end_pos"] - mydataframe["start_pos"]) < 0]
        for i in mydataframe.index:
            internal_dic[(mydataframe["start_pos"][i],mydataframe["end_pos"][i])] = 0
        external_dic[key] = internal_dic
    print("[INFO] " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ", " + "Remove overlaps between kmers done.")
    return external_dic                    #external_dic{"chr/ctg":{(1,21):0,...,(31,51):0},...}

def getHeaderKmer(fasta, headerkmerpos_dic, kmer_length):
    data = open(fasta, "r")
    lines = data.readlines()
    data.close()
    kmer_pos_dic = {}
    seqname_kmer_dic = {}
    sequence_name = ""
    for line in lines:
        line = line.strip().split()[0]
        if line[0] == ">":
            sequence_name = line[1:]
            kmer_pos_dic = {}
        else:
            for key, value in headerkmerpos_dic.items():
                if sequence_name == key:
                    for pos in value.keys():
                        kmer_pos_dic[reverseCompleKmer(line[pos[0] - 1:pos[0] + kmer_length - 1])] = []
                    seqname_kmer_dic[sequence_name] = kmer_pos_dic
    for line in lines:
        line = line.strip().split()[0]
        if line[0] == ">":
            sequence_name = line[1:]
        else:
            for key, value in headerkmerpos_dic.items():
                if sequence_name == key:
                    for pos in value:
                        seqname_kmer_dic[sequence_name][reverseCompleKmer(line[pos[0] - 1: pos[0] + kmer_length - 1])].append(pos)
    print("[INFO] " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ", " + "Get header kmer done.")
    return seqname_kmer_dic  # seqname_kmer_dic={"chr/ctg":{"ATCG":[(1,21),...,(31,51)]},...}

def randomselectkmer(refkmerdic,sample_num):
    kmerdic = {}
    for key,value in refkmerdic.items():
        for k,v in value.items():
            kmerdic[k] = 0
    mylist = sample(list(kmerdic.items()),sample_num)
    newkmerdic = {}
    for i in mylist:
        newkmerdic[i[0]] = 0
    external_dic = {}
    for key,value in refkmerdic.items():
        internal_dic = {}
        for k,v in value.items():
            if k in newkmerdic.keys():
                internal_dic[k] = v
        external_dic[key] = internal_dic
    print("[INFO] " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ", random select 200000 reference kmer done.")
    return external_dic            # external_dic={"chr/ctg":{"ATCG":[(1,21),...,(31,51)]},...}

def getAsbkmer(ctgfile,reffile,refkmer_dic,kmer_length):
    refkmer = {}
    for key,value in refkmer_dic.items():
        for k,v in value.items():
            refkmer[k] = 0
    file = open(ctgfile,"r")
    lines = file.readlines()
    file.close()
    external_dic = {}
    internal_dic = {}
    ctgname = ""
    for line in lines:
        line = line.strip().split()[0]
        if line[0] == ">":
            ctgname = line[1:]
            internal_dic = {}
        else:
            for i in range(len(line) - kmer_length + 1):
                if reverseCompleKmer(line[i:i + kmer_length]) in refkmer.keys():
                    internal_dic[reverseCompleKmer(line[i:i + kmer_length])] = internal_dic.get(reverseCompleKmer(line[i:i + kmer_length]),[]) + [(i + 1, i + kmer_length)]
            external_dic[ctgname] = internal_dic
    print("[INFO] " + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + ", " + "Unique kmer from " + reffile + " file count in " + ctgfile + " file done.")
    return external_dic      # external_dic={"chr/ctg":{"ATCG":[(1,21),...,(31,51)]},...}

def assembleAssessment(ref_fa, asb_fa, kmer_length, sample_num, prefix):
    print("[INFO] " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ", Begin.")
    integrateReadLine(ref_fa, prefix)
    integrateReadLine(asb_fa, prefix)
    refUniKmerPos = getRefUniKmerPos(prefix + "_" + ref_fa.split("/")[-1], kmer_length)
    refHeaderKmerPos = removeOverlapKmer(refUniKmerPos)
    refUniKmerPos = None
    if sample_num == "all":
        refHeaderKmer = getHeaderKmer(prefix + "_" + ref_fa.split("/")[-1], refHeaderKmerPos, kmer_length)
    else:
        refheaderKmer = getHeaderKmer(prefix + "_" + ref_fa.split("/")[-1], refHeaderKmerPos, kmer_length)
        refHeaderKmer = randomselectkmer(refheaderKmer,sample_num)
    refheaderkmer = None
    refHeaderKmerPos = None
    asbHeaderKmer = getAsbkmer(prefix + "_" + asb_fa.split("/")[-1],prefix + "_" + ref_fa.split("/")[-1],refHeaderKmer,kmer_length)
    with  open("random_refHeaderkmer.dic","w") as file:
        file.write(str(refHeaderKmer))
    file.close()
    with open("refHeaderkmer.out", "w") as file:
        file.write("Chr\tKmer\tStart\tEnd\n")
        for key, value in refHeaderKmer.items():
            for k, v in value.items():
                file.write("{}\t{}\t{}\t{}\n".format(key, k, v[0][0], v[0][1]))
            file.write("\n")
    file.close()
    with open("asbHeaderkmer.out", "w") as file:
        file.write("Contig\tKmer\tStart\tEnd\n")
        for key, value in asbHeaderKmer.items():
            for k, v in value.items():
                for i in v:
                    file.write("{}\t{}\t{}\t{}\n".format(key, k, i[0], i[1]))
            file.write("\n")
    file.close()
    asbKmerCount = {}
    for Key, Value in asbHeaderKmer.items():
        for k, v in Value.items():
            asbKmerCount[k] = asbKmerCount.get(k, 0) + len(v)
    singleCopyKmerNum = 0
    duplicateKmerNum = 0
    colKmerNum = 0
    for key, value in refHeaderKmer.items():
        for k, v in value.items():
            colKmerNum += 1
    for key, value in asbKmerCount.items():
        if value == 1:
            singleCopyKmerNum += 1
        else:
            duplicateKmerNum += 1
    singleCopy = singleCopyKmerNum / colKmerNum
    print("[INFO] " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ", " + "Compute single copy rate done.")
    duplicateRate = duplicateKmerNum / colKmerNum
    print("[INFO] " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ", " + "Compute duplicate rate done.")
    ctgkmer_dic = {}
    for key, value in asbHeaderKmer.items():
        ctgkmer_dic[key] = {}
    for key, value in asbHeaderKmer.items():
        for k, v in value.items():
            if k not in ctgkmer_dic[key].keys():
                ctgkmer_dic[key][k] = 0  # ctgkmer_dic = {"ctg00001":{"ATCG":0,...,"ATCG":0},...}
    chrkmer_dic = {}
    for key, value in refHeaderKmer.items():
        chrkmer_dic[key] = {}
    for key, value in refHeaderKmer.items():
        for k, v in value.items():
            if k not in chrkmer_dic[key].keys():
                chrkmer_dic[key][k] = 0  # chrkmer_dic = {"Chr01":{"ATCG":0,...,"ATCG":0},...}
    chr_to_kmerlist = {}
    contig_to_chr = {}
    for ctg, ctgkmer in asbHeaderKmer.items():
        chr_to_kmerlist = {}
        for chr, chrkmer in refHeaderKmer.items():
            chr_to_kmerlist[chr] = {}
        contig_to_chr[ctg] = chr_to_kmerlist
    for asb_key, asb_value in ctgkmer_dic.items():
        for i in asb_value.keys():
            for ref_key, ref_value in chrkmer_dic.items():
                if i in ref_value.keys() and i not in contig_to_chr[asb_key][ref_key].keys():
                    contig_to_chr[asb_key][ref_key][i] = 0  # contig_to_chr={"ctg0001":{"chr01":{"ATCG":0,...,"ATCG":0},...},...}chr和ctg共有kmer
    print("[INFO] " + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + ", " + "Get collective header kmer from reference and assemble file done.")
    contig_to_kmer = {}
    for key, value in contig_to_chr.items():
        kmerlist = {}
        for k, v in value.items():
            for kmer, it in v.items():
                kmerlist[kmer] = 0
        contig_to_kmer[key] = kmerlist  # contig_to_kmer = {"ctg0001":{"ATCG":0,...,"ATCG":0},...}
    ctgkmer_dic = None
    chrkmer_dic = None
    proportion_of_the_largest_categories = 0
    largest_categories_ex = {}
    largest_categories_in = {}
    numerator = 0
    denominator = 0
    for key, value in contig_to_chr.items():  # 找出最大类
        largest_categories_num = 0
        largest_categories_in = {}
        for k, v in value.items():
            if len(v) > largest_categories_num:
                largest_categories_num = len(v)
        for k, v in value.items():
            if len(v) == largest_categories_num:
                largest_categories_in[k] = v
                largest_categories_ex[key] = largest_categories_in  # largest_categories_ex={"ctg0001":{"chr01":{"ATCG":0,...,"ATCG":0}},...}
        numerator += largest_categories_num
        denominator += len(contig_to_kmer[key])
    proportion_of_the_largest_categories += float(numerator) / float(denominator)
    print("[INFO] " + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + ", " + "Compute proportion of the largest categories done.")
    aveEachCtgDistance_sum = 0
    contig_to_chr = None
    with open("largest_categories.dic","w") as fi:
        fi.write(str(largest_categories_ex))
    fi.close()
    with open("refKmer.dic","w") as fi:
        fi.write(str(refHeaderKmer))
    fi.close()
    with open("asbKmer.dic","w") as fi:
        fi.write(str(asbHeaderKmer))
    fi.close()
    contig_nums = 0
    for key, value in largest_categories_ex.items():  # largest_categories_ex={"ctg0001":{"chr01":{"ATCG":0,...,"ATCG":0}},...}
        ref_base_pos_dic = {}
        asb_base_pos_dic = {}
        t = 0
        eachCtgDistance_sum = 0
        for k, v in value.items():
            if len(v) > 1:
                contig_nums += 1
                for i in range(len(v)):
                    ref_base_pos_dic[list(v.items())[i][0]] = refHeaderKmer[k][list(v.items())[i][0]]  # ref_base_pos_dic={"ATCG":[(1,21),...,(31,51)]}
                    asb_base_pos_dic[list(v.items())[i][0]] = asbHeaderKmer[key][list(v.items())[i][0]]
                ref_base_list = list(ref_base_pos_dic.items())
                ref_base_list.sort(key=lambda x: x[1][0][0], reverse=False)
                for i in range(len(ref_base_list) - 1):
                    refKmerDistance = abs(ref_base_list[i + 1][1][0][0] - ref_base_list[i][1][0][0])
                    asbKmerDistance = {}
                    for j in range(len(asb_base_pos_dic[ref_base_list[i][0]])):
                        for m in range(len(asb_base_pos_dic[ref_base_list[i + 1][0]])):
                            distance = abs(asb_base_pos_dic[ref_base_list[i][0]][j][0] - asb_base_pos_dic[ref_base_list[i + 1][0]][m][0])
                            asbKmerDistance[distance] = 0
                    for j in asbKmerDistance.keys():
                        eachCtgDistance_sum += abs(j - refKmerDistance)
                        t += 1
                aveEachCtgDistance_sum += eachCtgDistance_sum / t
        else:
            continue
    ave_distance_diff = aveEachCtgDistance_sum / contig_nums
    print("[INFO] " + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + ", " + "Compute average distance difference done." + "\n")
    print("{:<12.7f}Complete\n"
          "{:<12.7f}Complete and single-copy\n"
          "{:<12.7f}Complete and duplicated\n"
          "{:<12.7f}Proportion of the largest categories\n"
          "{:<12.7f}ave distance diff\n".format(singleCopy + duplicateRate, singleCopy, duplicateRate,proportion_of_the_largest_categories, ave_distance_diff))
    with open("result.report", "w") as fi:
        fi.write("{:<12.7f}Complete\n"
                 "{:<12.7f}Complete and single-copy\n"
                 "{:<12.7f}Complete and duplicated\n"
                 "{:<12.7f}Proportion of the largest categories\n"
                 "{:<12.7f}ave distance diff\n".format(singleCopy + duplicateRate, singleCopy, duplicateRate,proportion_of_the_largest_categories, ave_distance_diff))
        fi.close()

if __name__ == "__main__":
    opt = ArgParse()
    path = os.getcwd()
    asb_seq = opt.input
    ref_seq = opt.reference
    kmer_len = opt.kmer_length
    prefix = opt.out_prefix
    sample_num = int(opt.sample)
    asb_seq_path = os.path.join(path,asb_seq)
    ref_seq_path = os.path.join(path,ref_seq)
    assembleAssessment(ref_seq_path, asb_seq_path, kmer_len, sample_num, prefix)
