import math

def get_addr_tag(addr, tag_len):
    end_index = tag_len + 1
    return addr[:end_index]

def get_addr_index(addr, index_len, tag_len):
    end_index = index_len + tag_len + 1
    return addr[index_len : end_index]

def get_addr_offset(addr, offset_len):
    addr_len = len(addr)
    start_index = addr_len - offset_len
    # return the last `offset_len` bits of addr
    return addr[start_index:]

def get_offset_len(block_size):
    return (int)(math.log(block_size, 2))

def get_index_len(block_num, set_size):
    num_of_sets = block_num / set_size
    return (int) (math.log(num_of_sets, 2))

def get_tag_len(addr_len, index_len, offset_len):
    return (int) (addr_len - index_len - offset_len)

def is_divisible(numerator, denominator):
    return numerator % denominator == 0

def hex_to_bin(hex_num):
    dec_int = int(hex_num, 16)
    bin_int = bin(dec_int)
    bin_str = str(bin_int)[2:]  # strip out 0b prefix
    return bin_str

def main():
    address_hex = "0xABCDEF"
    address_bin = hex_to_bin(address_hex)
    print(address_bin)
    address_len = len(address_bin)
    block_num = 4096
    set_size = 16      # n-way associative
    block_size = 16
    index_len = get_index_len(block_num, set_size)
    offset_len = get_offset_len(block_size)
    tag_len = get_tag_len(address_len, index_len, offset_len)

    address_tag = get_addr_tag(address_bin, tag_len)
    address_index = get_addr_index(address_bin, index_len, tag_len)
    address_offset = get_addr_offset(address_bin, offset_len)

    print('Tag is {}\nIndex is {}\nOffset is {}\
        '.format(address_tag, address_index, address_offset))

if __name__ == '__main__':
    main()
