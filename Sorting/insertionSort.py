'''삽입 정렬-앞의 값보다 작으면 바꿔서 정렬'''
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
	for j in range(i, 0, -1):
		if array[j] < array[j-1]:
			array[j], array[j-1] = array[j-1], array[j]
		else:
			break

print(array)