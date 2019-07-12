
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
                        if mro[i] is not None:
                            for v in mro[i]:
                                get_anchestors(inst=i, mro=mro, anc_set=anc_set)
        except KeyError:
            pass

    return anc_set

anc_set = set()
already_handle = list()
input_parents = []
n = int(input())
for i in range(n):
    input_parents.append(input())

parents = create_parents_dict(input_parents)

q = int(input())
for _ in range(q):

    i = input()
    anc_set.clear()
    already_handle.append(i)
    ancestors = get_anchestors(inst=i, mro=parents, anc_set=anc_set)
    for v in ancestors:
        if v in already_handle:
            print(i)
            break
