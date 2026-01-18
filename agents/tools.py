from langchain_community.tools.tavily_search import TavilySearchResults

def get_tools(enable:bool):
    if enable:
        return [TavilySearchResults(max_results = 2 )]
    else:
        return []