from emergencyLanding import *

search_radius = 10

data_retrieval = EmergencyProblem()
data_retrieval.run_problem('AA221')

if len(data_retrieval.airports) == 0:
    print("\nYOU ARE GOING TO DIE GG")
    quit()
else:
    the_problem = Problem([data_retrieval.aircraft.latitude,data_retrieval.aircraft.longitude], data_retrieval.airports)
    Node = breadth_first_tree_search(the_problem)
    print("stop")
# problem_solving_agent = SimpleProblemSolvingAgentProgram([the_problem.aircraft.latitude, the_problem.aircraft.latitude])
