# # List

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# # 조세호씨가 몇 번째 칸에 타고 있는가?
# print(subway.index("조세호"))

# # 하하씨가 다음 정류장에서 다음 칸에 탐
# subway.append("하하")
# print(subway)

# # 정형돈씨를 유재석 / 조세호 사이에 태워봄
# subway.insert(1,"정형돈")
# print(subway)

# # 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# subway.pop()
# print(subway)

# # 같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# # 정렬
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)

# # 순서 뒤집기 가능
# num_list.reverse()
# print(num_list)

# # 모두 지우기
# num_list.clear()
# print(num_list)

# # 다양한 자료형 함께 사용
# num_list = [5,2,4,3,1]
# mix_list = ["조세호", 20, True]

# # 리스트 확장
# num_list.extend(mix_list)
# print(num_list)

#----------------------------------------------------------

# # Dictionary

# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet.get(5))
# print(cabinet.get(5, "사용 가능"))

# print(3 in cabinet) # True
# print(5 in cabinet) # False

# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# #새 손님
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)

# # 간 손님
# del cabinet["A-3"]
# print(cabinet)

# # key들만 출력
# print(cabinet.keys())

# # value들만 출력
# print(cabinet.values())

# # key, value 쌍으로 출력
# print(cabinet.items())

# # 목욕탕 폐점
# cabinet.clear()
# print(cabinet)

#----------------------------------------------------------

# Tuple

# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# # menu.add("생선까스") 튜플이라서 안됨.

# # name = "김종국"
# # age = 20
# # hobby = "코딩"
# # print(name,age,hobby)

# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name,age,hobby)

#----------------------------------------------------------

# # 집합 (Set)
# # 중복 안됨, 순서 없음
# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# # 교집합 (java와 python을 모두 할 수 있는 개발자)
# print(java & python)
# print(java.intersection(python))

# # 합집합 (java할 수 있거나 python 할 수 있는 개발자)
# print(java | python)
# print(java.union(python))

# # 차집합 (java 할 수 있지만 python은 할 수 없는 개발자)
# print(java - python)
# print(java.difference(python))

# # python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# # java를 잊었어요
# java.remove("김태호")
# print(java)

#----------------------------------------------------------

# # 자료구조의 변경
# # 커피숍
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

#----------------------------------------------------------

# Quiz 4

from random import *
users = list(range(1,21)) # 1부터 20까지 숫자 생성
shuffle(users)

winners = sample(users,4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")