# n = 4
# list_mro=[
#         'A',
#         'B : A',
#         'C : A',
#         'D : B C'
# ]
#
#
# q = 4
# list_q = [
#         'A B',
#         'B D',
#         'C D',
#         'D A'
# ]

list_mro = [  # список введённых строк
    'G : F',  # сначала отнаследуем от F, потом его объявим, корректный алгоритм все равно правильно обойдёт граф, независимо что было раньше: наследование или объявление
    'A',
    'B : A',
    'C : A',
    'D : B C',
    'E : D',
    'F : D',
    # а теперь другая ветка наследования
    'X',
    'Y : X A',  # свяжем две ветки наследования для проверки, обошла ли рекурсия предков Z и предков Y в поисках A
    'Z : X',
    'V : Z Y',
    'W : V',
    'T'
]

list_q = [  # список введённых запросов
    'A G',      # Yes   # A предок G через B/C, D, F
    'A Z',      # No    # Y потомок A, но не Y
    'A W',      # Yes   # A предок W через Y, V
    'X W',      # Yes   # X предок W через Y, V
    'X QWE',    # No    # нет такого класса QWE
    'A X',      # No    # классы есть, но они нет родства :)
    'X X',      # Yes   # родитель он же потомок
    '1 1',      # No    # несуществующий класс
    'T W',
    'T T'
]

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
                        # print('mro_inst',i)
                        if mro[i] is not None:
                            for v in mro[i]:
                                #print('mro_i', v)
                                get_anchestors(inst=i, mro=mro, anc_set=anc_set)
                            #return key
        except KeyError:
            pass

    return anc_set

def create_list_q(list = list_q):
    for i in range(len(list)):
        list[i] = list[i].split()
    return list

mro = create_mro_dict(list_mro)
print(mro)
list_class = create_list_q(list_q)
print(list_class)


for i,v in list_class:
    #print()
    #print(i,v)
    anc_set.clear()
    get_anchestors(inst=v, mro=mro, anc_set=anc_set)
    #print(anc_set)
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
