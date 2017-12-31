list = ['Word1','Word2','Word3']
list2 = [1,2]
x = 'Word4'

#list.append(x)
list.append(x)
print(list)


#list.extend(L)
list.extend(list2)
print(list)


#list.insert(i, x)
list.insert(0,'list.insert()')
print(list)


#list.remove()
list.remove('list.insert()')
print(list)


#list.pop([i]) <= [] for optional
list.pop(-1)
list.pop()
print (list)


#list.index(x)
print (list.index(x))


#list.count()
print (list.count(x))


#list.sort()
list.sort(key=None, reverse=True)
print(list)


#list.reverse()
list.reverse()
print(list)
