# Challenge "Hatch Latch"
![Banner Image](banner.jpg)

You found this hatch. It should be easy to open, but you might need some force.

[hatchlatch.py](hatchlatch.py)

    from random import *

    flag="REDACTED"
    cipher=[]
    kee=randint(1,10000)
    off=randint(1,5)
    for f in flag:
        cipher.append(str((ord(f) - off) ^ kee))

    # print(cipher)
    # ['6255', '6248', '6181', '6183', '6181', '6203', '6258', '6255', '6203', '6267', '6250', '6255', '6230', '6203', '6250', '6250', '6202', '6200', '6200', '6230', '6254', '6245', '6203', '6241', '6267', '6202', '6251', '6256']

# Solution
On the first impression, this might be hard because we have two random inputs kee and off. But since we know the beginning he2024, we can try to derive them first to make them fix for the rest of the flag.



## The flag
    he2024{}
