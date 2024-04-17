def reverse_bits(byte):
    # Convert the byte to binary string and reverse it
    reversed_byte = bin(byte)[2:].zfill(8)[::-1]
    # Convert the reversed binary string back to an integer
    return int(reversed_byte, 2)

def reverse_file_bits(input_file, output_file):
    with open(input_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            byte = f_in.read(1)
            while byte:
                # Reverse the bits in the byte
                reversed_byte = reverse_bits(ord(byte))
                # Write the modified byte to the output file
                f_out.write(bytes([reversed_byte]))
                byte = f_in.read(1)

# Example usage:
input_file = 'gnp.galf'
output_file = 'flag.png'

reverse_file_bits(input_file, output_file)
print("Bits reversed successfully and written to", output_file)
