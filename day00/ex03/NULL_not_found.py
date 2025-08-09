def NULL_not_found(object: any) -> int:
    if type(object) is type(None):
        print(f"Nothing: {object} {type(object)}")
        return 0
    elif type(object) is float and object != object:
        print(f"Cheese: {object} {type(object)}")
        return 0
    elif type(object) is int and object == 0:
        print(f"Zero: {object} {type(object)}")
        return 0
    elif type(object) is str and object == "":
        print(f"Empty: {object} {type(object)}")
        return 0
    elif type(object) is bool and not object:
        print(f"Fake: {object} {type(object)}")
        return 0
    else:
        print("Type not Found")
    return 1


Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))
Empty = "7"
