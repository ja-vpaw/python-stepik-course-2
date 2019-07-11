key = 0
anc_set = set()

def create_mro_dict(list):
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

list_mro = []

n = int(input())
for i in range(n):
    list_mro.append(input())

mro = create_mro_dict(list_mro)

q = int(input())
for _ in range(q):

    i, v = input().split()
    anc_set.clear()
    get_anchestors(inst=v, mro=mro, anc_set=anc_set)
    if i not in mro.keys():
        print('No')
    elif i == v:
        print('Yes')
    elif v not in mro.keys():
        print('No')
    elif i in anc_set:
        print('Yes')
    else:
        print('No')
