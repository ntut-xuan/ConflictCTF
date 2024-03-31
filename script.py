#flag_format = "flag{FLAG_HERE}"

alice = ['0x62', '0x6f', '0x6f', '0x6c', '0x72', '0x6e', '0x63', '0x6e', '0x69', '0x72', '0x76', '0x6e', '0x5f', '0x75', '0x65', '0x75', '0x73', '0x5f', '0x69', '0x7b', '0x61', '0x66']
bob = []

def make_the_list_into_char_list(list: list[str]) -> list[str]:
    array = []
    for i in range(len(list)):
        array.append(chr(int(list[i], base=16)))
    return array

def reverse_the_list(list: list[str]) -> list[str]:
    array = []
    for i in range(len(list)):
        array.append(list[len(list)-1-i])
    return array

def decrease(list: list[str]) -> list[str]:
    return []

def make_flag(alice_key, bob_key):
    for i in range(len(alice_key)):
        print(alice_key[i], end="")
        print(bob_key[i], end="")
    print()

make_flag(
    make_the_list_into_char_list(reverse_the_list(alice)), 
    make_the_list_into_char_list(reverse_the_list(decrease(bob)))
)
