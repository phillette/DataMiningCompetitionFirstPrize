root_loc = "/Users/mac/Documents/contest/data/original_data/"
card_file = "borrow_train.txt"

stu_id=186
output_loc="/Users/mac/Documents/contest/data/distribution/borrow_"+str(stu_id)+".txt"
w=open(output_loc,'w')

lines = open(root_loc + card_file).readlines()
for line in lines:
    temps = line.strip("\n").split(",")
    id = int(temps[0])
    time = temps[1]
    date = time.split(" ")[0]
    if id==stu_id:
        w.write(line)

w.close()
