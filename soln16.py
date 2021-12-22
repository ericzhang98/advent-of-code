with open('input16.txt') as f:
    line = f.readline().strip()
hex_map = {
        '0' : '0000',
        '1' : '0001',
        '2' : '0010',
        '3' : '0011',
        '4' : '0100',
        '5' : '0101',
        '6' : '0110',
        '7' : '0111',
        '8' : '1000',
        '9' : '1001',
        'A' : '1010',
        'B' : '1011',
        'C' : '1100',
        'D' : '1101',
        'E' : '1110',
        'F' : '1111',
}
def parse_hex(line):
    txt = []
    for c in list(line):
        txt.append(hex_map[c])
    txt = "".join(txt)
    return txt
def parse_literal(s):
    b = []
    i = 0
    while True:
        b.append(s[i+1:i+5])
        if s[i] == '0':
            i += 5
            break
        i += 5
    b = int("".join(b), 2)
    return b, i+6
i = 0
def parse_packet(s):
    print(s)
    packet_version = int(s[:3], 2)
    type_id = int(s[3:6], 2)
    print('packet version', packet_version, 'type id', type_id)
    if type_id == 4:
        print('literal')
        literal, di = parse_literal(s[6:])
        print('literal value', literal)
        return [], literal, packet_version, type_id, di
    else:
        print('subpacket')
        subpacket_list = []
        if s[6] == '0':
            bitlength = int(s[7:22], 2)
            print('bitlength', bitlength)
            i = 22
            while True:
                subpackets, literal, packet_version2, type_id2, di = parse_packet(s[i:])
                subpacket_list.append((subpackets, literal, packet_version2, type_id2))
                i += di
                print('di', di)
                print('i', i)
                print('check', i-22, bitlength)
                if i - 22 == bitlength:
                    print('break')
                    break
                if i - 22 > bitlength:
                    raise Exception('rip')
        else:
            subpacket_cnt = int(s[7:18], 2)
            i = 18
            for _ in range(subpacket_cnt):
                subpackets, literal, packet_version2, type_id2, di = parse_packet(s[i:])
                subpacket_list.append((subpackets, literal, packet_version2, type_id2))
                i += di
        print('returning', subpacket_list, None, packet_version)
        return subpacket_list, None, packet_version, type_id, i

def parse(s):
    return parse_packet(s)[:4]

#print(parse_packet('00111000000000000110111101000101001010010001001000000000'))
print(parse_packet('11101110000000001101010000001100100000100011000001100000'))

def sum_versions(packet):
    print(packet)
    subpacket_list, literal, packet_version, type_id = packet
    if literal is not None:
        return packet_version
    res = packet_version
    for subpacket in subpacket_list:
        res += sum_versions(subpacket)
    return res

def compute(packet):
    print(packet)
    subpacket_list, literal, packet_version, type_id = packet
    if type_id == 0:
        return sum(compute(subpacket) for subpacket in subpacket_list)
    elif type_id == 1:
        import functools
        return functools.reduce(lambda a,b:a*b, (compute(subpacket) for subpacket in subpacket_list))
    elif type_id == 2:
        return min(compute(subpacket) for subpacket in subpacket_list)
    elif type_id == 3:
        return max(compute(subpacket) for subpacket in subpacket_list)
    elif type_id == 4:
        return literal
    elif type_id == 5:
        return int(compute(subpacket_list[0]) > compute(subpacket_list[1]))
    elif type_id == 6:
        return int(compute(subpacket_list[0]) < compute(subpacket_list[1]))
    elif type_id == 7:
        return int(compute(subpacket_list[0]) == compute(subpacket_list[1]))

#print(sum_versions(parse(parse_hex('8A004A801A8002F478'))))
#print(sum_versions(parse(parse_hex('A0016C880162017C3686B18A3D4780'))))
#print(sum_versions(parse(parse_hex(line))))
print(compute(parse(parse_hex(line))))
