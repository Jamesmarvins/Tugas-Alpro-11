def cek_sama(t):
    return len(set(t)) == 1

tA = (90, 90, 90, 90)

if cek_sama(tA):
    print("True")
else:
    print("False")