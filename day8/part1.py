license = [int(e) for e in open("day8.input", "r").read().rstrip().split(" ")]

metadata = {}
childs = {}

node_ctr = 0

def parse_node(idx):
    global license, node_ctr
    node_id = node_ctr
    node_ctr += 1
    child_num = license[idx]
    meta_num = license[idx+1]
    metadata[node_id] = []
    childs[node_id] = []
    metadata_begin = idx+2
    for ch_idx in range(child_num):
        childs[node_id].append(node_ctr)
        metadata_begin = parse_node(metadata_begin)
    for m_idx in range(metadata_begin, metadata_begin+meta_num):
        metadata[node_id].append(license[m_idx])
    return metadata_begin+meta_num

def explore_tree(node_id, rec):
    print("%s#%d: %r" % ("\t"*rec, node_id, metadata[node_id]))
    for ch in childs[node_id]:
        explore_tree(ch, rec+1)

parse_node(0)
#explore_tree(0, 0)

total = 0
for node in metadata:
    total += sum(metadata[node])

print(total)
