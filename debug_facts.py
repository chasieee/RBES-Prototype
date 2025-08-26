def debug_facts(engine):
    """Print semua facts yang ada di working memory untuk debugging"""
    print("\n=== DEBUG: FACTS IN WORKING MEMORY ===")
    
    for fact in engine.facts:
        print(f"Fact: {fact}")
    
    print(f"Total facts: {len(engine.facts)}")
    print("=" * 50)