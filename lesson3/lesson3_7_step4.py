from xml.etree import ElementTree

#sample = '<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>'

# sample = '''
# <cube color="blue">
#     <cube color="red">
#         <cube color="green">
#             <cube color="green">
#                 <cube color="green">
#                     <cube color="blue">
#                     </cube>
#                     <cube color="green">
#                     </cube>
#                     <cube color="red">
#                     </cube>
#                 </cube>
#             </cube>
#         </cube>
#     </cube>
#     <cube color="red">
#         <cube color="blue">
#         </cube>
#     </cube>
# </cube>
# '''
#
# root = ElementTree.fromstring(sample)

root = ElementTree.fromstring(input())

ves = 0

ves_dict = {"red": 0, "green": 0, "blue": 0}


def count_tag(element, ves=ves, ves_dict=ves_dict):

    ves += 1

    #print(element.attrib)

    ves_dict[element.attrib['color']] += ves

    #print(ves_dict)

    for child in element:
        count_tag(child, ves)

count_tag(root)

print(ves_dict['red'], ves_dict['green'], ves_dict['blue'])