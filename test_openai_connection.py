from src.core.config import settings

print("Testing OpenAI API Key Configuration...")
print(f"API Key Configured: {'Yes' if settings.openai_api_key else 'No'}")
print(f"Key starts with: {settings.openai_api_key[:7] if settings.openai_api_key else 'Not set'}")
print(f"Key length: {len(settings.openai_api_key) if settings.openai_api_key else 0}")

# Test actual connection
if settings.openai_api_key:
    try:
        from openai import OpenAI
        client = OpenAI(api_key=settings.openai_api_key)
        
        # Make a simple test call
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say 'Hello, Multi-Agent System is connected!'"}],
            max_tokens=20
        )
        print(f"\n✅ OpenAI Connection Successful!")
        print(f"Response: {response.choices[0].message.content}")
    except Exception as e:
        print(f"\n❌ Error connecting to OpenAI: {e}")
else:
    print("\n⚠️ No API key found. Please add OPENAI_API_KEY to your .env file")
