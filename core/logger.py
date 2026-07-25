from pathlib import Path
from datetime import datetime
LOG=Path('dashboard.log')
def log(msg):
    LOG.open('a',encoding='utf-8').write(f'[{datetime.now():%Y-%m-%d %H:%M:%S}] {msg}\n')
