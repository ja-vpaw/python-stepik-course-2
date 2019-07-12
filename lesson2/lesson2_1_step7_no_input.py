input_parents = [
    'ArithmeticError',
    'ZeroDivisionError : ArithmeticError',
    'OSError',
    'FileNotFoundError : OSError'
]

input_exceptions = [
    'ZeroDivisionError',
    'OSError',
    'ArithmeticError',
    'FileNotFoundError'
]



def create_parents_dict(list):
    mro = {}
    for i in range(len(list)):
        a = list[i].split(' : ')
        try:
            mro[a[0]] = a[1].split()
        except IndexError:
            mro[a[0]] = None

    return mro


def get_anchestors(inst=None, mro=None, anc_set=None):

    if inst not in mro.keys():
        pass
    else:
        try:
            if mro[inst] is None:
                pass
            elif isinstance(mro[inst], list):
                for _ in mro[inst]:
                    anc_set.add(_)
                else:
                    for i in mro[inst]:
                        # print('mro_inst',i)
                        if mro[i] is not None:
                            for v in mro[i]:
                                #print('mro_i', v)
                                get_anchestors(inst=i, mro=mro, anc_set=anc_set)
                            #return key
        except KeyError:
            pass

    return anc_set

anc_set = set()
parents = create_parents_dict(input_parents)
print(parents)
already_handle = list()

for i in input_exceptions:
    print()
    print(i)
    anc_set.clear()
    already_handle.append(i)
    print('already handle', already_handle)
    ancestors = get_anchestors(inst=i, mro=parents, anc_set=anc_set)
    print('anchestors',ancestors)
    for v in ancestors:
        if v in already_handle:
            print(i)
            break

