print("Testing main app initialization...")

try:
    from src.api.main import app
    print("✓ App imported successfully")
    
    # Test if we can get the routes
    routes = []
    for route in app.routes:
        if hasattr(route, "path"):
            routes.append(route.path)
    
    print(f"✓ Found {len(routes)} routes:")
    for route in routes[:5]:  # Show first 5 routes
        print(f"  - {route}")
        
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
