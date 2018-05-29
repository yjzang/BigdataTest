s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

s_up = s.upper()
sList = s_up.split()
sList.sort()   # void 라서 값을 받을 수 없다. sorted(sList) 해야 결과가 나온다.  
for s in sList :  
    print(s)

print("\n======================")
sList_set = list(set(sList))  # 중복제거- Set 형태로 , 정렬 - List 형태로 가능하므로 중복제거후 정렬 - set 해주고 다시 list
sList_set.sort()
for x in  sList_set:
    print("%s:%d" %(x,s_up.count(x)))


# 참고 : .sort(reverse=True) 하면 내림차순