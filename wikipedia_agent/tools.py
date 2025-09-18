"""
Wikipedia Search Tool for simplified agent
"""

import wikipedia

def wikipedia_search(query: str) -> str:
    """
    Search Wikipedia and return a summary.

    Args:
        query (str): Search query for Wikipedia

    Returns:
        str: Wikipedia summary or error message
    """
    try:
        # Try to get summary directly
        result = wikipedia.summary(query, sentences=3)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        # If multiple options, try the first one
        try:
            result = wikipedia.summary(e.options[0], sentences=3)
            return f"Found: {e.options[0]} - {result}"
        except:
            return f"Multiple results found: {', '.join(e.options[:3])}"
    except wikipedia.exceptions.PageError:
        # If page not found, try search
        try:
            search_results = wikipedia.search(query, results=1)
            if search_results:
                result = wikipedia.summary(search_results[0], sentences=3)
                return f"Found: {search_results[0]} - {result}"
            else:
                return f"No Wikipedia results found for: {query}"
        except:
            return f"No Wikipedia results found for: {query}"
    except Exception as e:
        return f"Wikipedia search error for '{query}': {str(e)}"