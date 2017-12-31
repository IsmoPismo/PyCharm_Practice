print ('Unpacking a TUPLE *args')

x =(range(3,6))
print (list(x))
args=[3,6]
print(list(range(*args)))


print ('\nUnpacking KEYS **kwargs')

def papiga(voltaza, stanje='ukocen', pokrez='voom'):
    return (voltaza + ' ' + stanje + ' ' + pokrez)

d = {"voltaza":"sto","stanje":"mrtav","pokrez":"nikakav"}
print (papiga(**d))
