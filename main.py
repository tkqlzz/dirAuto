import os
arr = os.listdir()
res = ""
for str in arr:
    if str.find(".zip") > -1:
        res += str[:-4] + "\n"

f = open("zip_list.txt", "w")
f.write(res)
f.close()