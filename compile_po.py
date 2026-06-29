import struct, os, re

def unescape(s):
    """Convert PO file escape sequences to actual characters."""
    return s.replace('\\\\', '\x00BACKSLASH\x00').replace('\\n', '\n').replace('\\t', '\t').replace('\\"', '"').replace('\x00BACKSLASH\x00', '\\')

def compile_po(po_path, mo_path):
    entries = {}
    cur_id = []
    cur_str = []
    in_id = False
    in_str = False

    with open(po_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    def flush():
        nonlocal cur_id, cur_str
        if cur_id is not None and cur_str is not None:
            k = unescape(''.join(cur_id))
            v = unescape(''.join(cur_str))
            entries[k] = v
        cur_id = []
        cur_str = []

    for line in lines:
        line = line.rstrip('\n')
        if line.startswith('msgid "'):
            if in_str:
                flush()
            in_id = True
            in_str = False
            cur_id = [line[7:-1]]
        elif line.startswith('msgstr "'):
            in_id = False
            in_str = True
            cur_str = [line[8:-1]]
        elif line.startswith('"') and in_id:
            cur_id.append(line[1:-1])
        elif line.startswith('"') and in_str:
            cur_str.append(line[1:-1])
        else:
            if in_str:
                flush()
            in_id = False
            in_str = False

    if in_str:
        flush()

    valid = {k: v for k, v in entries.items() if k != '' and v != ''}
    header = entries.get('', '')
    if not header or ('charset' not in header.lower()):
        header = 'Content-Type: text/plain; charset=UTF-8\nContent-Transfer-Encoding: 8bit\n'

    all_entries = [('', header)] + sorted(valid.items())

    ids  = [k.encode('utf-8') for k, v in all_entries]
    strs = [v.encode('utf-8') for k, v in all_entries]
    n = len(ids)

    # Standard MO header: exactly 7 uint32s = 28 bytes
    header_size    = 28
    ids_offset     = header_size
    strs_offset    = ids_offset  + 8 * n
    ids_data_off   = strs_offset + 8 * n
    strs_data_off  = ids_data_off + sum(len(b) + 1 for b in ids)

    hdr = struct.pack('<IIIIIII', 0x950412de, 0, n, ids_offset, strs_offset, 0, 0)

    id_table  = b''
    str_table = b''
    ids_data  = b''
    strs_data = b''

    cur_id_off  = ids_data_off
    for b in ids:
        id_table += struct.pack('<II', len(b), cur_id_off)
        ids_data += b + b'\x00'
        cur_id_off += len(b) + 1

    cur_str_off = strs_data_off
    for b in strs:
        str_table += struct.pack('<II', len(b), cur_str_off)
        strs_data += b + b'\x00'
        cur_str_off += len(b) + 1

    with open(mo_path, 'wb') as f:
        f.write(hdr + id_table + str_table + ids_data + strs_data)

    return n

base = r'c:\Users\cengi\Desktop\gfenixfinal\locale'
for lang in ['tr', 'es', 'ca']:
    po = os.path.join(base, lang, 'LC_MESSAGES', 'django.po')
    mo = os.path.join(base, lang, 'LC_MESSAGES', 'django.mo')
    n = compile_po(po, mo)
    print(f'{lang}: {n} entries')
