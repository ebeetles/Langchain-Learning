from typing import Dict, TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    name : str 


def compliment_node(state: AgentState) -> AgentState:
    """Simple node that compliments the user"""

    state['name'] = state["name"] + " you're doing an amazing job learning LangGraph!"

    return state 

graph = StateGraph(AgentState)

graph.add_node("compliment", compliment_node)

graph.set_entry_point("compliment")
graph.set_finish_point("compliment")

app = graph.compile()

from IPython.display import Image, display
display(Image(app.get_graph().draw_mermaid_png()))