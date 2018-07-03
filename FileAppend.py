
filename = r"C:\Users\pradeeba.shanmugam\PycharmProjects\tutorial\Poc_Proj\logdetails.txt"

#
# import os
# i=1
# with open(filename, 'ra') as file:
#     file.seek(-1, os.lseek(0,1,1))
#     file.write(b"\nccccc\n")

with open(filename,"r+") as f:
    l = f.readlines()
    f.seek(0)
    f.truncate()
    # #print(f.read())
    # f.seek(40)
    # f.write("#")
    # print(f.read())
    # # f.truncate()
    # #print(l)
    newlist=[]
    for i in l:
        newlist.append("#" + i)

    f.writelines(newlist)
