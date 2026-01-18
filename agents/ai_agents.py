from langgraph.prebuilt import create_react_agent
from langchain.agents import create_agent
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from agents.tools import get_tools
from agents.llm_provider import get_llm

def get_response_from_ai_agent(llm_id, query, web_search_allowed, system_prompt, provider):
    print("in get_response_from_ai_agent")
    llm = get_llm(provider, llm_id)
    tools = get_tools(web_search_allowed)
    query = (query or "").strip()
    if not query:
        return "Please enter a message."

    agent = create_react_agent(model=llm, tools=tools)

    #conversation history
    state =  {
        "messages" : [
            SystemMessage(content= system_prompt),
            HumanMessage(content= query),

        ]
    }

    print("before state")
    print("STATE:", state)
    print("STATE messages len:", len(state["messages"]))
    response = agent.invoke(state)
    message = response.get("messages", [])
    ai_message = [msg.content for msg in message if isinstance(msg, AIMessage)]
    return ai_message[-1] if ai_message else "got no response"





