def distance_from_zero(mel):
    if type(mel) == int or type(mel) == float:
        return abs(mel)
    else:
        return "Nope"

print(distance_from_zero(-5.6))
print(distance_from_zero("what?"))
