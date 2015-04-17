import time

__author__ = 'Carl Rodriguez'
#I did not work together with anyone else on this project

def lcs_dyn(a, b):
    m = len(a)
    n = len(b)
    answer = ""
    myArr = [[0 for x in range(m + 1)] for y in range(n + 1)]
    myArr2 = [[0 for x in range(m + 1)] for y in range(n + 1)]

    for i in range(1, m + 1):
        if i%100 == 0:
            print("Done: ", i)
        for j in range(1, n + 1):
            if b[j - 1] == a[i - 1]:
                myArr[i][j] = myArr[i - 1][j - 1] + 1
                myArr2[i][j] = 2
            elif myArr[i][j - 1] >= myArr[i - 1][j]:
                myArr[i][j] = myArr[i][j - 1]
                myArr2[i][j] = 1
            else:
                myArr[i][j] = myArr[i - 1][j]
                myArr2[i][j] = 0

    x = m
    y = n
    answer = ""

    while x > 0 and y > 0:
        if myArr2[x][y] == 2:
            answer = a[x - 1] + answer
            x -= 1
            y -= 1
        elif myArr2[x][y] == 1:
            y -= 1
        else:
            x -= 1
    print(answer, " is the match")

    return myArr[i][j]


def lcs_brute(a, b):
    max = 0
    tmp = 0
    start = 0
    longest = ""
    test = ""
    for i in range(0, 2 ** len(a)):
        for j in range(0, len(a)):
            if (i // (2 ** j)) % 2 == 0:
                test += a[j]
        if len(test) < max:
            tmp = 0
        else:
            tmp = match(test, b)
        if tmp > max:
            max = tmp
            longest = test
        test = ""
    print(longest, " is the match")
    return max


def match(a1, b2):
    track = 0
    if len(a1) == 0:
        return 0
    for i in range(0, len(b2)):
        if a1[track] == b2[i]:
            track += 1
            if track == len(a1):
                return track
        i += 1
    return track


def printArr(multi):
    for j in range(0, len(multi[0])):
        for i in range(0, len(multi)):
            print(multi[i][j], end=" ")
        print()

def lcs_brute2(a, b):
    max = 0
    tmp = 0
    start = 0
    longest = ""
    test = ""
    binary = ""
    for i in range(0, 2 ** len(a)):
        for j in range(0, len(a)):
            if (i // (2 ** j)) % 2 == 0:
                binary+="1"
                test += a[j]
            else:
                binary += "0"
        if len(test) < max:
            tmp = 0
        else:
            tmp = match(test, b)
        if tmp > max:
            max = tmp
            longest = test
            print(binary," current max")
        else:
            print(binary)
        binary = ""
        test = ""
    print(longest, " is the match")
    return max


before = time.time()
print("Size = 10 brute:")
a10 = "TGTTTCCCGT"
b10="GCTCGCATTA"
before = time.time()
print(lcs_brute(a10, b10))
after = time.time()
print(after - before, " seconds elapsed")
print()

before = time.time()
print("Size = 10 Dynamic:")
a10 = "TGTTTCCCGT"
b10="GCTCGCATTA"
before = time.time()
print(lcs_dyn(a10, b10), "is longest substring")
after = time.time()
print(after - before, " seconds elapsed")
print()

print("Size = 15 brute:")
a15 = "GATTTAGATTATTGC"
b15 = "AGGTCTAGAATATTG"
before = time.time()
print(lcs_brute(a15, b15))
after = time.time()
print(after - before, " seconds elapsed")
print()

print("Size = 15 Dynamic: ")
a15 = "GATTTAGATTATTGC"
b15 = "AGGTCTAGAATATTG"
before = time.time()
print(lcs_dyn(a15, b15), "is longest substring")
after = time.time()
print(after - before, " seconds elapsed")
print()


print("Size = 20 brute:")
a20 = "CCGCTTCTTAAGGGAGTATA"
b20 = "GGATAGACGATCGTCTCAAA"
before = time.time()
#print(lcs_brute(a20, b20))
after = time.time()
print(after-before, " seconds elapsed")
print()

print("Size = 20 Dynamic: ")
a20 = "CCGCTTCTTAAGGGAGTATA"
b20 = "GGATAGACGATCGTCTCAAA"
before = time.time()
print(lcs_dyn(a20,b20),"is longest substring")
after = time.time()
print(after-before, " seconds elapsed")
print()

print("Size = 100 Dynamic: ")
a100 = "TGTGTGACTTCCTGGCTACTACCCGTTGCATCTAGTTACAGGTATCACTAACGTCTGATTATGCAGCTCCCAATTAGGGCCGTGTGTCAGGACTTTTTGA"
b100 = "CGGGTTCGCCCGCGGGAGTAACTGTTACAGCAAAGTACTGTACCGCAACGCTGGGGATGATATGTACGGGGCTTGTGTGATTAGACAGGGCCTGAGCTCC"
before = time.time()
print(lcs_dyn(a100,b100),"is longest substring")
after = time.time()
print(after-before, " seconds elapsed")
print()

print("Size = 1000 Dynamic: ")
a1000 = "AAGTTGGTACCCTCTATTTATGCCCGGATCTTGATCTCCAGACAGGGGGTAAAGGCATGGGCCAGTTACTACCCGTATTTAGGTTGTATTCCGCATCTGAAGGCGCCGTAGTGA" \
    "TAGGCGCTGAACTGAATGCATAATGGCCAATTTGACACCTGTGGTTGTCCTCACCAATACCTGGCCCTGTCGCTCCTAATACCCCGAAGCATAGAGCAGGTCCTAACCGGATAA" \
    "CTCAGCTAACAGAAACTCCCCCAAGAACTAAGCACACCCAATGTGAACGTAGTCCGCTAGTGCTAGCGCTTCCTTACAGCCTTTCCTTATGGTATCTATGAGCTGGCCTAGTAT" \
    "ACAGGTTCTCCGACAACCAAGCCTCTCGCTGCGTTCGAGCACTGCCCGATGGCTTTGACGCGAGAGCGCTGGGTCTCATAATAAGATGGGGCGCTGTAGCGTAGTATCCCTCTC" \
    "GAGGGGACCCCGTAATGATGACATAGGTACATGCTGATAGAGGGGTCGACGGTCATTAATAACGTCCGGCTCGGCCACCCCTAGACTAGAGGGGAGAAGTTTCAGTATCTCTCG" \
    "TTTTGAATGGTACATATAAGCCTAAAGACGAGGGTAGGGTCACTAAAACTAAGTGAGCAACGTGCGGTACTGTCCTAGGCGGGCTTGACATTATACTCACTACGTTGGTTTCGC" \
    "GATGAGTCACAGGACTTTTCAGACCATGTGTCTGCCTCTAGGACCAATGGCTGGGTGTTGGTATACAACAGAGTCATTCATTTACGTCGTATATTCTAATACCACTCTTCACAC" \
    "GTCGAAATTTTCTGAGTTTCGACTACGCTTGTGAGCACTTCCTACTTGGTTAAGCAAGTGTGGGACGGCCTTCTTGGGCCAGGACGTAGGTTCCGCTGACAGTACAACGGAGAC" \
    "CAGAAAAGCTATTCAAGAGAGACATGGTACAGTTCTGTATGCATAAGCGTGCCCCTTAGCGCAACTGGCGTATACCGTCGATTCAGGG"

b1000= 'GTTCGTTCATGACTGTCTAAACCTATTCGACGTGCGCCCTTTAGAGGATCATTCTAGATT'\
   'GTATGAGACCGATAAGATGAACATTTTATCAATTCCGCGCGGGGCTACAATATGATCTTG'\
   'ATAATTGTGGTATAAGAGACGATAAAGGCGATTTTCTATCAATCCATCTGACAAACCGTC'\
   'TCTAGCATCAATGCAACGCGTTTGGTTGGCCTAGTGGCGTTAGTGAATGGGGACCAGTTC'\
   'AGTATCGCCCATCGGACTTGAACAATAAGCGTGAACGGACCCAAACTTTTATGCCCGGCC'\
   'GGTTTCGACCCCGTTGCGACGAGTTATCATTTCAGCACGAGGACATGGTCCCGGTTTGAG'\
   'ACTCGTAAAACCCTACCTAGCACGGTATTCCGGACACTAATATAAAATGAATACCTGCGA'\
   'TAATAGATCAAGCGCTACAGCCCGGGCCCAGCTACCCGGATATAAATCTAAATGTTGCAT'\
   'AAACCATTATTGTACCTCAACTTGAGTTCGATAGGCCGCGCACTGTGGCTTTGCCATGCC'\
   'TACGCTTCACCATAGACTACACGTGAAAATTCGCATTAGCCTACACGACACGCCCGAGTC'\
   'TAAATGTTCCTCGAAGAACAATGTTGCCAAAGTTCTATTGATTACACACAAGCGCACTAA'\
   'AAGACAAAATTTATGGCCAGGGGCGGTAGTAGAATAGCAAGGTGAGTTGTTCGCAGGCTA'\
   'CATGCGATGCGATAGTATACTCGCGACCGGAGGGGGTCCCACACCCTTATGCTGATATTG'\
   'CTTATGCATATGGCTACGATACAGCCGAAACCAAACGGCTAAATATTAGTACCTAGTTTC'\
   'GAAAACATGGCTTGCGCATCACCTTCCATAAGGACGACGTCGAGCCAAGCGCATAGAAGG'\
   'CTTTATAATTATAAGGACAATGGGGACATCTCGTCCTGGTGTATTCGTCCAAGTGCTTGG'\
   'TGAAATCATCACGACCCATAGATGCTTCATCAGCATCATC'
before = time.time()
print(lcs_dyn(a1000,b1000),"is longest substring")
after = time.time()
print(after-before, " seconds elapsed")
a10000 = "AAGTTGGTACCCTCTATTTATGCCCGGATCTTGATCTCCAGACAGGGGGTAAAGGCATGGGCCAGTTACTACCCGTATTTAGGTTGTATTCCGCATCTGAAGGCGCCGTAGTGA" \
    "TAGGCGCTGAACTGAATGCATAATGGCCAATTTGACACCTGTGGTTGTCCTCACCAATACCTGGCCCTGTCGCTCCTAATACCCCGAAGCATAGAGCAGGTCCTAACCGGATAA" \
    "CTCAGCTAACAGAAACTCCCCCAAGAACTAAGCACACCCAATGTGAACGTAGTCCGCTAGTGCTAGCGCTTCCTTACAGCCTTTCCTTATGGTATCTATGAGCTGGCCTAGTAT" \
    "ACAGGTTCTCCGACAACCAAGCCTCTCGCTGCGTTCGAGCACTGCCCGATGGCTTTGACGCGAGAGCGCTGGGTCTCATAATAAGATGGGGCGCTGTAGCGTAGTATCCCTCTC" \
    "GAGGGGACCCCGTAATGATGACATAGGTACATGCTGATAGAGGGGTCGACGGTCATTAATAACGTCCGGCTCGGCCACCCCTAGACTAGAGGGGAGAAGTTTCAGTATCTCTCG" \
    "TTTTGAATGGTACATATAAGCCTAAAGACGAGGGTAGGGTCACTAAAACTAAGTGAGCAACGTGCGGTACTGTCCTAGGCGGGCTTGACATTATACTCACTACGTTGGTTTCGC" \
    "GATGAGTCACAGGACTTTTCAGACCATGTGTCTGCCTCTAGGACCAATGGCTGGGTGTTGGTATACAACAGAGTCATTCATTTACGTCGTATATTCTAATACCACTCTTCACAC" \
    "GTCGAAATTTTCTGAGTTTCGACTACGCTTGTGAGCACTTCCTACTTGGTTAAGCAAGTGTGGGACGGCCTTCTTGGGCCAGGACGTAGGTTCCGCTGACAGTACAACGGAGAC" \
    "CAGAAAAGCTATTCAAGAGAGACATGGTACAGTTCTGTATGCATAAGCGTGCCCCTTAGCGCAACTGGCGTATACCGTCGATTCAGGG"\
"AAGTTGGTACCCTCTATTTATGCCCGGATCTTGATCTCCAGACAGGGGGTAAAGGCATGGGCCAGTTACTACCCGTATTTAGGTTGTATTCCGCATCTGAAGGCGCCGTAGTGA" \
    "TAGGCGCTGAACTGAATGCATAATGGCCAATTTGACACCTGTGGTTGTCCTCACCAATACCTGGCCCTGTCGCTCCTAATACCCCGAAGCATAGAGCAGGTCCTAACCGGATAA" \
    "CTCAGCTAACAGAAACTCCCCCAAGAACTAAGCACACCCAATGTGAACGTAGTCCGCTAGTGCTAGCGCTTCCTTACAGCCTTTCCTTATGGTATCTATGAGCTGGCCTAGTAT" \
    "ACAGGTTCTCCGACAACCAAGCCTCTCGCTGCGTTCGAGCACTGCCCGATGGCTTTGACGCGAGAGCGCTGGGTCTCATAATAAGATGGGGCGCTGTAGCGTAGTATCCCTCTC" \
    "GAGGGGACCCCGTAATGATGACATAGGTACATGCTGATAGAGGGGTCGACGGTCATTAATAACGTCCGGCTCGGCCACCCCTAGACTAGAGGGGAGAAGTTTCAGTATCTCTCG" \
    "TTTTGAATGGTACATATAAGCCTAAAGACGAGGGTAGGGTCACTAAAACTAAGTGAGCAACGTGCGGTACTGTCCTAGGCGGGCTTGACATTATACTCACTACGTTGGTTTCGC" \
    "GATGAGTCACAGGACTTTTCAGACCATGTGTCTGCCTCTAGGACCAATGGCTGGGTGTTGGTATACAACAGAGTCATTCATTTACGTCGTATATTCTAATACCACTCTTCACAC" \
    "GTCGAAATTTTCTGAGTTTCGACTACGCTTGTGAGCACTTCCTACTTGGTTAAGCAAGTGTGGGACGGCCTTCTTGGGCCAGGACGTAGGTTCCGCTGACAGTACAACGGAGAC" \
    "CAGAAAAGCTATTCAAGAGAGACATGGTACAGTTCTGTATGCATAAGCGTGCCCCTTAGCGCAACTGGCGTATACCGTCGATTCAGGG"\
"AAGTTGGTACCCTCTATTTATGCCCGGATCTTGATCTCCAGACAGGGGGTAAAGGCATGGGCCAGTTACTACCCGTATTTAGGTTGTATTCCGCATCTGAAGGCGCCGTAGTGA" \
    "TAGGCGCTGAACTGAATGCATAATGGCCAATTTGACACCTGTGGTTGTCCTCACCAATACCTGGCCCTGTCGCTCCTAATACCCCGAAGCATAGAGCAGGTCCTAACCGGATAA" \
    "CTCAGCTAACAGAAACTCCCCCAAGAACTAAGCACACCCAATGTGAACGTAGTCCGCTAGTGCTAGCGCTTCCTTACAGCCTTTCCTTATGGTATCTATGAGCTGGCCTAGTAT" \
    "ACAGGTTCTCCGACAACCAAGCCTCTCGCTGCGTTCGAGCACTGCCCGATGGCTTTGACGCGAGAGCGCTGGGTCTCATAATAAGATGGGGCGCTGTAGCGTAGTATCCCTCTC" \
    "GAGGGGACCCCGTAATGATGACATAGGTACATGCTGATAGAGGGGTCGACGGTCATTAATAACGTCCGGCTCGGCCACCCCTAGACTAGAGGGGAGAAGTTTCAGTATCTCTCG" \
    "TTTTGAATGGTACATATAAGCCTAAAGACGAGGGTAGGGTCACTAAAACTAAGTGAGCAACGTGCGGTACTGTCCTAGGCGGGCTTGACATTATACTCACTACGTTGGTTTCGC" \
    "GATGAGTCACAGGACTTTTCAGACCATGTGTCTGCCTCTAGGACCAATGGCTGGGTGTTGGTATACAACAGAGTCATTCATTTACGTCGTATATTCTAATACCACTCTTCACAC" \
    "GTCGAAATTTTCTGAGTTTCGACTACGCTTGTGAGCACTTCCTACTTGGTTAAGCAAGTGTGGGACGGCCTTCTTGGGCCAGGACGTAGGTTCCGCTGACAGTACAACGGAGAC" \
    "CAGAAAAGCTATTCAAGAGAGACATGGTACAGTTCTGTATGCATAAGCGTGCCCCTTAGCGCAACTGGCGTATACCGTCGATTCAGGG"\
"AAGTTGGTACCCTCTATTTATGCCCGGATCTTGATCTCCAGACAGGGGGTAAAGGCATGGGCCAGTTACTACCCGTATTTAGGTTGTATTCCGCATCTGAAGGCGCCGTAGTGA" \
    "TAGGCGCTGAACTGAATGCATAATGGCCAATTTGACACCTGTGGTTGTCCTCACCAATACCTGGCCCTGTCGCTCCTAATACCCCGAAGCATAGAGCAGGTCCTAACCGGATAA" \
    "CTCAGCTAACAGAAACTCCCCCAAGAACTAAGCACACCCAATGTGAACGTAGTCCGCTAGTGCTAGCGCTTCCTTACAGCCTTTCCTTATGGTATCTATGAGCTGGCCTAGTAT" \
    "ACAGGTTCTCCGACAACCAAGCCTCTCGCTGCGTTCGAGCACTGCCCGATGGCTTTGACGCGAGAGCGCTGGGTCTCATAATAAGATGGGGCGCTGTAGCGTAGTATCCCTCTC" \
    "GAGGGGACCCCGTAATGATGACATAGGTACATGCTGATAGAGGGGTCGACGGTCATTAATAACGTCCGGCTCGGCCACCCCTAGACTAGAGGGGAGAAGTTTCAGTATCTCTCG" \
    "TTTTGAATGGTACATATAAGCCTAAAGACGAGGGTAGGGTCACTAAAACTAAGTGAGCAACGTGCGGTACTGTCCTAGGCGGGCTTGACATTATACTCACTACGTTGGTTTCGC" \
    "GATGAGTCACAGGACTTTTCAGACCATGTGTCTGCCTCTAGGACCAATGGCTGGGTGTTGGTATACAACAGAGTCATTCATTTACGTCGTATATTCTAATACCACTCTTCACAC" \
    "GTCGAAATTTTCTGAGTTTCGACTACGCTTGTGAGCACTTCCTACTTGGTTAAGCAAGTGTGGGACGGCCTTCTTGGGCCAGGACGTAGGTTCCGCTGACAGTACAACGGAGAC" \
    "CAGAAAAGCTATTCAAGAGAGACATGGTACAGTTCTGTATGCATAAGCGTGCCCCTTAGCGCAACTGGCGTATACCGTCGATTCAGGG"\
"AAGTTGGTACCCTCTATTTATGCCCGGATCTTGATCTCCAGACAGGGGGTAAAGGCATGGGCCAGTTACTACCCGTATTTAGGTTGTATTCCGCATCTGAAGGCGCCGTAGTGA" \
    "TAGGCGCTGAACTGAATGCATAATGGCCAATTTGACACCTGTGGTTGTCCTCACCAATACCTGGCCCTGTCGCTCCTAATACCCCGAAGCATAGAGCAGGTCCTAACCGGATAA" \
    "CTCAGCTAACAGAAACTCCCCCAAGAACTAAGCACACCCAATGTGAACGTAGTCCGCTAGTGCTAGCGCTTCCTTACAGCCTTTCCTTATGGTATCTATGAGCTGGCCTAGTAT" \
    "ACAGGTTCTCCGACAACCAAGCCTCTCGCTGCGTTCGAGCACTGCCCGATGGCTTTGACGCGAGAGCGCTGGGTCTCATAATAAGATGGGGCGCTGTAGCGTAGTATCCCTCTC" \
    "GAGGGGACCCCGTAATGATGACATAGGTACATGCTGATAGAGGGGTCGACGGTCATTAATAACGTCCGGCTCGGCCACCCCTAGACTAGAGGGGAGAAGTTTCAGTATCTCTCG" \
    "TTTTGAATGGTACATATAAGCCTAAAGACGAGGGTAGGGTCACTAAAACTAAGTGAGCAACGTGCGGTACTGTCCTAGGCGGGCTTGACATTATACTCACTACGTTGGTTTCGC" \
    "GATGAGTCACAGGACTTTTCAGACCATGTGTCTGCCTCTAGGACCAATGGCTGGGTGTTGGTATACAACAGAGTCATTCATTTACGTCGTATATTCTAATACCACTCTTCACAC" \
    "GTCGAAATTTTCTGAGTTTCGACTACGCTTGTGAGCACTTCCTACTTGGTTAAGCAAGTGTGGGACGGCCTTCTTGGGCCAGGACGTAGGTTCCGCTGACAGTACAACGGAGAC" \
    "CAGAAAAGCTATTCAAGAGAGACATGGTACAGTTCTGTATGCATAAGCGTGCCCCTTAGCGCAACTGGCGTATACCGTCGATTCAGGG"\
"AAGTTGGTACCCTCTATTTATGCCCGGATCTTGATCTCCAGACAGGGGGTAAAGGCATGGGCCAGTTACTACCCGTATTTAGGTTGTATTCCGCATCTGAAGGCGCCGTAGTGA" \
    "TAGGCGCTGAACTGAATGCATAATGGCCAATTTGACACCTGTGGTTGTCCTCACCAATACCTGGCCCTGTCGCTCCTAATACCCCGAAGCATAGAGCAGGTCCTAACCGGATAA" \
    "CTCAGCTAACAGAAACTCCCCCAAGAACTAAGCACACCCAATGTGAACGTAGTCCGCTAGTGCTAGCGCTTCCTTACAGCCTTTCCTTATGGTATCTATGAGCTGGCCTAGTAT" \
    "ACAGGTTCTCCGACAACCAAGCCTCTCGCTGCGTTCGAGCACTGCCCGATGGCTTTGACGCGAGAGCGCTGGGTCTCATAATAAGATGGGGCGCTGTAGCGTAGTATCCCTCTC" \
    "GAGGGGACCCCGTAATGATGACATAGGTACATGCTGATAGAGGGGTCGACGGTCATTAATAACGTCCGGCTCGGCCACCCCTAGACTAGAGGGGAGAAGTTTCAGTATCTCTCG" \
    "TTTTGAATGGTACATATAAGCCTAAAGACGAGGGTAGGGTCACTAAAACTAAGTGAGCAACGTGCGGTACTGTCCTAGGCGGGCTTGACATTATACTCACTACGTTGGTTTCGC" \
    "GATGAGTCACAGGACTTTTCAGACCATGTGTCTGCCTCTAGGACCAATGGCTGGGTGTTGGTATACAACAGAGTCATTCATTTACGTCGTATATTCTAATACCACTCTTCACAC" \
    "GTCGAAATTTTCTGAGTTTCGACTACGCTTGTGAGCACTTCCTACTTGGTTAAGCAAGTGTGGGACGGCCTTCTTGGGCCAGGACGTAGGTTCCGCTGACAGTACAACGGAGAC" \
    "CAGAAAAGCTATTCAAGAGAGACATGGTACAGTTCTGTATGCATAAGCGTGCCCCTTAGCGCAACTGGCGTATACCGTCGATTCAGGG"\
"AAGTTGGTACCCTCTATTTATGCCCGGATCTTGATCTCCAGACAGGGGGTAAAGGCATGGGCCAGTTACTACCCGTATTTAGGTTGTATTCCGCATCTGAAGGCGCCGTAGTGA" \
    "TAGGCGCTGAACTGAATGCATAATGGCCAATTTGACACCTGTGGTTGTCCTCACCAATACCTGGCCCTGTCGCTCCTAATACCCCGAAGCATAGAGCAGGTCCTAACCGGATAA" \
    "CTCAGCTAACAGAAACTCCCCCAAGAACTAAGCACACCCAATGTGAACGTAGTCCGCTAGTGCTAGCGCTTCCTTACAGCCTTTCCTTATGGTATCTATGAGCTGGCCTAGTAT" \
    "ACAGGTTCTCCGACAACCAAGCCTCTCGCTGCGTTCGAGCACTGCCCGATGGCTTTGACGCGAGAGCGCTGGGTCTCATAATAAGATGGGGCGCTGTAGCGTAGTATCCCTCTC" \
    "GAGGGGACCCCGTAATGATGACATAGGTACATGCTGATAGAGGGGTCGACGGTCATTAATAACGTCCGGCTCGGCCACCCCTAGACTAGAGGGGAGAAGTTTCAGTATCTCTCG" \
    "TTTTGAATGGTACATATAAGCCTAAAGACGAGGGTAGGGTCACTAAAACTAAGTGAGCAACGTGCGGTACTGTCCTAGGCGGGCTTGACATTATACTCACTACGTTGGTTTCGC" \
    "GATGAGTCACAGGACTTTTCAGACCATGTGTCTGCCTCTAGGACCAATGGCTGGGTGTTGGTATACAACAGAGTCATTCATTTACGTCGTATATTCTAATACCACTCTTCACAC" \
    "GTCGAAATTTTCTGAGTTTCGACTACGCTTGTGAGCACTTCCTACTTGGTTAAGCAAGTGTGGGACGGCCTTCTTGGGCCAGGACGTAGGTTCCGCTGACAGTACAACGGAGAC" \
    "CAGAAAAGCTATTCAAGAGAGACATGGTACAGTTCTGTATGCATAAGCGTGCCCCTTAGCGCAACTGGCGTATACCGTCGATTCAGGG"\
"AAGTTGGTACCCTCTATTTATGCCCGGATCTTGATCTCCAGACAGGGGGTAAAGGCATGGGCCAGTTACTACCCGTATTTAGGTTGTATTCCGCATCTGAAGGCGCCGTAGTGA" \
    "TAGGCGCTGAACTGAATGCATAATGGCCAATTTGACACCTGTGGTTGTCCTCACCAATACCTGGCCCTGTCGCTCCTAATACCCCGAAGCATAGAGCAGGTCCTAACCGGATAA" \
    "CTCAGCTAACAGAAACTCCCCCAAGAACTAAGCACACCCAATGTGAACGTAGTCCGCTAGTGCTAGCGCTTCCTTACAGCCTTTCCTTATGGTATCTATGAGCTGGCCTAGTAT" \
    "ACAGGTTCTCCGACAACCAAGCCTCTCGCTGCGTTCGAGCACTGCCCGATGGCTTTGACGCGAGAGCGCTGGGTCTCATAATAAGATGGGGCGCTGTAGCGTAGTATCCCTCTC" \
    "GAGGGGACCCCGTAATGATGACATAGGTACATGCTGATAGAGGGGTCGACGGTCATTAATAACGTCCGGCTCGGCCACCCCTAGACTAGAGGGGAGAAGTTTCAGTATCTCTCG" \
    "TTTTGAATGGTACATATAAGCCTAAAGACGAGGGTAGGGTCACTAAAACTAAGTGAGCAACGTGCGGTACTGTCCTAGGCGGGCTTGACATTATACTCACTACGTTGGTTTCGC" \
    "GATGAGTCACAGGACTTTTCAGACCATGTGTCTGCCTCTAGGACCAATGGCTGGGTGTTGGTATACAACAGAGTCATTCATTTACGTCGTATATTCTAATACCACTCTTCACAC" \
    "GTCGAAATTTTCTGAGTTTCGACTACGCTTGTGAGCACTTCCTACTTGGTTAAGCAAGTGTGGGACGGCCTTCTTGGGCCAGGACGTAGGTTCCGCTGACAGTACAACGGAGAC" \
    "CAGAAAAGCTATTCAAGAGAGACATGGTACAGTTCTGTATGCATAAGCGTGCCCCTTAGCGCAACTGGCGTATACCGTCGATTCAGGG"\
"AAGTTGGTACCCTCTATTTATGCCCGGATCTTGATCTCCAGACAGGGGGTAAAGGCATGGGCCAGTTACTACCCGTATTTAGGTTGTATTCCGCATCTGAAGGCGCCGTAGTGA" \
    "TAGGCGCTGAACTGAATGCATAATGGCCAATTTGACACCTGTGGTTGTCCTCACCAATACCTGGCCCTGTCGCTCCTAATACCCCGAAGCATAGAGCAGGTCCTAACCGGATAA" \
    "CTCAGCTAACAGAAACTCCCCCAAGAACTAAGCACACCCAATGTGAACGTAGTCCGCTAGTGCTAGCGCTTCCTTACAGCCTTTCCTTATGGTATCTATGAGCTGGCCTAGTAT" \
    "ACAGGTTCTCCGACAACCAAGCCTCTCGCTGCGTTCGAGCACTGCCCGATGGCTTTGACGCGAGAGCGCTGGGTCTCATAATAAGATGGGGCGCTGTAGCGTAGTATCCCTCTC" \
    "GAGGGGACCCCGTAATGATGACATAGGTACATGCTGATAGAGGGGTCGACGGTCATTAATAACGTCCGGCTCGGCCACCCCTAGACTAGAGGGGAGAAGTTTCAGTATCTCTCG" \
    "TTTTGAATGGTACATATAAGCCTAAAGACGAGGGTAGGGTCACTAAAACTAAGTGAGCAACGTGCGGTACTGTCCTAGGCGGGCTTGACATTATACTCACTACGTTGGTTTCGC" \
    "GATGAGTCACAGGACTTTTCAGACCATGTGTCTGCCTCTAGGACCAATGGCTGGGTGTTGGTATACAACAGAGTCATTCATTTACGTCGTATATTCTAATACCACTCTTCACAC" \
    "GTCGAAATTTTCTGAGTTTCGACTACGCTTGTGAGCACTTCCTACTTGGTTAAGCAAGTGTGGGACGGCCTTCTTGGGCCAGGACGTAGGTTCCGCTGACAGTACAACGGAGAC" \
    "CAGAAAAGCTATTCAAGAGAGACATGGTACAGTTCTGTATGCATAAGCGTGCCCCTTAGCGCAACTGGCGTATACCGTCGATTCAGGG"\
"AAGTTGGTACCCTCTATTTATGCCCGGATCTTGATCTCCAGACAGGGGGTAAAGGCATGGGCCAGTTACTACCCGTATTTAGGTTGTATTCCGCATCTGAAGGCGCCGTAGTGA" \
    "TAGGCGCTGAACTGAATGCATAATGGCCAATTTGACACCTGTGGTTGTCCTCACCAATACCTGGCCCTGTCGCTCCTAATACCCCGAAGCATAGAGCAGGTCCTAACCGGATAA" \
    "CTCAGCTAACAGAAACTCCCCCAAGAACTAAGCACACCCAATGTGAACGTAGTCCGCTAGTGCTAGCGCTTCCTTACAGCCTTTCCTTATGGTATCTATGAGCTGGCCTAGTAT" \
    "ACAGGTTCTCCGACAACCAAGCCTCTCGCTGCGTTCGAGCACTGCCCGATGGCTTTGACGCGAGAGCGCTGGGTCTCATAATAAGATGGGGCGCTGTAGCGTAGTATCCCTCTC" \
    "GAGGGGACCCCGTAATGATGACATAGGTACATGCTGATAGAGGGGTCGACGGTCATTAATAACGTCCGGCTCGGCCACCCCTAGACTAGAGGGGAGAAGTTTCAGTATCTCTCG" \
    "TTTTGAATGGTACATATAAGCCTAAAGACGAGGGTAGGGTCACTAAAACTAAGTGAGCAACGTGCGGTACTGTCCTAGGCGGGCTTGACATTATACTCACTACGTTGGTTTCGC" \
    "GATGAGTCACAGGACTTTTCAGACCATGTGTCTGCCTCTAGGACCAATGGCTGGGTGTTGGTATACAACAGAGTCATTCATTTACGTCGTATATTCTAATACCACTCTTCACAC" \
    "GTCGAAATTTTCTGAGTTTCGACTACGCTTGTGAGCACTTCCTACTTGGTTAAGCAAGTGTGGGACGGCCTTCTTGGGCCAGGACGTAGGTTCCGCTGACAGTACAACGGAGAC" \
    "CAGAAAAGCTATTCAAGAGAGACATGGTACAGTTCTGTATGCATAAGCGTGCCCCTTAGCGCAACTGGCGTATACCGTCGATTCAGGG"

b10000 = 'GTTCGTTCATGACTGTCTAAACCTATTCGACGTGCGCCCTTTAGAGGATCATTCTAGATT'\
   'GTATGAGACCGATAAGATGAACATTTTATCAATTCCGCGCGGGGCTACAATATGATCTTG'\
   'ATAATTGTGGTATAAGAGACGATAAAGGCGATTTTCTATCAATCCATCTGACAAACCGTC'\
   'TCTAGCATCAATGCAACGCGTTTGGTTGGCCTAGTGGCGTTAGTGAATGGGGACCAGTTC'\
   'AGTATCGCCCATCGGACTTGAACAATAAGCGTGAACGGACCCAAACTTTTATGCCCGGCC'\
   'GGTTTCGACCCCGTTGCGACGAGTTATCATTTCAGCACGAGGACATGGTCCCGGTTTGAG'\
   'ACTCGTAAAACCCTACCTAGCACGGTATTCCGGACACTAATATAAAATGAATACCTGCGA'\
   'TAATAGATCAAGCGCTACAGCCCGGGCCCAGCTACCCGGATATAAATCTAAATGTTGCAT'\
   'AAACCATTATTGTACCTCAACTTGAGTTCGATAGGCCGCGCACTGTGGCTTTGCCATGCC'\
   'TACGCTTCACCATAGACTACACGTGAAAATTCGCATTAGCCTACACGACACGCCCGAGTC'\
   'TAAATGTTCCTCGAAGAACAATGTTGCCAAAGTTCTATTGATTACACACAAGCGCACTAA'\
   'AAGACAAAATTTATGGCCAGGGGCGGTAGTAGAATAGCAAGGTGAGTTGTTCGCAGGCTA'\
   'CATGCGATGCGATAGTATACTCGCGACCGGAGGGGGTCCCACACCCTTATGCTGATATTG'\
   'CTTATGCATATGGCTACGATACAGCCGAAACCAAACGGCTAAATATTAGTACCTAGTTTC'\
   'GAAAACATGGCTTGCGCATCACCTTCCATAAGGACGACGTCGAGCCAAGCGCATAGAAGG'\
   'CTTTATAATTATAAGGACAATGGGGACATCTCGTCCTGGTGTATTCGTCCAAGTGCTTGG'\
   'TGAAATCATCACGACCCATAGATGCTTCATCAGCATCATC'\
'GTTCGTTCATGACTGTCTAAACCTATTCGACGTGCGCCCTTTAGAGGATCATTCTAGATT'\
   'GTATGAGACCGATAAGATGAACATTTTATCAATTCCGCGCGGGGCTACAATATGATCTTG'\
   'ATAATTGTGGTATAAGAGACGATAAAGGCGATTTTCTATCAATCCATCTGACAAACCGTC'\
   'TCTAGCATCAATGCAACGCGTTTGGTTGGCCTAGTGGCGTTAGTGAATGGGGACCAGTTC'\
   'AGTATCGCCCATCGGACTTGAACAATAAGCGTGAACGGACCCAAACTTTTATGCCCGGCC'\
   'GGTTTCGACCCCGTTGCGACGAGTTATCATTTCAGCACGAGGACATGGTCCCGGTTTGAG'\
   'ACTCGTAAAACCCTACCTAGCACGGTATTCCGGACACTAATATAAAATGAATACCTGCGA'\
   'TAATAGATCAAGCGCTACAGCCCGGGCCCAGCTACCCGGATATAAATCTAAATGTTGCAT'\
   'AAACCATTATTGTACCTCAACTTGAGTTCGATAGGCCGCGCACTGTGGCTTTGCCATGCC'\
   'TACGCTTCACCATAGACTACACGTGAAAATTCGCATTAGCCTACACGACACGCCCGAGTC'\
   'TAAATGTTCCTCGAAGAACAATGTTGCCAAAGTTCTATTGATTACACACAAGCGCACTAA'\
   'AAGACAAAATTTATGGCCAGGGGCGGTAGTAGAATAGCAAGGTGAGTTGTTCGCAGGCTA'\
   'CATGCGATGCGATAGTATACTCGCGACCGGAGGGGGTCCCACACCCTTATGCTGATATTG'\
   'CTTATGCATATGGCTACGATACAGCCGAAACCAAACGGCTAAATATTAGTACCTAGTTTC'\
   'GAAAACATGGCTTGCGCATCACCTTCCATAAGGACGACGTCGAGCCAAGCGCATAGAAGG'\
   'CTTTATAATTATAAGGACAATGGGGACATCTCGTCCTGGTGTATTCGTCCAAGTGCTTGG'\
   'TGAAATCATCACGACCCATAGATGCTTCATCAGCATCATC'\
'GTTCGTTCATGACTGTCTAAACCTATTCGACGTGCGCCCTTTAGAGGATCATTCTAGATT'\
   'GTATGAGACCGATAAGATGAACATTTTATCAATTCCGCGCGGGGCTACAATATGATCTTG'\
   'ATAATTGTGGTATAAGAGACGATAAAGGCGATTTTCTATCAATCCATCTGACAAACCGTC'\
   'TCTAGCATCAATGCAACGCGTTTGGTTGGCCTAGTGGCGTTAGTGAATGGGGACCAGTTC'\
   'AGTATCGCCCATCGGACTTGAACAATAAGCGTGAACGGACCCAAACTTTTATGCCCGGCC'\
   'GGTTTCGACCCCGTTGCGACGAGTTATCATTTCAGCACGAGGACATGGTCCCGGTTTGAG'\
   'ACTCGTAAAACCCTACCTAGCACGGTATTCCGGACACTAATATAAAATGAATACCTGCGA'\
   'TAATAGATCAAGCGCTACAGCCCGGGCCCAGCTACCCGGATATAAATCTAAATGTTGCAT'\
   'AAACCATTATTGTACCTCAACTTGAGTTCGATAGGCCGCGCACTGTGGCTTTGCCATGCC'\
   'TACGCTTCACCATAGACTACACGTGAAAATTCGCATTAGCCTACACGACACGCCCGAGTC'\
   'TAAATGTTCCTCGAAGAACAATGTTGCCAAAGTTCTATTGATTACACACAAGCGCACTAA'\
   'AAGACAAAATTTATGGCCAGGGGCGGTAGTAGAATAGCAAGGTGAGTTGTTCGCAGGCTA'\
   'CATGCGATGCGATAGTATACTCGCGACCGGAGGGGGTCCCACACCCTTATGCTGATATTG'\
   'CTTATGCATATGGCTACGATACAGCCGAAACCAAACGGCTAAATATTAGTACCTAGTTTC'\
   'GAAAACATGGCTTGCGCATCACCTTCCATAAGGACGACGTCGAGCCAAGCGCATAGAAGG'\
   'CTTTATAATTATAAGGACAATGGGGACATCTCGTCCTGGTGTATTCGTCCAAGTGCTTGG'\
   'TGAAATCATCACGACCCATAGATGCTTCATCAGCATCATC'\
'GTTCGTTCATGACTGTCTAAACCTATTCGACGTGCGCCCTTTAGAGGATCATTCTAGATT'\
   'GTATGAGACCGATAAGATGAACATTTTATCAATTCCGCGCGGGGCTACAATATGATCTTG'\
   'ATAATTGTGGTATAAGAGACGATAAAGGCGATTTTCTATCAATCCATCTGACAAACCGTC'\
   'TCTAGCATCAATGCAACGCGTTTGGTTGGCCTAGTGGCGTTAGTGAATGGGGACCAGTTC'\
   'AGTATCGCCCATCGGACTTGAACAATAAGCGTGAACGGACCCAAACTTTTATGCCCGGCC'\
   'GGTTTCGACCCCGTTGCGACGAGTTATCATTTCAGCACGAGGACATGGTCCCGGTTTGAG'\
   'ACTCGTAAAACCCTACCTAGCACGGTATTCCGGACACTAATATAAAATGAATACCTGCGA'\
   'TAATAGATCAAGCGCTACAGCCCGGGCCCAGCTACCCGGATATAAATCTAAATGTTGCAT'\
   'AAACCATTATTGTACCTCAACTTGAGTTCGATAGGCCGCGCACTGTGGCTTTGCCATGCC'\
   'TACGCTTCACCATAGACTACACGTGAAAATTCGCATTAGCCTACACGACACGCCCGAGTC'\
   'TAAATGTTCCTCGAAGAACAATGTTGCCAAAGTTCTATTGATTACACACAAGCGCACTAA'\
   'AAGACAAAATTTATGGCCAGGGGCGGTAGTAGAATAGCAAGGTGAGTTGTTCGCAGGCTA'\
   'CATGCGATGCGATAGTATACTCGCGACCGGAGGGGGTCCCACACCCTTATGCTGATATTG'\
   'CTTATGCATATGGCTACGATACAGCCGAAACCAAACGGCTAAATATTAGTACCTAGTTTC'\
   'GAAAACATGGCTTGCGCATCACCTTCCATAAGGACGACGTCGAGCCAAGCGCATAGAAGG'\
   'CTTTATAATTATAAGGACAATGGGGACATCTCGTCCTGGTGTATTCGTCCAAGTGCTTGG'\
   'TGAAATCATCACGACCCATAGATGCTTCATCAGCATCATC'\
'GTTCGTTCATGACTGTCTAAACCTATTCGACGTGCGCCCTTTAGAGGATCATTCTAGATT'\
   'GTATGAGACCGATAAGATGAACATTTTATCAATTCCGCGCGGGGCTACAATATGATCTTG'\
   'ATAATTGTGGTATAAGAGACGATAAAGGCGATTTTCTATCAATCCATCTGACAAACCGTC'\
   'TCTAGCATCAATGCAACGCGTTTGGTTGGCCTAGTGGCGTTAGTGAATGGGGACCAGTTC'\
   'AGTATCGCCCATCGGACTTGAACAATAAGCGTGAACGGACCCAAACTTTTATGCCCGGCC'\
   'GGTTTCGACCCCGTTGCGACGAGTTATCATTTCAGCACGAGGACATGGTCCCGGTTTGAG'\
   'ACTCGTAAAACCCTACCTAGCACGGTATTCCGGACACTAATATAAAATGAATACCTGCGA'\
   'TAATAGATCAAGCGCTACAGCCCGGGCCCAGCTACCCGGATATAAATCTAAATGTTGCAT'\
   'AAACCATTATTGTACCTCAACTTGAGTTCGATAGGCCGCGCACTGTGGCTTTGCCATGCC'\
   'TACGCTTCACCATAGACTACACGTGAAAATTCGCATTAGCCTACACGACACGCCCGAGTC'\
   'TAAATGTTCCTCGAAGAACAATGTTGCCAAAGTTCTATTGATTACACACAAGCGCACTAA'\
   'AAGACAAAATTTATGGCCAGGGGCGGTAGTAGAATAGCAAGGTGAGTTGTTCGCAGGCTA'\
   'CATGCGATGCGATAGTATACTCGCGACCGGAGGGGGTCCCACACCCTTATGCTGATATTG'\
   'CTTATGCATATGGCTACGATACAGCCGAAACCAAACGGCTAAATATTAGTACCTAGTTTC'\
   'GAAAACATGGCTTGCGCATCACCTTCCATAAGGACGACGTCGAGCCAAGCGCATAGAAGG'\
   'CTTTATAATTATAAGGACAATGGGGACATCTCGTCCTGGTGTATTCGTCCAAGTGCTTGG'\
   'TGAAATCATCACGACCCATAGATGCTTCATCAGCATCATC'\
'GTTCGTTCATGACTGTCTAAACCTATTCGACGTGCGCCCTTTAGAGGATCATTCTAGATT'\
   'GTATGAGACCGATAAGATGAACATTTTATCAATTCCGCGCGGGGCTACAATATGATCTTG'\
   'ATAATTGTGGTATAAGAGACGATAAAGGCGATTTTCTATCAATCCATCTGACAAACCGTC'\
   'TCTAGCATCAATGCAACGCGTTTGGTTGGCCTAGTGGCGTTAGTGAATGGGGACCAGTTC'\
   'AGTATCGCCCATCGGACTTGAACAATAAGCGTGAACGGACCCAAACTTTTATGCCCGGCC'\
   'GGTTTCGACCCCGTTGCGACGAGTTATCATTTCAGCACGAGGACATGGTCCCGGTTTGAG'\
   'ACTCGTAAAACCCTACCTAGCACGGTATTCCGGACACTAATATAAAATGAATACCTGCGA'\
   'TAATAGATCAAGCGCTACAGCCCGGGCCCAGCTACCCGGATATAAATCTAAATGTTGCAT'\
   'AAACCATTATTGTACCTCAACTTGAGTTCGATAGGCCGCGCACTGTGGCTTTGCCATGCC'\
   'TACGCTTCACCATAGACTACACGTGAAAATTCGCATTAGCCTACACGACACGCCCGAGTC'\
   'TAAATGTTCCTCGAAGAACAATGTTGCCAAAGTTCTATTGATTACACACAAGCGCACTAA'\
   'AAGACAAAATTTATGGCCAGGGGCGGTAGTAGAATAGCAAGGTGAGTTGTTCGCAGGCTA'\
   'CATGCGATGCGATAGTATACTCGCGACCGGAGGGGGTCCCACACCCTTATGCTGATATTG'\
   'CTTATGCATATGGCTACGATACAGCCGAAACCAAACGGCTAAATATTAGTACCTAGTTTC'\
   'GAAAACATGGCTTGCGCATCACCTTCCATAAGGACGACGTCGAGCCAAGCGCATAGAAGG'\
   'CTTTATAATTATAAGGACAATGGGGACATCTCGTCCTGGTGTATTCGTCCAAGTGCTTGG'\
   'TGAAATCATCACGACCCATAGATGCTTCATCAGCATCATC'\
'GTTCGTTCATGACTGTCTAAACCTATTCGACGTGCGCCCTTTAGAGGATCATTCTAGATT'\
   'GTATGAGACCGATAAGATGAACATTTTATCAATTCCGCGCGGGGCTACAATATGATCTTG'\
   'ATAATTGTGGTATAAGAGACGATAAAGGCGATTTTCTATCAATCCATCTGACAAACCGTC'\
   'TCTAGCATCAATGCAACGCGTTTGGTTGGCCTAGTGGCGTTAGTGAATGGGGACCAGTTC'\
   'AGTATCGCCCATCGGACTTGAACAATAAGCGTGAACGGACCCAAACTTTTATGCCCGGCC'\
   'GGTTTCGACCCCGTTGCGACGAGTTATCATTTCAGCACGAGGACATGGTCCCGGTTTGAG'\
   'ACTCGTAAAACCCTACCTAGCACGGTATTCCGGACACTAATATAAAATGAATACCTGCGA'\
   'TAATAGATCAAGCGCTACAGCCCGGGCCCAGCTACCCGGATATAAATCTAAATGTTGCAT'\
   'AAACCATTATTGTACCTCAACTTGAGTTCGATAGGCCGCGCACTGTGGCTTTGCCATGCC'\
   'TACGCTTCACCATAGACTACACGTGAAAATTCGCATTAGCCTACACGACACGCCCGAGTC'\
   'TAAATGTTCCTCGAAGAACAATGTTGCCAAAGTTCTATTGATTACACACAAGCGCACTAA'\
   'AAGACAAAATTTATGGCCAGGGGCGGTAGTAGAATAGCAAGGTGAGTTGTTCGCAGGCTA'\
   'CATGCGATGCGATAGTATACTCGCGACCGGAGGGGGTCCCACACCCTTATGCTGATATTG'\
   'CTTATGCATATGGCTACGATACAGCCGAAACCAAACGGCTAAATATTAGTACCTAGTTTC'\
   'GAAAACATGGCTTGCGCATCACCTTCCATAAGGACGACGTCGAGCCAAGCGCATAGAAGG'\
   'CTTTATAATTATAAGGACAATGGGGACATCTCGTCCTGGTGTATTCGTCCAAGTGCTTGG'\
   'TGAAATCATCACGACCCATAGATGCTTCATCAGCATCATC'\
'GTTCGTTCATGACTGTCTAAACCTATTCGACGTGCGCCCTTTAGAGGATCATTCTAGATT'\
   'GTATGAGACCGATAAGATGAACATTTTATCAATTCCGCGCGGGGCTACAATATGATCTTG'\
   'ATAATTGTGGTATAAGAGACGATAAAGGCGATTTTCTATCAATCCATCTGACAAACCGTC'\
   'TCTAGCATCAATGCAACGCGTTTGGTTGGCCTAGTGGCGTTAGTGAATGGGGACCAGTTC'\
   'AGTATCGCCCATCGGACTTGAACAATAAGCGTGAACGGACCCAAACTTTTATGCCCGGCC'\
   'GGTTTCGACCCCGTTGCGACGAGTTATCATTTCAGCACGAGGACATGGTCCCGGTTTGAG'\
   'ACTCGTAAAACCCTACCTAGCACGGTATTCCGGACACTAATATAAAATGAATACCTGCGA'\
   'TAATAGATCAAGCGCTACAGCCCGGGCCCAGCTACCCGGATATAAATCTAAATGTTGCAT'\
   'AAACCATTATTGTACCTCAACTTGAGTTCGATAGGCCGCGCACTGTGGCTTTGCCATGCC'\
   'TACGCTTCACCATAGACTACACGTGAAAATTCGCATTAGCCTACACGACACGCCCGAGTC'\
   'TAAATGTTCCTCGAAGAACAATGTTGCCAAAGTTCTATTGATTACACACAAGCGCACTAA'\
   'AAGACAAAATTTATGGCCAGGGGCGGTAGTAGAATAGCAAGGTGAGTTGTTCGCAGGCTA'\
   'CATGCGATGCGATAGTATACTCGCGACCGGAGGGGGTCCCACACCCTTATGCTGATATTG'\
   'CTTATGCATATGGCTACGATACAGCCGAAACCAAACGGCTAAATATTAGTACCTAGTTTC'\
   'GAAAACATGGCTTGCGCATCACCTTCCATAAGGACGACGTCGAGCCAAGCGCATAGAAGG'\
   'CTTTATAATTATAAGGACAATGGGGACATCTCGTCCTGGTGTATTCGTCCAAGTGCTTGG'\
   'TGAAATCATCACGACCCATAGATGCTTCATCAGCATCATC'\
'GTTCGTTCATGACTGTCTAAACCTATTCGACGTGCGCCCTTTAGAGGATCATTCTAGATT'\
   'GTATGAGACCGATAAGATGAACATTTTATCAATTCCGCGCGGGGCTACAATATGATCTTG'\
   'ATAATTGTGGTATAAGAGACGATAAAGGCGATTTTCTATCAATCCATCTGACAAACCGTC'\
   'TCTAGCATCAATGCAACGCGTTTGGTTGGCCTAGTGGCGTTAGTGAATGGGGACCAGTTC'\
   'AGTATCGCCCATCGGACTTGAACAATAAGCGTGAACGGACCCAAACTTTTATGCCCGGCC'\
   'GGTTTCGACCCCGTTGCGACGAGTTATCATTTCAGCACGAGGACATGGTCCCGGTTTGAG'\
   'ACTCGTAAAACCCTACCTAGCACGGTATTCCGGACACTAATATAAAATGAATACCTGCGA'\
   'TAATAGATCAAGCGCTACAGCCCGGGCCCAGCTACCCGGATATAAATCTAAATGTTGCAT'\
   'AAACCATTATTGTACCTCAACTTGAGTTCGATAGGCCGCGCACTGTGGCTTTGCCATGCC'\
   'TACGCTTCACCATAGACTACACGTGAAAATTCGCATTAGCCTACACGACACGCCCGAGTC'\
   'TAAATGTTCCTCGAAGAACAATGTTGCCAAAGTTCTATTGATTACACACAAGCGCACTAA'\
   'AAGACAAAATTTATGGCCAGGGGCGGTAGTAGAATAGCAAGGTGAGTTGTTCGCAGGCTA'\
   'CATGCGATGCGATAGTATACTCGCGACCGGAGGGGGTCCCACACCCTTATGCTGATATTG'\
   'CTTATGCATATGGCTACGATACAGCCGAAACCAAACGGCTAAATATTAGTACCTAGTTTC'\
   'GAAAACATGGCTTGCGCATCACCTTCCATAAGGACGACGTCGAGCCAAGCGCATAGAAGG'\
   'CTTTATAATTATAAGGACAATGGGGACATCTCGTCCTGGTGTATTCGTCCAAGTGCTTGG'\
   'TGAAATCATCACGACCCATAGATGCTTCATCAGCATCATC'\
'GTTCGTTCATGACTGTCTAAACCTATTCGACGTGCGCCCTTTAGAGGATCATTCTAGATT'\
   'GTATGAGACCGATAAGATGAACATTTTATCAATTCCGCGCGGGGCTACAATATGATCTTG'\
   'ATAATTGTGGTATAAGAGACGATAAAGGCGATTTTCTATCAATCCATCTGACAAACCGTC'\
   'TCTAGCATCAATGCAACGCGTTTGGTTGGCCTAGTGGCGTTAGTGAATGGGGACCAGTTC'\
   'AGTATCGCCCATCGGACTTGAACAATAAGCGTGAACGGACCCAAACTTTTATGCCCGGCC'\
   'GGTTTCGACCCCGTTGCGACGAGTTATCATTTCAGCACGAGGACATGGTCCCGGTTTGAG'\
   'ACTCGTAAAACCCTACCTAGCACGGTATTCCGGACACTAATATAAAATGAATACCTGCGA'\
   'TAATAGATCAAGCGCTACAGCCCGGGCCCAGCTACCCGGATATAAATCTAAATGTTGCAT'\
   'AAACCATTATTGTACCTCAACTTGAGTTCGATAGGCCGCGCACTGTGGCTTTGCCATGCC'\
   'TACGCTTCACCATAGACTACACGTGAAAATTCGCATTAGCCTACACGACACGCCCGAGTC'\
   'TAAATGTTCCTCGAAGAACAATGTTGCCAAAGTTCTATTGATTACACACAAGCGCACTAA'\
   'AAGACAAAATTTATGGCCAGGGGCGGTAGTAGAATAGCAAGGTGAGTTGTTCGCAGGCTA'\
   'CATGCGATGCGATAGTATACTCGCGACCGGAGGGGGTCCCACACCCTTATGCTGATATTG'\
   'CTTATGCATATGGCTACGATACAGCCGAAACCAAACGGCTAAATATTAGTACCTAGTTTC'\
   'GAAAACATGGCTTGCGCATCACCTTCCATAAGGACGACGTCGAGCCAAGCGCATAGAAGG'\
   'CTTTATAATTATAAGGACAATGGGGACATCTCGTCCTGGTGTATTCGTCCAAGTGCTTGG'\
   'TGAAATCATCACGACCCATAGATGCTTCATCAGCATCATC'

print("Size = 10000 Dynamic:")
before = time.time()
print(lcs_dyn(a10000,b10000),"is longest substring")
after = time.time()
print(after-before, " seconds elapsed")













'''
**OUTPUT**
C:\Python34\python.exe C:/Users/Carl-Admin/Documents/PyCharm/DNA/DNA.py
Size = 10 brute:
GCCGT  is the match
5
0.009006023406982422  seconds elapsed

Size = 10 Dynamic:
GCCGT  is the match
5 is longest substring
0.0  seconds elapsed

Size = 15 brute:
ATTAGATATTGC  is the match
11
0.40827083587646484  seconds elapsed

Size = 15 Dynamic:
ATTAGATATTG  is the match
11 is longest substring
0.001001119613647461  seconds elapsed

Size = 20 brute:
GAAGGAGTTA  is the match
10
17.784836053848267  seconds elapsed

Size = 20 Dynamic:
GAAGGAGTTA  is the match
10 is longest substring
0.0  seconds elapsed

Size = 100 Dynamic:
GGGTTCGCCCCGGATCTGTTACAGCAAAGTCTGTAGCAGCTAATTAGGGCGTGTGTCAGGCTGA  is the match
64 is longest substring
0.010006904602050781  seconds elapsed

Size = 1000 Dynamic:
GTTGTTCATGACTGTCTCCAGACGGGTAAGGATCCAGTTATACCGATAGGTTTATTCCGCCGGGGCCTATGATCTGATAATGATAAGAGACATGGGTTTTCACAATCCTGCCCGTCTCTAATCAAGCAAGCGGTCCTAGGATAATCAGTCAGATCCCCAAGAACTAAGCACACCCAAACTATCCCGGCCGTTTCGCCCCGTTCGACGAGTTACATTTCGACAACAGTCCCGGTTGAGACTGCCCATGCTTTCCGGACCTTATAAAAGATCCTGCGTATATCCCTCAGGGGCCCGTAATATAAATCATGTGATAAACCATTATACTCCGGTCGACCCGACTGGGGAGAGTTCAATCTCCGTGAATTCATTAGCCTAAGACAGGGTAGTCCTAAAACAATGGCAAGTCTATGTCCACGGCTGACATTTATCCAGGGGCGTGAGTACAGGATTTTCGCAGGTCTGCTCTAGAATGGCGGGGGGTCAACAGGTATTCTTATGATATCTAATACACCACACGGAAATTTTCTAGTTTCGAACGCTTGGACACTTCCATAAGGACGCTCGGCCAACGTAGGGCTAATAAAGGACAAGCATTCGCTGGTACGTTCTGTATCATACGCCCTAGATGCTTCTCGATCA  is the match
639 is longest substring
0.9476280212402344  seconds elapsed

Process finished with exit code 0

'''
