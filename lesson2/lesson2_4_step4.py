with open("dataset_24465_4.txt") as f, open("inv.txt", "w") as w:
    il = f.read().splitlines()
    w.write("\n".join(il[i] for i in range(len(il)-1, -1, -1)))

