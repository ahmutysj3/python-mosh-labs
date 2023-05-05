import converters

kg_weight = 100
lb_weight = converters.kg_to_lbs(kg_weight)
print(lb_weight)

from definitions import move
name = "bob"
move(name)