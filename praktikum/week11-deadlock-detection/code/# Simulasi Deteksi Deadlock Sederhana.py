# Simulasi Deteksi Deadlock Sederhana
# Menggunakan Resource Allocation Graph (RAG)

# Data proses: (Process, Allocation, Request)
processes = [
    ("P1", "R1", "R2"),
    ("P2", "R2", "R3"),
    ("P3", "R3", "R1")
]

# Membuat Resource Allocation Graph
graph = {}

for process, allocation, request in processes:
    if request not in graph:
        graph[request] = []
    graph[request].append(allocation)

# Fungsi untuk mendeteksi cycle (deadlock)
visited = set()
stack = set()

def detect_cycle(node):
    if node in stack:
        return True
    if node in visited:
        return False

    visited.add(node)
    stack.add(node)

    for neighbor in graph.get(node, []):
        if detect_cycle(neighbor):
            return True

    stack.remove(node)
    return False

# Proses deteksi deadlock
deadlock = False
for node in graph:
    if detect_cycle(node):
        deadlock = True
        break

# Output hasil
if deadlock:
    print("⚠️ Deadlock TERDETEKSI")
    print("Proses yang terlibat deadlock:")
    for p in processes:
        print("-", p[0])
else:
    print("✅ Tidak terjadi deadlock")
