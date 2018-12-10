import math
from util import hex_to_bin, bin_to_hex

'''
About this script:

Cache Address can be partitioned into:

    |------------------|-----------------|----------|
    |        Tag       |      Index      |  Offset  |

Partitioning a cache address into these components require 5 inputs:
1. The address itself
2. Number of blocks in the cache table
3. The size of each block
4. n-way associativity (set size)

In which:
- number of blocks & n-way associativity    => index length
- the size of each block                    => offset length
- addr length, index length, offset length  => tag length

Author: Vic Lee
'''

def get_addr_tag(addr, tag_len):
    '''Returns the address tag, given tag length'''
    return addr[:tag_len]

def get_addr_index(addr, index_len, tag_len):
    '''Returns the address index, given index length and tag length'''
    end_index = tag_len + index_len
    return addr[tag_len : end_index]

def get_addr_offset(addr, offset_len):
    '''Returns the address offset, given offset length'''
    addr_len = len(addr)
    start_index = addr_len - offset_len
    return addr[start_index:]

def get_offset_len(block_size):
    '''Returns the offset length, given block size in cache'''
    return (int)(math.log(block_size, 2))

def get_index_len(block_num, set_size):
    '''Returns the index length, given total number of blocks and associatity
    '''
    num_of_sets = block_num / set_size
    return (int) (math.log(num_of_sets, 2))

def get_tag_len(addr_len, index_len, offset_len):
    '''Returns the tag length, given address length, index length, offset length
    '''
    return (int) (addr_len - index_len - offset_len)

def partition_addr(addr, tag_len, index_len, offset_len):
    '''Returns the partitions of an address (tag, index, offset)'''
    addr_tag = get_addr_tag(addr, tag_len)
    addr_index = get_addr_index(addr, index_len, tag_len)
    addr_offset = get_addr_offset(addr, offset_len)
    return addr_tag, addr_index, addr_offset

def batch_bin_to_hex(addr1, addr2, addr3):
    return bin_to_hex(addr1), bin_to_hex(addr2), bin_to_hex(addr3)

def get_user_input():
    address_hex = input("Address in hex: ")
    block_num = int(input("Number of blocks in cache: "))
    set_size = int(input("Size of each set (how many ways associative?): "))
    block_size = int(input("Block size (size of each block in cache): "))

    return address_hex, block_num, set_size, block_size

def main():

    address_hex, block_num, set_size, block_size = get_user_input()

    address_bin = hex_to_bin(address_hex)

    print("\nThe address you entered is {} (binary {})\
        ".format(address_hex, address_bin))

    print("\nNumber of blocks: {}\t Size of each set: {}\t Size of each block: {}\
        ".format(block_num, set_size, block_size))

    address_len = len(address_bin)
    index_len = get_index_len(block_num, set_size)
    offset_len = get_offset_len(block_size)
    tag_len = get_tag_len(address_len, index_len, offset_len)

    address_tag, address_index, address_offset = partition_addr(\
        address_bin, tag_len, index_len, offset_len)

    address_tag_hex, address_index_hex, address_offset_hex = batch_bin_to_hex(\
        address_tag, address_index, address_offset)

    print('\nTag (bin) is\t\t{}\nIndex (bin) is\t\t{}\nOffset (bin) is\t\t{}\
        '.format(address_tag, address_index, address_offset))

    print('\nTag (hex) is\t\t{}\nIndex (hex) is\t\t{}\nOffset (hex) is\t\t{}\
        '.format(address_tag_hex, address_index_hex, address_offset_hex))


if __name__ == '__main__':
    main()
