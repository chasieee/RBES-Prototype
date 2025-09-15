def debug_facts(engine):
    """Print semua facts yang ada di working memory untuk debugging"""
    print("\n=== DEBUG: FACTS IN WORKING MEMORY ===")
    
    for fact in engine.facts:
        print(f"Fact: {fact}")
    
    print(f"Total facts: {len(engine.facts)}")
    print("=" * 50)

def debug_results(engine):
    """Print hasil keputusan dan triggered rules"""
    print("\n=== DEBUG: HASIL KEPUTUSAN ===")
    
    if hasattr(engine, 'results') and engine.results:
        for i, result in enumerate(engine.results, 1):
            print(f"Result {i}: {result}")
    else:
        print("Tidak ada results yang tersimpan")
    
    print(f"\n=== DEBUG: TRIGGERED RULES ===")
    if hasattr(engine, 'triggered_rules') and engine.triggered_rules:
        for i, rule in enumerate(engine.triggered_rules, 1):
            print(f"Rule {i}: {rule}")
    else:
        print("Tidak ada rules yang terpicu")
    
    print("=" * 50)