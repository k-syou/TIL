# a, b, c = 9, 2, 3
# pa, pb, pc = a << 8, b << 4, c
# print(pa, bin(pa))
# print(pb, bin(pb))
# print(pc, bin(pc))
# print(pa | pb | pc, bin(pa | pb | pc))

# enc = pa | pb | pc
# d = 4

# da = (pa >> 8) << 8
# print(bin(pa >> 8))
# print(bin(da))
# print(bin(enc))
# print(bin(enc - da))

from itertools import permutations, combinations, product

for x in range(1, 10):
    arr = [*range(x)]
    N = len(arr)
    perm_cnt = 0
    comb_cnt = 0
    prod_cnt = 0
    for i in range(N + 1):
        perm_cnt += len(list(permutations(arr, i)))
        comb_cnt += len(list(combinations(arr, i)))
        prod_cnt += len(list(product(arr, repeat=i)))

    print(f"comb {x}", comb_cnt)
    print(f"perm {x}", perm_cnt)
    print(f"prod {x}", prod_cnt)