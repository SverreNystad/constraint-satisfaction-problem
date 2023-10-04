import pytest
from src.constraint_satisfaction_problem import CSP  
from src.map_coloring_util import create_map_coloring_csp  

def test_inference_for_no_assignment():
    csp = CSP()
    # Add variables, domains, and constraints
    
    assignment = {}  # Add a partial assignment
    arcs = []  # Add some arcs
    
    consistent = csp.inference(assignment, arcs)
    
    assert consistent  # or not, depending on your test case
    assert assignment == {}  # Replace with expected output


def test_revise_map_coloring():
    csp = create_map_coloring_csp()
    assignment = {state: ["red", "green", "blue"] for state in csp.variables}
    
    # Forcing a revision by making "SA" and "WA" both have "red"
    assignment["SA"] = ["red"]
    revised = csp.revise(assignment, "WA", "SA")
    
    assert revised
    assert assignment["WA"] == ["green", "blue"]

