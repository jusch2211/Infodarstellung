def codepoint_to_utf8(cp):
    """Convert Unicode code point (int) to list of UTF-8 bytes (binary strings)."""
    return [f"{b:08b}" for b in chr(cp).encode("utf-8")]

def utf8_to_codepoint(byte_list):
    """Convert list of UTF-8 bytes (as binary strings) back to a code point."""
    raw_bytes = bytes(int(b, 2) for b in byte_list)
    return ord(raw_bytes.decode("utf-8"))

def string_to_ascii_bits(text: str) -> list[str]:
    """Konvertiert einen String in eine Liste von 8-Bit-ASCII-Bitstrings."""
    return [format(ord(char), '08b') for char in text]

def main():
    print(codepoint_to_utf8(0x00F6))
    print(string_to_ascii_bits("Moin"))
    examples = {
        "A (U+0041)": 0x41,
        "ö (U+00F6)": 0x00F6,
        "😀 (U+1F600)": 0x1F600
    }

    #output = {}

    #for name, cp in examples.items():
    #    utf8_bytes = codepoint_to_utf8(cp)
    #    restored_cp = utf8_to_codepoint(utf8_bytes)
    #    output[name] = {
    #        "original_codepoint_hex": hex(cp),
    #        "utf8_bitpattern": utf8_bytes,
    #        "restored_codepoint_hex": hex(restored_cp)
    #    }

    #for name, data in output.items():
    #    print(f"{name}:")
    #    print(f"  Original Codepoint: {data['original_codepoint_hex']}")
    #    print(f"  UTF-8 Bit Pattern: {data['utf8_bitpattern']}")
    #    print(f"  Restored Codepoint: {data['restored_codepoint_hex']}\n")

if __name__ == "__main__":
    main()
