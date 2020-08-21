images = []

for i in range(0,10):
    images.append("imagenes_" + str(i) + "_.png")

#[  
#   [imagenes, unvalor, .png],
#   [imagenes, unvalor, .png],
#   [imagenes, unvalor, .png]
#]
list_of_list = []
for img in images:
    list_of_list.append(img.split('_'))
    print(list_of_list)

numbers_of_list = []

for list_element in list_of_list:
    numbers_of_list.append(list_element[1])
    print(numbers_of_list)

counter = max(numbers_of_list)
#delete(path + "imagenes_" + str(min(numbers_of_list)) + "_.png")
print(max(numbers_of_list))
print(numbers_of_list)

numbers_of_list = []

