import os
import random
import time
from pathlib import Path

def read_levels_from_set(levelset_path, levels_list):
    with open(levelset_path, "rb") as f:
        unused_bytes = f.read(4)
        total_levels_bytes = f.read(2)
        total_levels = int.from_bytes(total_levels_bytes, "little")
        for x in range(total_levels):
            bytes_in_level_info = f.read(2)
            bytes_in_level = int.from_bytes(bytes_in_level_info, "little")
            level = f.read(bytes_in_level)
            levels_list.append(bytes_in_level_info + level)
        
def create_random_dat(levels_list, number_of_levels):

    # Add the initial data, number of levels
    random_dat = b''
    random_dat += b'\xac\xaa\x02\x00'
    random_dat += (number_of_levels + 1).to_bytes(2, "little")

    # # Level 1 will always be just to load the map, free finish
    # random_dat += b'\x8a\x00\x01\x00\x00\x00\x00\x00\x01\x00Y\x00\xff!\x00\xff\t9\xff\x17\x009\xff\x07;9\xff\x17\x009\xff\x07;9\xff\x17\x009;;\x15\x15\x15;;9\xff\x17\x009;;\x15n\x15;;9\xff\x17\x009;;\x15\x15\x15;;9\xff\x17\x009\xff\x07;9\xff\x17\x009\xff\x07;9\xff\x17\x00\xff\t9\xff\xff\x00\xff\xff\x00\xff\xd8\x00\x0f\x00\xff\xff\x00\xff\xff\x00\xff\xff\x00\xff\xff\x00\xff\x04\x00\x14\x00\x03\x0bGood Luck!\x00\x06\x05\xd8\xd8\xd8\xd8\x00'

    # For each level, add a random level that was scraped, but replace all the passwords with AAAA
    for x in range(number_of_levels):
        random_level = random.choice(levels_list)
        modified_random_level = random_level[0:2] + (x+1).to_bytes(2, "little") + random_level[4:]
        random_dat += modified_random_level

    # Last level can't be finished so you know it's the end
    random_dat += b'\x8a\x00' + (number_of_levels + 1).to_bytes(2, "little") + b'\x00\x00\x00\x00\x01\x00Y\x00\xff!\x00\xff\t9\xff\x17\x009\xff\x07;9\xff\x17\x009\xff\x07;9\xff\x17\x009;;\x00\x00\x00;;9\xff\x17\x009;;\x00n\x00;;9\xff\x17\x009;;\x00\x00\x00;;9\xff\x17\x009\xff\x07;9\xff\x17\x009\xff\x07;9\xff\x17\x00\xff\t9\xff\xff\x00\xff\xff\x00\xff\xd8\x00\x0f\x00\xff\xff\x00\xff\xff\x00\xff\xff\x00\xff\xff\x00\xff\x04\x00\x14\x00\x03\x0bGo Back!!!\x00\x06\x05\xdb\xdb\xdb\xdb\x00'

    return random_dat


def save_random_set(set_info):
    file = open("randomlevelsets/" + "RANDOM_CHIPS_DAT_" + str(int(time.time())) + ".dat", "wb")
    file.write(set_info)
    file.close()

levels_list = []
for filename in os.listdir(Path('levelsets')):
    levelset_path = os.path.join(Path('levelsets'), filename)
    read_levels_from_set(levelset_path, levels_list)

random_dat_bytes = create_random_dat(levels_list, 10)
save_random_set(random_dat_bytes)

