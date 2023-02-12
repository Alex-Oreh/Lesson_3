from smartphone import Smartphone
catalog = []
for i in range(5):
    brand = "brand"  + str(i)
    model = "Model " + str(i)
    number = "Number " + str(i)
    catalog.append(  Smartphone(brand, model, number) )

for i in range(5):
    print(catalog[i].brand,end = ', ')
    print(catalog[i].model,end = ', ')
    print(catalog[i].number)
