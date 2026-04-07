def find_s(D):
    #assuming that the last column would be the target concept
    flag = True
    hypothesis = [0]*(len(D[0])-1)
      
    for X in D:
        if X[-1] in ["yes","Yes","YES"]:
            bucket = X[:-1].copy()
            if flag == True:
                hypothesis = bucket
                flag = False
            else:
                for elem in range(len(bucket)):
                    if hypothesis[elem] == bucket[elem]:
                        pass
                    else:
                        hypothesis[elem] = "?"
    print(hypothesis)

