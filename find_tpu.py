from pycoral.utils.edgetpu import list_edge_tpus

# List available Edge TPUs
edge_tpus = list_edge_tpus()

if edge_tpus:
    print(f"Edge TPU available: {edge_tpus}")
else:
    print("No Edge TPU detected! Running on CPU.")

