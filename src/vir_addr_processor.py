import math
from util import hex_to_bin, bin_to_hex

'''
About this script:

VA can be partitioned into:

    |------------------------------------|----------------|
    |         Virtual Page Number        |     Offset     |

Partioning an address requires 2 inputs:

1. the address itself
2. page Size

We can derive offset size from page size; after having page size and
the address, we have the size of the VPN. After acquiring the size
of VPN and offset, we perform substring operations to get VPN and offset.

Author: Vic Lee
'''


def get_vpn(addr, vpn_len):
    return addr[:vpn_len]


def get_vpo(addr, vpn_len):
    return addr[vpn_len:]


def get_offset_len(page_size):
    '''
    The length of offset is determined by how large the page size is.
    The larger the page is, the more offset digits are required to
    represent which byte houses the Physical Address is at.
    '''
    return int(math.log(page_size, 2))


def get_vpn_len(addr, offset_len):
    return len(addr) - offset_len


def get_user_input():
    address_hex = input("Address in hex: ")
    page_size = int(input("VA page size: "))
    return address_hex, page_size


def main():
    address_hex, page_size = get_user_input()
    address_bin = hex_to_bin(address_hex)

    offset_len = get_offset_len(page_size)
    vpn_len = get_vpn_len(address_bin, offset_len)

    addr_vpn = get_vpn(address_bin, vpn_len)
    addr_vpo = get_vpo(address_bin, vpn_len)

    addr_vpn_hex = bin_to_hex(addr_vpn)
    addr_vpo_hex = bin_to_hex(addr_vpo)

    print("\nThe Virtual Page Number of your address is {}\n\
        ".format(addr_vpn))
    print("The Virtual Page Offset of your address is {}\n\
        ".format(addr_vpo))

    print("\nThe Virtual Page Number of your address in hex is {}\n\
        ".format(addr_vpn_hex))
    print("The Virtual Page Offset of your address in hex is {}\n\
        ".format(addr_vpo_hex))


if __name__ == '__main__':
    main()
