import torch
from torch_geometric.data import Data, InMemoryDataset

class TestDataset(InMemoryDataset):
	def __init__(self, data_list):
		super(TestDataset, self).__init__('/tmp/TestDataset')
		self.data, self.slices = self.collate(data_list)

	def _download(self):
		pass
	def _process(self):
		pass

def MyDataset(path, dataset_name):
    # Initialize graph ID (taken directly from model argument, not actually used below)
    # graphId = model
    
    # Counters for nodes, node types, and edge types
    node_cnt = 0
    nodeType_cnt = 0
    edgeType_cnt = 0
    
    # Storage for parsed provenance data (edges with mapped IDs/types)
    provenance = []
    
    # Dictionaries for mapping raw IDs/types/edges to integer indices
    nodeType_map = {}
    edgeType_map = {}
    
    # Lists of edge sources and edge destinations (for graph construction)
    edge_s = []
    edge_e = []
    
    # Threshold value (currently unused)
    data_thre = 1000000

    # Outer loop (only runs once, could be generalized if needed)
    for out_loop in range(1):
        f = open(path, 'r')  # Open provenance file for reading

        nodeId_map = {}  # Map raw node IDs (strings) → integer indices

        for line in f:
            # Each line expected format: srcId, srcType, dstId, dstType, edgeType
            temp = line.strip('\n').split('\t')
            
            # Map source node ID to integer index if new
            if not (temp[0] in nodeId_map.keys()):
                nodeId_map[temp[0]] = node_cnt
                node_cnt += 1
            temp[0] = nodeId_map[temp[0]]
            
            # Map destination node ID to integer index if new
            if not (temp[2] in nodeId_map.keys()):
                nodeId_map[temp[2]] = node_cnt
                node_cnt += 1
            temp[2] = nodeId_map[temp[2]]

            # Map source node type to integer index if new
            if not (temp[1] in nodeType_map.keys()):
                nodeType_map[temp[1]] = nodeType_cnt
                nodeType_cnt += 1
            temp[1] = nodeType_map[temp[1]]

            # Map destination node type to integer index if new
            if not (temp[3] in nodeType_map.keys()):
                nodeType_map[temp[3]] = nodeType_cnt
                nodeType_cnt += 1
            temp[3] = nodeType_map[temp[3]]
            
            # Map edge type to integer index if new
            if not (temp[4] in edgeType_map.keys()):
                edgeType_map[temp[4]] = edgeType_cnt
                edgeType_cnt += 1
            temp[4] = edgeType_map[temp[4]]

            # Store edge endpoints
            edge_s.append(temp[0])
            edge_e.append(temp[2])
            
            # Save mapped edge entry for later processing
            provenance.append(temp)

    # Save edge type mapping to file (feature.txt)
    f_train_feature = open(f'../models/{dataset_name}/feature.txt', 'w')
    for i in edgeType_map.keys():
        f_train_feature.write(str(i) + '\t' + str(edgeType_map[i]) + '\n')
    f_train_feature.close()

    # Save node type mapping to file (label.txt)
    f_train_label = open(f'../models/{dataset_name}/label.txt', 'w')
    for i in nodeType_map.keys():
        f_train_label.write(str(i) + '\t' + str(nodeType_map[i]) + '\n')
    f_train_label.close()

    # Number of edge types = number of features
    feature_num = edgeType_cnt
    label_num = nodeType_cnt

    # Initialize feature matrix (x_list), labels (y_list), and masks
    x_list = []
    y_list = []
    train_mask = []
    test_mask = []

    for i in range(node_cnt):
        # Each node has 2 × feature_num features (incoming + outgoing edge counts)
        temp_list = [0] * (feature_num * 2)
        x_list.append(temp_list)

        # Default label = 0 (will be overwritten)
        y_list.append(0)

        # Mark all nodes as available for training/testing
        train_mask.append(True)
        test_mask.append(True)

    # Populate feature and label matrices from provenance edges
    for temp in provenance:
        srcId = temp[0]   # integer ID of source node
        srcType = temp[1] # mapped type ID of source node
        dstId = temp[2]   # integer ID of destination node
        dstType = temp[3] # mapped type ID of destination node
        edge = temp[4]    # mapped type ID of edge

        # Outgoing edge contributes to source features
        x_list[srcId][edge] += 1
        y_list[srcId] = srcType

        # Incoming edge contributes to destination features
        x_list[dstId][edge + feature_num] += 1
        y_list[dstId] = dstType

    # Convert lists into PyTorch tensors
    x = torch.tensor(x_list, dtype=torch.float)   # Node features
    y = torch.tensor(y_list, dtype=torch.long)    # Node labels
    train_mask = torch.tensor(train_mask, dtype=torch.bool)
    test_mask = train_mask                       # Train = test (no split here)
    edge_index = torch.tensor([edge_s, edge_e], dtype=torch.long)  # Edge list

    # Create PyTorch Geometric Data object
    data1 = Data(
        x=x, y=y,
        edge_index=edge_index,
        train_mask=train_mask,
        test_mask=test_mask
    )

    # Double feature_num (outgoing + incoming features)
    feature_num *= 2

    # Return dataset list, feature count, label count, and two unused zeros
    return [data1], feature_num, label_num

# Example:
# input
# A   process   B   file   open
# A   process   B   file   open
# B   file      C   socket send
# Built data
# x = [
#  [2,0,  0,0],   # Node A: 2 outgoing 'open'
#  [0,1,  1,0],   # Node B: 1 outgoing 'send', 1 incoming 'open'
#  [0,0,  0,1],   # Node C: 1 incoming 'send'
# ]
# y = [0,1,2]     # [process, file, socket]
# edge_index = [[0,1],
#               [1,2]]
# train_mask = [True, True, True]
# test_mask  = [True, True, True]