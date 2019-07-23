def is_divisible(numerator, denominator):
    return numerator % denominator == 0


def hex_to_bin(hex_str):
    dec_int = int(hex_str, 16)
    bin_int = bin(dec_int)
    bin_str = str(bin_int)[2:]  # strip out 0b prefix
    return bin_str


def bin_to_hex(bin_str):
    dec_int = int(bin_str, 2)
    hex_int = hex(dec_int)
    hex_str = str(hex_int)[2:]  # strip out 0x prefix
    hex_str = hex_str.upper()
    return hex_str
