"""Compile all .po files to .mo using Babel (no GNU gettext needed)."""
from pathlib import Path
from babel.messages.mofile import write_mo
from babel.messages.pofile import read_po

locale_dir = Path(__file__).parent / 'locale'
for po_path in locale_dir.rglob('*.po'):
    mo_path = po_path.with_suffix('.mo')
    with open(po_path, 'rb') as f:
        catalog = read_po(f)
    with open(mo_path, 'wb') as f:
        write_mo(f, catalog)
    print(f'Compiled: {po_path}')

print('All messages compiled.')
