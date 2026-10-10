"""Release identity attached to results and sponsor traces."""
from pathlib import Path
import subprocess
SPEC_VERSION = '1.5'
SPEC_NAME = 'CaseList Counselor Copilot Build Specification'
ROOT = Path(__file__).parent
try:
    BUILD_COMMIT = subprocess.check_output(['git', '-C', str(ROOT), 'rev-parse', 'HEAD'], text=True).strip()
    WORKING_TREE_MODIFIED = bool(subprocess.check_output(['git', '-C', str(ROOT), 'diff', '--name-only'], text=True).strip())
except (OSError, subprocess.CalledProcessError):
    BUILD_COMMIT, WORKING_TREE_MODIFIED = 'unavailable', True
