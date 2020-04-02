"""
You're looking to move into a new apartment, and you're given a list of blocks where each block contains an
apartment
"""

def apartmentHunting(blocks, reqs):
    print()


if __name__ == "__main__":
    # list of hash table
    blocks = [
        {"gym": False, "school": True, "store": False},     # best option so far -> [false,true,false]
        {"gym": True, "school": False, "store": True},      #
        {"gym": True, "school": True, "store": False},
        {"gym": False, "school": True, "store": False},
        {"gym": False, "school": True, "store": True}
    ]

    req = ["gym", "school", "store"] # [True, True, True]