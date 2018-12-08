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

mem_values = {}

def get_value(node_id):
    if node_id in mem_values:
        return mem_values[node_id]
    if len(childs[node_id]) == 0:
        mem_values[node_id] = sum(metadata[node_id])
        return mem_values[node_id]
    val = 0
    for meta in metadata[node_id]:
        if meta == 0 or meta > len(childs[node_id]):
            continue
        val += get_value(childs[node_id][meta-1])
    mem_values[node_id] = val
    return val

parse_node(0)
#explore_tree(0, 0)

print(get_value(0))
