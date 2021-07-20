
f2 = open("AsinNoDoppioni.txt", "w+")
with open('Doppioni.txt', 'r+') as f:
    seen = set()
    for line in f:
        line_lower = line.lower()
        if line_lower in seen:
            print(line)
        else:
            seen.add(line_lower)
            f2.write(line)
f2.close()
cnt  = 0
with open("AsinNoDoppioni.txt", "r+") as f4:
    for l in f4:
        if "cat:" in l:
            cnt +=1
f4 = open("AsinNoDoppioni.txt", "r+")
with open("Asin_last.txt", "w+") as f6:
    cnt2 = 0
    for l in f4:
        if "cat:" in l:
            categoria = l
            cnt2+=1
            if cnt2 == cnt:
                f6.write(categoria)
                print(cnt2)
                for l in f4:
                    print("prova:"+l)
                    f6.write(l)



