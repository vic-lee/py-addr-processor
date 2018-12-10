import math
from util import hex_to_bin, bin_to_hex

def get_vpn(addr, vpn_len):
    return addr[:vpn_len]

def get_vpo(addr, vpn_len):
    return addr[vpn_len:]

def get_offset_len(page_size):
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
