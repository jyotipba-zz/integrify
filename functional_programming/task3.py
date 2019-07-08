from itertools import groupby
data = [

        ('orange', 'apple', 'banana'),
        (40,30,50,20, 100),
        ('orange',30,50,20, 100)
    ]

def groupby_demonstrator(data, verify_sorted):
    if verify_sorted:
        sorted_data = sorted(data , key = lambda x: str(x[0]))
        grouped_data = groupby(sorted_data, key = lambda a:a[0])
        for key, grp in grouped_data:
            print('{}: {}'.format(key,list(grp)))
            print('')


groupby_demonstrator(data, True)
