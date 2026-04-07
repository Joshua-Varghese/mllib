def find_s(c):
    #assuming that the last column would be the target concept
    flag = True
    hypo_target = [0]*(len(c[0])-1)
      
    for hypo in c:
        if hypo[-1] in ["yes","Yes","YES"]:
            bucket = hypo[:-1].copy()
            if flag == True:
                hypo_target = bucket
                flag = False
            else:
                for elem in range(len(bucket)):
                    if hypo_target[elem] == bucket[elem]:
                        pass
                    else:
                        hypo_target[elem] = "?"
    print(hypo_target)

        



