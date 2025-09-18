"""
Simplified Wikipedia Search Agent Package
Single agent in loop with iterative search until answer found
"""

from .agent import (
    root_agent,
    wikipedia_loop,
    wikipedia_agent
)

from .tools import wikipedia_search

__all__ = [
    'root_agent',
    'wikipedia_loop',
    'wikipedia_agent',
    'wikipedia_search'
]