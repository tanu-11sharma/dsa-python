"""
Restore IP Addresses (Backtracking)
-------------------------------------
Given a string of digits, find every way to insert three dots so the
string splits into exactly four segments, each a valid IPv4 octet
(0-255, no leading zeros unless the segment is exactly "0"). Return
every valid full IP address that can be formed this way.

Time:  O(1) -- at most 4 choices for 3 dot positions, bounded by octet format
Space: O(1) auxiliary beyond the output list
"""


def restore_ip_addresses(digits: str) -> list[str]:
    results: list[str] = []
    n = len(digits)

    def is_valid_octet(segment: str) -> bool:
        if not segment or len(segment) > 3:
            return False
        if segment[0] == "0" and len(segment) > 1:
            return False
        return 0 <= int(segment) <= 255

    def backtrack(start: int, parts: list[str]) -> None:
        if len(parts) == 4:
            if start == n:
                results.append(".".join(parts))
            return
        remaining_parts = 4 - len(parts)
        remaining_chars = n - start
        if not (remaining_parts <= remaining_chars <= remaining_parts * 3):
            return
        for length in range(1, 4):
            if start + length > n:
                break
            segment = digits[start:start + length]
            if is_valid_octet(segment):
                parts.append(segment)
                backtrack(start + length, parts)
                parts.pop()

    backtrack(0, [])
    return results


if __name__ == "__main__":
    print(restore_ip_addresses("25525511135"))
    # expected output: ['255.255.11.135', '255.255.111.35']
    print(restore_ip_addresses("0000"))
    # expected output: ['0.0.0.0']
    print(restore_ip_addresses("101023"))
    # expected output: ['1.0.10.23', '1.0.102.3', '10.1.0.23', '10.10.2.3', '101.0.2.3']
    print(restore_ip_addresses("1111"))
    # expected output: ['1.1.1.1']
