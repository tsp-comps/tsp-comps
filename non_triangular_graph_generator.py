import random
dict = {}
output = open("datasets/synthetic/random_generated.tsv", "w")
for i in range(100):
    for j in range(100):
        if (i, j) not in dict:
            weight = random.randint(1, 10)
            dict[(i, j)] = weight
            dict[(j, i)] = weight
            output.write(str(i)+"\t"+str(j)+"\t"+str(weight)+"\n")
            if i != j:
                output.write(str(j)+"\t"+str(i)+"\t"+str(weight)+"\n")