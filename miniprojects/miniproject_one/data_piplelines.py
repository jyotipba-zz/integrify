#!/usr/bin/env python
# coding: utf-8
'''Example data pipeline using pandas
  This module demonstrate the how we can build the data pipeline
  using pandas and kwargs to generalize a given function to any kind of input parameters.
 '''
import pandas as pd
import numpy as np
import re
from operator import itemgetter
import argparse

parser = argparse.ArgumentParser(description='Nas to drop')
parser.add_argument('small', type=int)
parser.add_argument('medium', type=int)
parser.add_argument('large', type=int)
args = parser.parse_args()

df = pd.DataFrame({'a':[1,5,np.nan, np.nan], 'b':[1,5,np.nan, 4],'c':[1,np.nan,6, 4]})

axis = 1
kwargs = {'input_':df,'step_1':pd.DataFrame.dropna, 'arg_1':{'axis':axis,'thresh':args.small},
    'step_2':pd.DataFrame.dropna, 'arg_2':{'axis':1,'thresh':args.medium},
'step_3':pd.DataFrame.dropna, 'arg_3':{'axis':1,'thresh':args.large}}
print(args.small, args.medium, args.large)

def recognize_step_i(i, **kwargs):
    '''
     This function returns the function and it's arguments
     involved in each step of data pipeline
     params:
     i : integer type denoting which step in pipeline
     kwargs : keyword arugments

     return : tuple of function and arugments in each step
     '''

    fun_string = f'step_{i}'
    arg_string = f'arg_{i}'
    #print(kwargs[fun_string])
    fnc =  itemgetter(fun_string)(kwargs)  # function to be applied
    arg_dict = itemgetter(arg_string)(kwargs) # dictionary of arguments to be passed to function
    return(fnc, arg_dict)


def dictionary_apply_kwarg_funs(**kwargs):

    dict_keys = kwargs.keys()
    steps = ' '.join(dict_keys)
    how_many_steps= re.findall('step_',steps)
    intermediate = kwargs['input_']
    output_ = {}  # dictionary to hold the ouput from each step in data pipeline

    #if intermediate is not None:
    try:
        for i in range(1,len(how_many_steps)+1):
            step_ID = f'step_{i}'
            fun_, arg_dict_ = recognize_step_i(i, **kwargs)
            intermediate = fun_(intermediate, **arg_dict_)
            print(f'We are currently in step {i} in data pipeline \n')
            print(f'The function name is {fun_.__name__}')
            print(f'The doctring of function is {fun_.__doc__[:50]}')

            output_[step_ID] = intermediate
            print('\n\n')
        return output_
    #else:
    except:
        print('Input data is empty')

output = dictionary_apply_kwarg_funs(**kwargs)
keys = output.keys()
for key in keys:
    print(key)
    print(output[key])
    print('\n')
