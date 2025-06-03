file = open("text2.txt", "r", encoding="utf-8")

word_map = {}
txt_list = file.read().split(" ")

for item in txt_list:
    item.strip(" .,;?![]\"\':-").lower()
    if item == "":
        continue
    elif item in word_map:
        word_map[item] += 1
    else:
        word_map[item] = 1

word_r_map = {v:k for (k, v) in word_map.items()}
word_map = {v:k for (k, v) in sorted(word_r_map.items(), reverse=True)}

for key in word_map:
    if word_map[key] >= 100:
        print("[{}] : {}".format(key, word_map[key]))




file.close()