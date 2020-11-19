# checking required packages

# pip freeze > pip_freeze.txt

freeze = []
common = []
dev    = []
prod   = []

with open('pip_freeze.txt', 'r') as f:
    for line in f:
        freeze.append(line)
print(f'Amount freeze: {len(freeze)}')

with open('common.txt', 'r') as f:
    for line in f:
        common.append(line)
print(f'Amount common: {len(common)}')

with open('dev.txt', 'r') as f:
    for line in f:
        dev.append(line)
print(f'Amount dev: {len(dev)}')

# with open('prod.txt', 'r') as f:
#     for line in f:
#         prod.append(line)

freeze_set = set(freeze)
common_set = set(common)
dev_set    = set(dev)
# prod_set   = set(prod)

freeze_uniq_set = freeze_set.difference(dev_set)
print(f'Amount freeze_uniq_set: {len(freeze_uniq_set)}')

common_new_set  = sorted(freeze_uniq_set.union(common_set))
print(f'Amount common_new_set: {len(common_new_set)}')

with open('common.txt', 'w') as f:
    for line in common_new_set:
        f.write(line)

