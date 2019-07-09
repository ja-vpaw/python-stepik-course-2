#command, namespace, arg = input().split()
command, namespace, arg = "create", "foo", "global"

names = {'global':{"var":"some_text", 'foo':{'var_foo':"some_text"}}}

stack = {}

def get_var_namespace(namespace=None, dictionary=names, stack=stack):

    for i,v in dictionary.items():
        print(i)
        print(v)
        if isinstance(v, dict):
            get_var_namespace(i, v, stack)
        else:
            stack[namespace] = i
    return stack

print(get_var_namespace())



# print(get_namespace("global", "var"))
# print(get_namespace("foo", "var_foo"))
# print(get_namespace_var("var_foo"))
# print(get_namespace_var("var_foo1"))
