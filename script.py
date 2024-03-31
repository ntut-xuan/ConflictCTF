import random

# flag_format = "flag{FLAG_HERE}"

alice = []
bob = ['0x81', '0x6a', '0x7c', '0x66', '0x6f', '0x7b', '0x71', '0x66', '0x77', '0x7b', '0x6e', '0x62', '0x6b', '0x6d', '0x67', '0x79', '0x64', '0x69', '0x75', '0x68', '0x6d', '0x6c']

def make_the_list_into_char_list(array):
    return list(map(chr, [int(x, base=16) for x in array]))

def reverse_the_list(list):
    array = []
    for i in range(len(list)):
        array.append(list[len(list)-1-i])
    return array

def decrease(list):
    random.seed("bob")
    for i in range(len(list)):
        list[i] = hex(int(list[i], base=16) - int(random.random() * 10))
    return list

def make_flag(alice_key, bob_key):
    for i in range(len(alice_key)):
        print(alice_key[i], end="")
        print(bob_key[i], end="")
    print()

make_flag(
    make_the_list_into_char_list(reverse_the_list(alice)), 
    make_the_list_into_char_list(reverse_the_list(decrease(bob)))
)