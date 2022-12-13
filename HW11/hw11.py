def play_with_list():
    print("list1 = [1,4,2,6,4,3,7,5,2,4,8]")
    list1 = [1,4,2,6,4,3,7,5,2,4,8]

    print("list1.sort()")
    list1.sort()
    print(list1)

    print("list1.count(2)")
    print(list1.count(2))

    print("list1.pop(-1)")
    print(list1.pop(-1))

def play_with_dics():
    print('dict1 = {"a":26,"b":2.3,"c":7.3,"d":56.76,"e":3,"f":546,"g":7,"h":34,"i":457, "j":23,}')
    dict1 = {"a":26,"b":2.3,"c":7.3,"d":56.76,"e":3,"f":546,"g":7,"h":34,"i":457, "j":23,}

    print('dict1.get("k", "NOT HERE")')
    print(dict1.get("k", "NOT HERE"))

    print("dict1 = {k: v for k, v in sorted(dict1.items(), key=lambda item: item[1])}")
    dict1 = {k: v for k, v in sorted(dict1.items(), key=lambda item: item[1])}
    print(dict1)

if __name__ == "__main__":
    play_with_list()
    print("\n--------------------\n")
    play_with_dics()

    
    
