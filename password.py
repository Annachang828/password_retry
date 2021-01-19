password = 'a123456'
while True:
	pwd = input('請輸入密碼:')
	if pwd == password:
		print('登入成功')
		break
	else:
		print('密碼錯誤!還有2次機會')
	pwd = input('請輸入密碼:')	
	if pwd == password:
		print('登入成功')
		break
	else:
		print('密碼錯誤!還有1次機會')
	pwd = input('請輸入密碼:')	
	if pwd == password:
		print('登入成功')
		break
	else:
		print('密碼錯誤!還有0次機會,請洽服務人員')
		break

