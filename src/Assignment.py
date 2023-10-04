# CSP Assignment
# Original code by Håkon Måløy
# Updated by Xavier Sánchez Díaz

import copy
from itertools import product as prod


class CSP:
    def __init__(self):
        # self.variables is a list of the variable names in the CSP
        self.variables = []

        # self.domains is a dictionary of domains (lists)
        self.domains = {}

        # Log the number of times the backtrack function is called and the number of times it fails
        self.backtrack_attempts = 0
        self.failures = 0

        # self.constraints[i][j] is a list of legal value pairs for
        # the variable pair (i, j)
        self.constraints = {}

    def add_variable(self, name: str, domain: list):
        """Add a new variable to the CSP.

        Parameters
        ----------
        name : str
            The name of the variable to add
        domain : list
            A list of the legal values for the variable
        """
        self.variables.append(name)
        self.domains[name] = list(domain)
        self.constraints[name] = {}

    def get_all_possible_pairs(self, a: list, b: list) -> list[tuple]:
        """Get a list of all possible pairs (as tuples) of the values in
        lists 'a' and 'b', where the first component comes from list
        'a' and the second component comes from list 'b'.

        Parameters
        ----------
        a : list
            First list of values
        b : list
            Second list of values

        Returns
        -------
        list[tuple]
            List of tuples in the form (a, b)
        """
        return prod(a, b)

    def get_all_arcs(self) -> list[tuple]:
        """Get a list of all arcs/constraints that have been defined in
        the CSP.

        Returns
        -------
        list[tuple]
            A list of tuples in the form (i, j), which represent a
            constraint between variable `i` and `j`
        """
        return [(i, j) for i in self.constraints for j in self.constraints[i]]

    def get_all_neighboring_arcs(self, var: str) -> list[tuple]:
        """Get a list of all arcs/constraints going to/from variable 'var'.

        Parameters
        ----------
        var : str
            Name of the variable

        Returns
        -------
        list[tuple]
            A list of all arcs/constraints in which `var` is involved
        """
        return [(i, var) for i in self.constraints[var]]

    def add_constraint_one_way(self, i: str, j: str,
                               filter_function: callable):
        """Add a new constraint between variables 'i' and 'j'. Legal
        values are specified by supplying a function 'filter_function',
        that should return True for legal value pairs, and False for
        illegal value pairs.

        NB! This method only adds the constraint one way, from i -> j.
        You must ensure to call the function the other way around, in
        order to add the constraint the from j -> i, as all constraints
        are supposed to be two-way connections!

        Parameters
        ----------
        i : str
            Name of the first variable
        j : str
            Name of the second variable
        filter_function : callable
            A callable (function name) that needs to return a boolean.
            This will filter value pairs which pass the condition and
            keep away those that don't pass your filter.
        """
        if j not in self.constraints[i]:
            # First, get a list of all possible pairs of values
            # between variables i and j
            self.constraints[i][j] = self.get_all_possible_pairs(
                self.domains[i], self.domains[j])

        # Next, filter this list of value pairs through the function
        # 'filter_function', so that only the legal value pairs remain
        self.constraints[i][j] = list(filter(lambda
                                             value_pair:
                                             filter_function(*value_pair),
                                             self.constraints[i][j]))

    def add_all_different_constraint(self, var_list: list):
        """Add an Alldiff constraint between all of the variables in the
        list provided.

        Parameters
        ----------
        var_list : list
            A list of variable names
        """
        for (i, j) in self.get_all_possible_pairs(var_list, var_list):
            if i != j:
                self.add_constraint_one_way(i, j, lambda x, y: x != y)

    def backtracking_search(self):
        """This functions starts the CSP solver and returns the found
        solution.
        """
        # Make a so-called "deep copy" of the dictionary containing the
        # domains of the CSP variables. The deep copy is required to
        # ensure that any changes made to 'assignment' does not have any
        # side effects elsewhere.
        assignment = copy.deepcopy(self.domains)

        # Reset log
        self.backtrack_attempts = 0
        self.failures = 0

        # Run AC-3 on all constraints in the CSP, to weed out all of the
        # values that are not arc-consistent to begin with
        self.inference(assignment, self.get_all_arcs())

        # Call backtrack with the partial assignment 'assignment'
        return self.backtrack(assignment)

    def backtrack(self, assignment):
        """The function 'Backtrack' from the pseudocode in the
        textbook.

        The function is called recursively, with a partial assignment of
        values 'assignment'. 'assignment' is a dictionary that contains
        a list of all legal values for the variables that have *not* yet
        been decided, and a list of only a single value for the
        variables that *have* been decided.

        When all of the variables in 'assignment' have lists of length
        one, i.e. when all variables have been assigned a value, the
        function should return 'assignment'. Otherwise, the search
        should continue. When the function 'inference' is called to run
        the AC-3 algorithm, the lists of legal values in 'assignment'
        should get reduced as AC-3 discovers illegal values.

        IMPORTANT: For every iteration of the for-loop in the
        pseudocode, you need to make a deep copy of 'assignment' into a
        new variable before changing it. Every iteration of the for-loop
        should have a clean slate and not see any traces of the old
        assignments and inferences that took place in previous
        iterations of the loop.
        """
        # TODO: YOUR CODE HERE
        # Log the number of times the backtrack function is called
        self.backtrack_attempts += 1

        working_assignment = copy.deepcopy(assignment)
        # Check if assignment is complete
        if all(len(working_assignment[variable]) == 1 for variable in working_assignment):
            print("Found solution!")
            return working_assignment

        variable: str = self.select_unassigned_variable(assignment)
        
        for value in self.order_domain_values(variable, assignment):
            # Try to assign the value to the variable
            working_assignment[variable] = [value]

            # Find all arcs that are neighbors of the variable and check if they are arc consistent by pruning their space
            queue = self.get_all_neighboring_arcs(variable)

            # Prune the domain of the neighbors of the variable, as inference mutates the assignment we need to make a copy
            pruned_working_assignment = copy.deepcopy(working_assignment)
            do_imply = self.inference(pruned_working_assignment, queue)

            if do_imply:
                # The assignment is arc consistent, so continue with the next variable
                result: bool = self.backtrack(pruned_working_assignment)
                if result:
                    return result

        # No solution found
        self.failures += 1
        return False

    def select_unassigned_variable(self, assignment: dict) -> str:
        """The function 'Select-Unassigned-Variable' from the defenition
        in the textbook (5.3.1). Should return the name of one of the variables
        in 'assignment' that have not yet been decided, i.e. whose list
        of legal values has a length greater than one.
        """
        variable: str
        for variable in assignment.keys():
            variables_constraint = assignment[variable]
            if len(variables_constraint) > 1:
                return variable

    def order_domain_values(self, variable: str, assignment: dict) -> list:
        """Order the domain values of the variable in the assignment using the minimum remaining values heuristic."""
        domain = assignment[variable]
        
        domain.sort(key=lambda x: len(x))
        return domain

    def inference(self, assignment, queue) -> bool:
        """The function 'AC-3' from the pseudocode in the textbook.
        'assignment' is the current partial assignment, that contains
        the lists of legal values for each undecided variable. 'queue'
        is the initial queue of arcs that should be visited.

        Returns false if an inconsistency is found,
        and returns true otherwise. 
        """
        # TODO: YOUR CODE HERE
        while len(queue):
            x_i: str
            x_j: str
            x_j, x_i = queue.pop()

            if self.revise(assignment, x_i, x_j):
                # The domain of x_i has been reduced to only legal values.
                if len(assignment[x_i]) == 0:
                    return False
                # Add all arcs that are neighbors of x_i and not x_j
                for x_k in [arc for arc in self.get_all_neighboring_arcs(x_i) if x_j not in arc]:
                    queue.append(x_k)
        return True

    def revise(self, assignment, x_i: str, x_j: str) -> bool:
        """The function 'Revise' from the pseudocode in the textbook.
        'assignment' is the current partial assignment, that contains
        the lists of legal values for each undecided variable. 'i' and
        'j' specifies the arc that should be visited. If a value is
        found in variable i's domain that doesn't satisfy the constraint
        between i and j, the value should be deleted from i's list of
        legal values in 'assignment'.
        """
        # TODO: YOUR CODE HERE
        revised = False
        domain_i = copy.deepcopy(assignment[x_i])
        domain_j = assignment[x_j]

        for x in assignment[x_i]:
            found_one = False
            for y in domain_j:
                for constraint in self.constraints[x_i][x_j]:
                    if (x, y) == constraint:
                        found_one = True
            if not found_one:
                domain_i.remove(x)
                revised = True

        assignment[x_i] = domain_i
        return revised


def create_map_coloring_csp() -> CSP:
    """Instantiate a CSP representing the map coloring problem from the
    textbook. This can be useful for testing your CSP solver as you
    develop your code.
    """
    csp = CSP()
    states = ['WA', 'NT', 'Q', 'NSW', 'V', 'SA', 'T']
    edges = {'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
             'NT': ['WA', 'Q'], 'NSW': ['Q', 'V']}
    colors = ['red', 'green', 'blue']
    for state in states:
        csp.add_variable(state, colors)
    for state, other_states in edges.items():
        for other_state in other_states:
            csp.add_constraint_one_way(state, other_state, lambda i, j: i != j)
            csp.add_constraint_one_way(other_state, state, lambda i, j: i != j)
    return csp


if __name__ == "__main__":
    csp = create_map_coloring_csp()
    # print(csp.variables)
    # print(csp.get_all_arcs())
    # print(f"csp.constraints = {csp.constraints}")
    # print(f"csp.domains = {csp.domains}")
    # print(f"csp.variables = {csp.variables}")

    print(csp.backtracking_search())
    print(f"csp.constraints = {csp.constraints}")
    print(f"csp.domains = {csp.domains}")
    print(f"csp.variables = {csp.variables}")
