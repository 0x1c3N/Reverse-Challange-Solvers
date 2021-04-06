arr1 = [159,174,156,182,189,185,239,235,230,158,185,236,179,185,227,185,187,168,137,227,189,239,187,150,185,237,227,137,185,228]
txt = ""
for i in arr1:
	var2 = i ^ 0xcb
	var1 = var2 - 0x11
	if not (32 < var1 < 127):
		var1 = (i^0xcb) + 0x4e
		txt += chr(var1)
	else:
		if var2 < 0x20:
			var1 = var2 - 0x81
			txt += chr(var1)
		else:
			var1 = var2 - 0x11
			txt += chr(var1)
print(txt)
