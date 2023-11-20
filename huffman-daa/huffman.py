import heapq
from collections import defaultdict, Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(data):
    char_freq = Counter(data)
    priority_queue = [HuffmanNode(char, freq) for char, freq in char_freq.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

def build_huffman_codes(node, code="", mapping=None):
    if mapping is None:
        mapping = {}

    if node is not None:
        if node.char is not None:
            mapping[node.char] = code
        build_huffman_codes(node.left, code + "0", mapping)
        build_huffman_codes(node.right, code + "1", mapping)

    return mapping

def huffman_encode(data):
    root = build_huffman_tree(data)
    codes = build_huffman_codes(root)
    encoded_data = "".join(codes[char] for char in data)
    return encoded_data, codes

def huffman_decode(encoded_data, codes):
    reversed_codes = {code: char for char, code in codes.items()}
    decoded_data = ""
    current_code = ""
    
    for bit in encoded_data:
        current_code += bit
        if current_code in reversed_codes:
            decoded_data += reversed_codes[current_code]
            current_code = ""

    return decoded_data

# Example usage:
data = "abracadabra"
encoded_data, huffman_codes = huffman_encode(data)
decoded_data = huffman_decode(encoded_data, huffman_codes)

print("Original data:", data)
print("Encoded data:", encoded_data)
print("Decoded data:", decoded_data)












#orrr








class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    # Count the frequency of each character in the text
    char_frequency = {}
    for char in text:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    # Create a list of Huffman nodes
    nodes = [HuffmanNode(char, freq) for char, freq in char_frequency.items()]

    while len(nodes) > 1:
        # Sort the nodes by frequency
        nodes.sort(key=lambda x: x.freq)

        # Get the two nodes with the lowest frequencies
        left_node = nodes.pop(0)
        right_node = nodes.pop(0)

        # Create a new node with the combined frequency
        merged_node = HuffmanNode(None, left_node.freq + right_node.freq)
        merged_node.left = left_node
        merged_node.right = right_node

        # Add the merged node back to the list of nodes
        nodes.append(merged_node)

    # The remaining node is the root of the Huffman tree
    return nodes[0]


def build_huffman_codes(node, current_code, huffman_codes):
    if node is None:
        return

    # If it's a leaf node (character node), add it to the codes dictionary
    if node.char is not None:
        huffman_codes[node.char] = current_code
        return

    # Traverse left and add '0' to the code, then traverse right and add '1'
    build_huffman_codes(node.left, current_code + '0', huffman_codes)
    build_huffman_codes(node.right, current_code + '1', huffman_codes)


def huffman_encode(text):
    root = build_huffman_tree(text)
    huffman_codes = {}
    build_huffman_codes(root, '', huffman_codes)

    encoded_text = ''.join([huffman_codes[char] for char in text])
    return encoded_text, huffman_codes


def huffman_decode(encoded_text, huffman_codes):
    decoded_text = ''
    current_code = ''

    for bit in encoded_text:
        current_code += bit
        for char, code in huffman_codes.items():
            if code == current_code:
                decoded_text += char
                current_code = ''
                break

    return decoded_text


# Example usage:
text = "this is an example for huffman encoding"
encoded_text, huffman_codes = huffman_encode(text)
print("Encoded text:", encoded_text)
decoded_text = huffman_decode(encoded_text, huffman_codes)
print("Decoded text:", decoded_text)

