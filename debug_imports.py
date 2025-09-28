print("Testing imports...")

try:
    import src
    print("✓ src module found")
except Exception as e:
    print(f"✗ src module error: {e}")

try:
    from src.core import logger
    print("✓ logger imported")
except Exception as e:
    print(f"✗ logger error: {e}")

try:
    from src.api.main import app
    print("✓ app imported successfully")
except Exception as e:
    print(f"✗ app import error: {e}")
    
print("\nPython path:")
import sys
for path in sys.path:
    print(f"  - {path}")
