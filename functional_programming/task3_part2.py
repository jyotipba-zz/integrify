from itertools import groupby

data = [

        ('orange', 'apple', 'banana'),
        (40,30,50,20, 100),
        ('orange',30,50,20, 100)
    ]

def sort_tuple(fun):
    def wrapper_fun(*args,**kwargs):
        if kwargs.get('verify_sorted')==True:
            sorted_value=sorted(*args,key=lambda x:str(x[0]))
            fun(sorted_value,**kwargs)
        else :
            print('You didn’t enforce the order')
    return wrapper_fun

@sort_tuple
def groupby_demonstrator(data, **verify_sorted):
    grouped_data = groupby(data, key = lambda a:str(a[0]))
    for key, grp in grouped_data:
        print('{}: {}'.format(key,list(grp)))
        print('')

groupby_demonstrator(data, verify_sorted=True)
