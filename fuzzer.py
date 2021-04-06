import os

flag = ["x","x","x","x","x","x","x","x","x"]
letters = "abcdefghijklmnopqrstuvwxyz_0123456789ABCDEFGHIJKLMNOPQRSTUVWXZ.?*^%$#@!+-~,/<>=[]"

for i in range(9):
  for j in range(len(letters)):
    flag[i] = letters[j]
    strflag = "".join(flag)
    strflag = "'CTFlearn{" + strflag
    strflag = strflag + "}'"

    cmd = "./Raspberry " + strflag
    output = os.popen(cmd).read()
    if f"Bad Character: {letters[j]}" not in output:
      print(flag[i])
      flag[i] = letters[j]
      break
print("".join(flag))  
