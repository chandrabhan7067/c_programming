#-----------------------------------------ALPHBATE PROBLEM-------------------------------------

# 15. Combinations of words formed by replacing given numbers with corresponding alphabets.

# ALPHA = ['','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# pair = []
# L1 =  [1,2,1,4,3]
# n= len(L1)
# for i in range(n-1):
#     make_pair = int(str(L1[i]) + str(L1[i+1]))
    
#     combo = []
#     j = 0
#     while j<n:
#         if j!=i and j!=i+1:
#             combo.append(L1[j])
#             j+=1
#         else:
#             combo.append(make_pair)
#             j+=2
#         if combo not in pair:
#             # print(pair)
#             pair.append(combo)
# print(pair)

# double  = []
# i = 0
# while i<n-1:
#     num = int(str(L1[i]) + str(L1[i+1]))
#     double.append(num)
#     i+=2
#     print(double)

# def isvailed(element):
#     count = 0
#     for item in element:
#         if item<26:
#             count+=1
#     if count==len(element):
#         return 1
#     return 0

# def result(element):
#     Alphalist= ''
#     for index in element:
#         Alphalist += str(ALPHA[index])
#     print(Alphalist)

# result(L1)

# for item in pair:
#     if isvailed(item):
#         result(item)

# if isvailed(double):
#     if len(double)>1:
#         result(double)
        
        
# ----------------------------------ROUGHT      
# l1 = [1,23,4]        
# for item in l1:
#     if item == 23:
#         print("yes")

# if 23 not in l1:
#     print('yes')
    # ------------------------------------------------    
        
        
        
ALPHA = ['','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
l1 = [1,2,1,4,3]
pair = []
n = len(l1)

for i in range(n-1):
    make_pair = int(str(l1[i]) + str(l1[i+1]))

    combo = []
    j = 0
    while j<n:
        if j!=i and j!=i+1:
            combo.append(l1[j])        
            j+=1
            
        else:
            combo.append(make_pair)
            j+=2
        # print(double)

        if combo not in pair:
            # print(pair)
            pair.append(combo)
print(pair)

double = []
i=0
while i<n-1:
    make_pair2 = int(str(l1[i]) + str(l1[i+1]))
    double.append(make_pair2)
    i+=2
print(double)


def Is_valid(element):
    count = 0
    for item in element:
        if item<26:
            count+=1
        
    if count == len(element):
        return 1
    return 0
    
def Final_result(element):
    Alphalist = ''
    for item in element:
        Alphalist += ALPHA[item]
        # Alphalist.append(ALPHA[item])
    print(Alphalist)

Final_result(l1)


for item in pair:
    if Is_valid(item):
        Final_result(item)
        
        
if Is_valid(double):
    if len(double)>1:
        Final_result(double)
        