from operator import itemgetter
# 按名字排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0].lower()
L2 = sorted(L, key=by_name)
print(L2)

#按成绩由高到低
def by_score(t):
    return -t[1]
L2 = sorted(L, key=by_score)
print(L2)
L=['bob','about','Zoo','Credit']
print(sorted(L))
print(sorted(L,key=str.lower))
students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))