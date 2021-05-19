driving = input('請問你有開過車嗎? ')
age = input('請問你的年齡?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('通過驗證')
	else:
		print('沒有通過驗證')
elif driving == '沒有':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你還不能考')
else:
	print('只能輸入有跟沒有')