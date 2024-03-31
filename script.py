flag_format = "flag{FLAG_HERE}"

alice = []
bob = []

def make_the_list_into_char_list(list: list[str]) -> list[str]:
    return []

def reverse_the_list(list: list[str]) -> list[str]:
    return []

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

print(flag_format)