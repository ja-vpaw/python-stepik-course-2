# command, namespace, arg = "create", "foo", "global"

# names = {'global':{"var":"some_text", 'foo':{'var_foo':"111111111111", 'var_foo2': "1111111"}, "var2":"ljlj",
#                    'bar':{'var_bar':"some_text", 'var_bar2': "kjlkj", 'foo_in_bar':{'var_foo_in_bar':"some_text",
#                                                                                     'var_foo2_in_bar': "kjlkj"}} }}

names = {'global':{}}

stack = {}

def get_var_stack(namespace="", dictionary=names):

    for i,v in dictionary.items():
        if isinstance(v, dict):
            stack[i] = []
            stack[i].insert(0, namespace)
            get_var_stack(i, v)
        else:
            stack[namespace].append(i)
    return stack

#stack_var = get_var_stack()
# print(stack_var)

def get_var_namespace(namespace=None, var=None):
    stack_var = get_var_stack()
    try:
        vars = stack_var[namespace][1:]
    except KeyError:
        return None
    if var in vars:
        return namespace
    else:
        if stack_var[namespace][0] != "":
            return get_var_namespace(stack_var[namespace][0], var)
        else:
            return None


def create_namespace(namespace=None, parent="global", dictionary=names):
    for i in dictionary.keys():
        if isinstance(dictionary[i], dict):
            if parent in dictionary.keys():
                dictionary[parent][namespace] = {}
            create_namespace(namespace, parent, dictionary=dictionary[i])

def add_namespace_var(namespace="global", var=None, dictionary=names):
    for i in dictionary.keys():
        if isinstance(dictionary[i], dict):
            if namespace in dictionary.keys():
                dictionary[namespace][var] = "some_data"
            add_namespace_var(namespace, var, dictionary=dictionary[i])


iter = int(input())
for i in range(iter):
    command, namespace, arg = input().split()

    if command == "create":
        create_namespace(namespace=namespace, parent=arg)
    elif command == "add":
        add_namespace_var(namespace=namespace, var=arg)
    elif command == "get":
        print(get_var_namespace(namespace=namespace, var=arg))


# print(names)
# create_namespace("super", "global")
# print(names)
# create_namespace("puper", "foo_in_bar")
# print(names)
# print(get_var_namespace("global", "var2"))
# print()
# print(get_var_namespace("foo_in_bar", "var21"))
# print(get_var_namespace("foo_in_bar", "var2"))
# print(get_var_namespace("foo_in_bar", "var_bar2"))
# print(names)
# add_namespace_var("global", "super_var")
# print(names)
# add_namespace_var("foo_in_bar", "super_var_foo_in_bar")
# print(names)
# print(get_var_namespace("foo_in_bar", "super_var_foo_in_bar"))
# print(get_var_namespace("foo_in_bar", "var2"))
# print(get_var_namespace("foo_in_bar", "super_var"))