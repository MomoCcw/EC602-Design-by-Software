#!/Users/francischen/opt/anaconda3/bin/python
#pythons sorts are STABLE: order is the same as original in tie.
# sort: key, reverse

q = ['two','twelve','One','3']

#sort q, result being a modified list. nothing is returned
q.sort()
print(q)

q = ['two','twelve','One','3',"this has lots of t's"]
q.sort(reverse=True)
print(q)

def f(x):
	return x.count('t')

q.sort(key = f)	
print(q)
q = ['twelve','two','One','3',"this has lots of t's"]

q.sort(key=f)
print(q)

#Multiple sorts
q = ['twelve','two','One','3',"this has lots of t's"]
q.sort()
q.sort(key=f)

# sort based on 1,2,and then 3
# sort 3, then sort 2, then sort 1

print(q)


def complicated(x):
	return(x.count('t'),len(x),x)

q = ['two','otw','wot','Z','t','tt','longer t']

q.sort(key=complicated)
print(q)