data = []
count = 0
sum = 0
with open ("reviews.txt", "r") as f:
	for line in f:
		data.append(line)
		count += 1
		sum += len(line)
		if count % 1000 == 0:
			print(count)

avg = sum / len(data)

print(f"讀取完畢, 共有{len(data)}筆留言")
print(f"平均留言長度為{avg}")
