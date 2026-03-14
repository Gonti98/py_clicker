#!/usr/bin/env bash

python3 -c "
from pathlib import Path
save = Path('data/save.json').resolve()
if save.exists():
    save.unlink()
    print(f'Deleted: {save}')
else:
    print('No save file', file=sys.stderr)
    exit(1)
"
