# Quiz 3

site = input("사이트를 입력하세요 : ")

pw = site.lstrip("http://") #replace("http://", "")
pw = pw[:pw.index(".")]
pw_1 = pw[:3]
pw_2 = len(pw)
pw_3 = pw.count('e')

pw = pw_1 + str(pw_2) + str(pw_3) + "!"
print(f"생성된 비밀번호 : {pw}")