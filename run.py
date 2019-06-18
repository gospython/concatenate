with open('result.txt', 'a', encoding='utf-8') as file_result:
	with open('a.txt', 'r', encoding='utf-8') as file_a:
		for a in file_a:
			a = a.replace('\n','')
			with open('b.txt', 'r', encoding='utf-8') as file_b:
				for b in file_b:
					b = b.replace('\n','')
					file_result.write(a + ' ' + b + '\n')
