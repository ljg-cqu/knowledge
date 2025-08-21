#!/usr/bin/env python3
"""
Preposition Coverage Checker
Analyzes all topic-specific preposition files to check for completeness against the master list.
"""

import os
import re
from pathlib import Path
from collections import defaultdict

# Master list of all prepositions from All_English_Prepositions_with_Examples.md
MASTER_PREPOSITIONS = {
    'aboard', 'about', 'above', 'according to', 'across', 'after', 'against', 'ago',
    'ahead of', 'along', 'along with', 'alongside', 'amid', 'amidst', 'among', 'amongst',
    'anti', 'apart', 'apart from', 'around', 'as', 'as for', 'as of', 'as per',
    'as regards', 'as to', 'as well as', 'aside', 'aside from', 'astride', 'at', 'atop',
    'away', 'away from', 'back', 'barring', 'because of', 'before', 'behind', 'below',
    'beneath', 'beside', 'between', 'beyond', 'but', 'but for', 'by', 'by means of',
    'by virtue of', 'circa', 'close to', 'concerning', 'considering', 'despite', 'down',
    'due to', 'during', 'east', 'except', 'except for', 'excepting', 'excluding',
    'failing', 'following', 'for', 'for the sake of', 'forth', 'from', 'from among',
    'from behind', 'from beneath', 'from under', 'home', 'in', 'in addition to',
    'in front of', 'in lieu of', 'in light of', 'in place of', 'in regard to',
    'in spite of', 'in view of', 'including', 'inside', 'instead of', 'into', 'less',
    'like', 'midst', 'minus', 'near', 'north', 'notwithstanding', 'of', 'off', 'on',
    'on account of', 'on behalf of', 'on top of', 'onto', 'opposite', 'out', 'out of',
    'outside', 'over', 'owing to', 'past', 'pending', 'per', 'plus', 'prior to',
    'qua', 're', 'regarding', 'regardless of', 'respecting', 'round', 'sans', 'save',
    'since', 'south', 'subsequent to', 'than', 'thanks to', 'through', 'throughout',
    'till', 'to', 'touching', 'toward', 'towards', 'under', 'underneath', 'unlike',
    'until', 'up', 'up to', 'upon', 'versus', 'via', 'west', 'with', 'with reference to',
    'with regard to', 'within', 'without', 'worthwhile'
}

def extract_prepositions_from_file(filepath):
    """Extract prepositions mentioned in a topic-specific file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        found_prepositions = set()
        
        # Look for prepositions in various formats
        # 1. Bold prepositions like **aboard**
        bold_pattern = r'\*\*([^*]+)\*\*'
        bold_matches = re.findall(bold_pattern, content)
        
        # 2. Code-formatted prepositions like `aboard`
        code_pattern = r'`([^`]+)`'
        code_matches = re.findall(code_pattern, content)
        
        # 3. Italicized prepositions like *aboard*
        italic_pattern = r'\*([^*]+)\*'
        italic_matches = re.findall(italic_pattern, content)
        
        # Combine all matches
        all_matches = bold_matches + code_matches + italic_matches
        
        # Check if each match is a known preposition
        for match in all_matches:
            match_clean = match.strip().lower()
            if match_clean in MASTER_PREPOSITIONS:
                found_prepositions.add(match_clean)
        
        # Also do a simple word search for each preposition in the master list
        content_lower = content.lower()
        for prep in MASTER_PREPOSITIONS:
            # Use word boundaries to avoid partial matches
            if re.search(r'\b' + re.escape(prep) + r'\b', content_lower):
                found_prepositions.add(prep)
        
        return found_prepositions
    
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return set()

def analyze_all_files():
    """Analyze all topic-specific files for preposition coverage."""
    topic_dir = Path("/home/zealy/github.com/ljg-cqu/knowledge/EnglishLearning/Vocabulary/EnglishPrepositions/TopicSpecificVersions")
    
    if not topic_dir.exists():
        print(f"Directory not found: {topic_dir}")
        return
    
    results = {}
    
    # Get all markdown files
    md_files = sorted(topic_dir.glob("*.md"))
    
    print(f"Analyzing {len(md_files)} topic-specific files...")
    print(f"Master list contains {len(MASTER_PREPOSITIONS)} prepositions.")
    print("-" * 80)
    
    for filepath in md_files:
        filename = filepath.name
        print(f"Processing: {filename}")
        
        found_prepositions = extract_prepositions_from_file(filepath)
        missing_prepositions = MASTER_PREPOSITIONS - found_prepositions
        
        results[filename] = {
            'found': found_prepositions,
            'missing': missing_prepositions,
            'coverage_percent': (len(found_prepositions) / len(MASTER_PREPOSITIONS)) * 100
        }
        
        print(f"  Found: {len(found_prepositions)}/{len(MASTER_PREPOSITIONS)} prepositions ({results[filename]['coverage_percent']:.1f}% coverage)")
    
    print("-" * 80)
    
    # Summary analysis
    print("\n=== COVERAGE SUMMARY ===")
    sorted_results = sorted(results.items(), key=lambda x: x[1]['coverage_percent'], reverse=True)
    
    for filename, data in sorted_results:
        print(f"{filename}: {len(data['found'])}/{len(MASTER_PREPOSITIONS)} ({data['coverage_percent']:.1f}%)")
    
    # Find prepositions that are missing from ALL files
    all_missing = set(MASTER_PREPOSITIONS)
    for data in results.values():
        all_missing &= data['missing']
    
    print(f"\n=== PREPOSITIONS MISSING FROM ALL FILES ({len(all_missing)}) ===")
    if all_missing:
        for prep in sorted(all_missing):
            print(f"  - {prep}")
    else:
        print("  (None - all prepositions appear in at least one file)")
    
    # Find files with lowest coverage
    print(f"\n=== FILES WITH LOWEST COVERAGE ===")
    lowest_coverage = sorted_results[-5:]  # Bottom 5
    for filename, data in lowest_coverage:
        print(f"{filename}: {data['coverage_percent']:.1f}% coverage")
        if len(data['missing']) <= 20:  # Only show if reasonable number
            print(f"  Missing: {', '.join(sorted(list(data['missing'])[:10]))}{'...' if len(data['missing']) > 10 else ''}")
        print()
    
    return results

if __name__ == "__main__":
    results = analyze_all_files()
