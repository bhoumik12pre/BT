# Program: Huffman Encoding using Greedy Strategy
# Aim: To implement Huffman Encoding algorithm using greedy approach
# and understand how data compression works by assigning variable-length codes.

import heapq                        # 'heapq' is used to implement a priority queue (min-heap)

# --- Class to represent each node of the Huffman Tree ---
class Node:
    def __init__(self, char, freq):  # Constructor to initialize character and its frequency
        self.char = char             # Store character (like 'a', 'b', etc.)
        self.freq = freq             # Store frequency of that character
        self.left = None             # Left child node
        self.right = None            # Right child node

    # Logic: For the heap to work, we need to compare nodes based on their frequencies
    def __lt__(self, other):
        return self.freq < other.freq


# --- Function to build Huffman Tree ---
def build_huffman_tree(char_freq):
    # Logic: Create a min-heap using character frequencies
    heap = [Node(char, freq) for char, freq in char_freq.items()]  # Convert each char-freq pair into a Node
    heapq.heapify(heap)                    # Convert list into a heap (priority queue based on freq)

    # Logic: Combine two smallest nodes until only one tree remains
    while len(heap) > 1:
        left = heapq.heappop(heap)         # Pop node with smallest frequency
        right = heapq.heappop(heap)        # Pop second smallest node

        # Create a new internal node with frequency = sum of two smallest nodes
        merged = Node(None, left.freq + right.freq)
        merged.left = left                 # Left child → smaller frequency node
        merged.right = right               # Right child → next smallest node

        heapq.heappush(heap, merged)       # Push the merged node back to heap

    # Finally, heap will contain only one node — the root of the Huffman Tree
    return heap[0]


# --- Function to generate Huffman Codes ---
def generate_codes(node, current_code, codes):
    # Base condition: If node is empty, return
    if node is None:
        return

    # Logic: If a leaf node is reached (means it has a character)
    if node.char is not None:
        codes[node.char] = current_code    # Store the character and its Huffman code
        return

    # Logic: Traverse left (add '0') and right (add '1') recursively
    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)


# --- Main Program ---
# Step 1: Take input from user
text = input("Enter a string to encode: ")

# Step 2: Calculate frequency of each character
char_freq = {}
for ch in text:
    char_freq[ch] = char_freq.get(ch, 0) + 1   # Count how many times each character appears

# Step 3: Build Huffman Tree using the greedy approach
root = build_huffman_tree(char_freq)

# Step 4: Generate Huffman Codes
codes = {}
generate_codes(root, "", codes)

# Step 5: Display each character with its Huffman code
print("\n--- Huffman Codes for each character ---")
for char, code in codes.items():
    print(f"{char} : {code}")

# Step 6: Encode the original text using the generated Huffman codes
encoded_text = "".join(codes[ch] for ch in text)
print("\nEncoded text:", encoded_text)

# Step 7: Display Time and Space Complexity
print("\n--- Time and Space Complexity ---")
print("Time Complexity: O(n log n)  (due to heap operations while building the tree)")
print("Space Complexity: O(n)       (for storing the tree and code dictionary)")






# Enter a string to encode: aabcddd

# --- Huffman Codes for each character ---
# a : 10
# b : 110
# c : 111
# d : 0

# Encoded text: 10101110000

# --- Time and Space Complexity ---
# Time Complexity: O(n log n)
# Space Complexity: O(n)
