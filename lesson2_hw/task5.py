i = 0
out = ""
end = 127
while i+32 < end + 1:
    if i % 10 == 0:
        out = f"{out}\n"
    out = f"{out}{i+32:<3}:{chr(i+32):<3}"
    i += 1
print(out)