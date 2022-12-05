import os


os.chdir("/Users/anto/Desktop/Advent of Code/Advent-of-Code/JOUR 5")
with open("input.txt", "r") as variable:
  data = variable.readlines()

pod = [["B",'L','D','T','W',"C",'F',"M"],
       ["N",'B',"L"],
       ["J",'C','H','T','L',"V"],
       ["S",'P','J',"W"],
       ["Z",'S','C','F','T','L',"R"],
       ["W",'D','G','B','H','N',"Z"],
       ["F",'M','S','P','V','G','C',"N"],
       ["W",'Q','R','J','F','V','C',"Z"],
       ["R",'P','M','L',"H"]]

for i in data:
    bin0, num_pod, bin1, pod_from, bin2, pod_to = i.rstrip().split(" ")
    num_pod,pod_from,pod_to = map(int, (num_pod,pod_from,pod_to))

    for j in range(num_pod):
        pod[pod_to-1].append(pod[pod_from-1].pop())


code = ""
for stack in pod:
    code += str(stack[-1])


print("PUZZLE 1 : ",code)