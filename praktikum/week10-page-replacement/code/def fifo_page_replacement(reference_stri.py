def fifo_page_replacement(reference_string, frames):
    memory = []
    page_faults = 0
    index = 0

    print("=== FIFO Page Replacement ===")
    for page in reference_string:
        if page not in memory:
            page_faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                memory[index] = page
                index = (index + 1) % frames
            status = "Page Fault"
        else:
            status = "Page Hit"

        print(f"Page: {page} -> Memory: {memory} ({status})")

    print(f"Total Page Fault FIFO: {page_faults}\n")
    return page_faults


def lru_page_replacement(reference_string, frames):
    memory = []
    page_faults = 0
    recent_use = {}

    print("=== LRU Page Replacement ===")
    for i, page in enumerate(reference_string):
        if page not in memory:
            page_faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                lru_page = min(memory, key=lambda p: recent_use[p])
                memory[memory.index(lru_page)] = page
            status = "Page Fault"
        else:
            status = "Page Hit"

        recent_use[page] = i
        print(f"Page: {page} -> Memory: {memory} ({status})")

    print(f"Total Page Fault LRU: {page_faults}\n")
    return page_faults


if __name__ == "__main__":
    reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    frames = 3

    fifo_faults = fifo_page_replacement(reference_string, frames)
    lru_faults = lru_page_replacement(reference_string, frames)

    print("=== Perbandingan ===")
    print(f"FIFO Page Faults: {fifo_faults}")
    print(f"LRU Page Faults : {lru_faults}")
