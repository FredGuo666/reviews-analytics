data = []
count = 0
with open('reviews.txt', 'r') as f:         
	for line in f:
		data.append(line)
		count += 1 
		if count % 1000 == 0:
			print(len(data))
print('档案读取完了， 总共有', len(data), '笔资料')

print(data[0])

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言的平均长度是', sum_len/len(data)) 

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '笔留言长度小于100') 
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good),'笔留言提到good')
print(good[0])

# list comprehension 清单快写法
good = [1 for d in data if 'good' in d] 
print(good)

bad = ['bad' in d for d in data]
print(bad)


# 单词计数
wc = {} # word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # 新增新的key进wc字典 

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))
print(wc['Allen'])

while True:
	word = input('请输入您要查询的单词： ')
	if word == 'q':
		break
	elif word in wc:
		print(word, '出现过的次数为: ', wc[word])
	else:
		print('这个词没有出现过')


print ('感谢您使用本次查询功能')


	














  





