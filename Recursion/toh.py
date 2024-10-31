def solve_towers_of_hanoi(num_disks, s, a, d):
    # Base case: If there's only one disk, move it directly from source (s) to destination (d)
    if num_disks == 1:
        print(f"Move disk 1 from {s} to {d}")
        return
    # Step 1: Move n-1 disks from source (s) to auxiliary (a) using destination (d) as temporary
    solve_towers_of_hanoi(num_disks - 1, s, d, a)
    # Step 2: Move the nth disk from source (s) to destination (d)
    print(f"Move disk {num_disks} from {s} to {d}")
    # Step 3: Move the n-1 disks from auxiliary (a) to destination (d) using source (s) as temporary
    solve_towers_of_hanoi(num_disks - 1, a, s, d)
# Example usage
num_disks = 2  # You can change this to test with more disks
solve_towers_of_hanoi(num_disks, 's', 'a', 'd')
