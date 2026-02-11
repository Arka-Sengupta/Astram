import os
import subprocess
import platform
from duckduckgo_search import DDGS

class Tools:
    @staticmethod
    def read_file(path):
        try:
            with open(path, 'r') as f:
                return f.read()
        except Exception as e:
            return f"Error reading file: {e}"

    @staticmethod
    def write_file(path, content):
        try:
            # Ensure directory exists (only if there's a directory component)
            dir_path = os.path.dirname(path)
            if dir_path and not os.path.exists(dir_path):
                os.makedirs(dir_path, exist_ok=True)
            with open(path, 'w') as f:
                f.write(content)
            return f"Successfully wrote to {path}"
        except Exception as e:
            return f"Error writing file: {e}"

    @staticmethod
    def list_files(directory="."):
        try:
            return os.listdir(directory)
        except Exception as e:
            return f"Error listing files: {e}"

    @staticmethod
    def run_command(command):
        try:
            # Platform specific shell command execution
            system = platform.system()
            if system == "Windows":
                 result = subprocess.run(command, shell=True, capture_output=True, text=True)
            else:
                 result = subprocess.run(command, shell=True, capture_output=True, text=True, executable='/bin/bash')
            
            return f"Output:\n{result.stdout}\nErrors:\n{result.stderr}"
        except Exception as e:
            return f"Error running command: {e}"

    @staticmethod
    def search_web(query, max_results=5):
        """
        Search the web using DuckDuckGo and return formatted results.
        
        Args:
            query: Search query string
            max_results: Maximum number of results to return (default: 5)
            
        Returns:
            Formatted string with search results including titles, snippets, and URLs
        """
        try:
            with DDGS() as ddgs:
                results = list(ddgs.text(query, max_results=max_results))
                
            if not results:
                return f"No results found for: {query}"
            
            # Format results
            formatted_results = f"Search results for '{query}':\n\n"
            for i, result in enumerate(results, 1):
                title = result.get('title', 'No title')
                snippet = result.get('body', 'No description')
                url = result.get('href', 'No URL')
                
                formatted_results += f"{i}. {title}\n"
                formatted_results += f"   {snippet}\n"
                formatted_results += f"   URL: {url}\n\n"
            
            return formatted_results.strip()
            
        except Exception as e:
            return f"Error searching web: {e}"
