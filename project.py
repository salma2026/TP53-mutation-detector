from Bio.Seq import Seq
import os
from datetime import datetime
from tabulate import tabulate
import sys


def main():
    try:
        file = input("File: ")
        raw_DNA = read_DNA("sequence.txt")
        raw_user = read_DNA(file)
        healthy = split_DNA(raw_DNA)
        if check_DNA(file):
            usersfile = split_DNA(raw_user)
        else:
            sys.exit("incorrect file")
        compare_nucleotides = comparison(healthy, usersfile)
        healthy_protein = translate(healthy)
        users_protein = translate(usersfile)
        protein_comparison = comparison(healthy_protein, users_protein)
        if raw_DNA == raw_user:
            print("no mutation detected")
        else:
            full = output(general(read_DNA(file), compare_nucleotides, protein_comparison))
            print(full)
            ask(full)
    except FileNotFoundError:
        print("file not found")
    except IndexError:
        print("DNA is shortend")

def read_DNA(file):
    DNA = []
    with open(file, "r") as file:
        for i in file:
            if i.startswith(">"):
                continue
            i = i.strip("\n")
            DNA.append(i)
    complete = "".join(DNA)
    return complete


def check_DNA(check):
    name, ending = os.path.splitext(check)
    if ending == ".fasta" or ending == ".txt" or ending == ".fa" or ending == ".fna":
        with open(check, "r") as file:
            for i in file:
                if i.startswith(">"):
                    if "TP53" in i:
                        return True
                    else:
                        return False
    else:
        sys.exit("incorrect file")


def split_DNA(DNA):
    splitted_DNA = []
    for i in range(0, len(DNA), 3):
        splitted_DNA.append(DNA[i:i+3])
    return splitted_DNA


def comparison(blueprint, final):
    incorrect = []
    for index, codon in enumerate(blueprint):
        if blueprint[index] != final[index]:
            incorrect.append((codon, final[index], index))
    return incorrect


def translate(raw):
    j = "".join(raw)
    s = Seq(j)
    n = s.translate(cds=True)
    return n

def general(number, diff_DNA, diff_protein):
    dic = {}
    i = len(number)
    i3 = int(len(number)/3)
    dic["Target gene"] = "TP53"
    dic["Total nucleotides"] = f"{i} bp"
    dic["Codons"] = i3
    dic["Total nucleotides changes"] = len(diff_DNA)
    dic["Total amino acid changes"] = len(diff_protein)
    if len(diff_DNA) > 1:
       DNA = list(zip(*diff_DNA))
       protein = list(zip(*diff_protein))
       dic["Original N"], dic["Mutated N"], dic["N index"] = DNA
       dic["Original AA"], dic["Mutated AA"], dic["AA index"] = protein
    else:
       dic["Original N"], dic["Mutated N"], dic["N index"] = diff_DNA[0]
       dic["Original AA"], dic["Mutated AA"], dic["AA index"] = diff_protein[0]
    c = dic.items()
    return c


def output(i):
    width, height = os.get_terminal_size()
    first = f"{'Mutation analysis':^{width}}"
    second = f"{'':=^{width}}"
    t = tabulate(i, tablefmt="plain")
    d = datetime.today()
    return f"{second}\n{first}\n{second}\n{t}\n{second}\n{d}"


def ask(o):
    q = input("do you want to download the report?[y/n]")
    if q == "y" or q == "yes" or q == "ye":
        name = input("what would you like be the name of the file?")
        with open(f"{name}.txt", "w") as file:
            file.write(o)
    else:
        sys.exit()


if __name__ == "__main__":
    main()
