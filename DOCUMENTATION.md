# Report for assignment 3

This is a template for your report. You are free to modify it as needed.
It is not required to use markdown for your report either, but the report
has to be delivered in a standard, cross-platform format.

## Project

Name: Algorithms
URL: https://github.com/keon/algorithms
Description: A python library containing minimal examples of algorithm and datastructure implementations.

## Onboarding experience

### 1. How easily can you build the project? Briefly describe if everything worked as documented or not:

#### (a) Did you have to install a lot of additional tools to build the software?

No additional tools were required to build the project. As it is a python project it did not need to be built, either.

#### (b) Were those tools well documented?

As there were no tools, no documentation was necessary.

#### (c) Were other components installed automatically by the build script?

The testing components were added in a requirements.txt file, and thus installed automatically.

#### (d) Did the build conclude automatically without errors?

Yes. The project built without any errors.

#### (e) How well do examples and tests run on your system(s)?

The tests ran without errors.

#### Summary

The project was easy to get started and running. No extra components or tools were necessary to run the program, and the components necessary for the tests were listed in a requirements.txt file. While the versions of each tool was not added to the requirements.txt file, it was not necessary in this case either as no errors were encountered. Had errors been encountered, however, it would be preferable to have the version numbers in case.

# Glossary:

*NLOC* : Number of Lines of Code
*CC* : Cyclomatic Complexity

## Complexity

1. What are your results for ten complex functions?
   * Did all methods (tools vs. manual count) get the same result?

   The results for each function is presented as follows:

   ### Cyclomatic Complexities:

   #### Strip_URL_Params:

   algorithms/algorithms/strings/strip_url_params.py
   strip_url_params1@14-68@

   CC = 20
   NLOC = 50

   #### Intersection:

   algorithms/algorithms/linkedlist/intersection.py
   intersection@21-64@

   CC = 14
   NLOC = 31
   **CC_Manual = 14**

   #### maximum_flow_bfs

   algorithms/graph/maximum_flow_bfs.py
   maximum_flow_bfs@28-84@

   CC = 10
   NLOC = 55
   #### maximum_flow_dfs

   algorithms/graph/maximum_flow_dfs.py
   maximum_flow_dfs@27-83@

   CC = 10
   NLOC = 55
   **CC_Manual = 10**

   #### three_sum

   ./algorithms/array/three_sum.py
   three_sum@18-48@

   CC = 11
   NLOC = 30
   #### Text_justification

   ./algorithms/strings/text_justification.py
   text_justification@34-89@ Count by hand = 13

   CC = 13
   NLOC = 55
   **CC_Manual = 13**

   #### multiply:

   algorithms/algorithms/matrix/sparse_mul.py:
   multiply@71-99@

   CC = 18
   NLOC = 24
   **CC_manual = 16**

   #### delete_fixup:

   algorithms/algorithms/tree/red_black_tree/red_black_tree.py:
   delete_fixup@209-267@

   CC = 14
   NLOC = 31

   ### count_islands:

   ./algorithms/bfs/count_islands.py
   count_islands@40-65@

   CC = 14
   NLOC = 25
   **CC_Manual = 14**

   ### pacific_atlantic:

   ./algorithms/dfs/pacific_atlantic.py
   pacific_atlantic@32-54@

   CC = 14
   NLOC = 22

   * Are the results clear?

   The results are mostly clear, bar one function which did not return the same cyclomatic complexity as the *Lizard* tool. Every other function returned the same result during the manual count as well as the automatic count. While we are not entirely certain as to why, we did perform certain experiments to assess how Lizard calculates the cyclomatic complexity of the functions, but as the tool is not open we could not come to any conclusive results. We do speculate however, as the Lizard tool itself states in its documentation: "This tool actually calculates how complex the code ‘looks’ rather than how complex the code really ‘is’", there might be some discrepancies regarding functions of a higher complexity as those become more complex.

2. Are the functions just complex, or also long?

While the sample size of this assignment is small, there seems to be no correlation between the NLOC and the CC, which seems to be a popular trend within Python in general. It appears to have more to do with the overall function of the code rather than its complexity, as it almost appears to be an inverse relation for the functions that we have picked. While the most complex function also has the most NLOC, this appears to just be a coincidense.

3. What is the purpose of the functions?

   #### Strip_URL_Params:

   The function takes a URL with a parameter string as an input, it then looks for duplicate parameters and removes them. One can also provide an array of parameters one would like to strip, and the functions removes any instance of those parameters within the URL.

   #### Intersection:

   The function takes two linked lists and checks if they share a node. If the nodes are shared (not node values) the function returns the first shared node in question.

   #### maximum_flow_bfs

   The function takes an m x n matrix of non-negative integers representing the height of each unit cell in a continent and return the position with parameters.

   #### maximum_flow_dfs

   Calculates the maximum flow through a graph given an adjencency list using depth for search.
   #### three_sum

   In a list of integers, find a set of three distinct integers that adds up to 0.
   #### Text_justification

   Formats a string to have a specified amount of characters on each line and evenly distributes the spaces without cutting words in two.

   #### multiply:

   Calculates the maximum flow through a graph given an adjencency list using depth for search.

   #### delete_fixup:

   This function takes a node from a red black tree. The purpose of this function is handling the rotation of a red black tree after deleting some node in the tree.

   ### count_islands:

   The function takes a 2D-array and counts the number of islands. If 1 (lands) are surrounded by 0 (water), it will be counted as an island.

   ### pacific_atlantic:

   The function takes an m x n matrix of non-negative integers representing the height of each unit cell in a continent and return the position with parameters.


4. Are exceptions taken into account in the given measurements?

During the manual count we took exceptions into account, however, most of the functions did not make use of exceptions. We did some experimenting with regards to exceptions for the Lizard tool, and we arrived at the conclusion that it seems that the Lizard tool regards exceptions as return statements, that is they were disregarded.

5. Is the documentation clear w.r.t. all the possible outcomes?

The documentation is very bare-bones, barely describing the functionality of each function, and when the functions are described barely one of the cases (always a working case) are described. We thus found the documentation to be extremely lacking in general. The documentation does not appear to follow any conventions or standards for documentations either, except using the Python Docstring denominator.

## Refactoring

During the refactoring step each member looked over the code in order to identify a list of key elements within their function. These key elements could be something similar to: similar pieces of code, unecessary branching or pieces of code that could be separated into smaller modules.

For each of these elements steps were taken to refactor the code in order to reduce the cyclomatic complecity of the function. This proved to be possible for some of the functions, but not for others. In the cases where it was not possible it was explained why.

1. If pieces of code were similar, the code snippets were made into their own function which repeatedly called at the appropriate points of the code.
2. If the code branched unecessarily (for example an extra if-statement) the unecessary branch was pruned in order to reduce the complexity.
3. If one could separate the function into smaller modules, the code was separated into these modules.

The most occurring refactoring was done through splitting the code into these smaller modules. As we did this for each function the results per refactoring were as follows:

1. intersection.py: Original: 14CCN, Refactored: 9CCN (According to Lizard). https://github.com/oscarzhpersson/algorithms/blob/Issue%236_opers/Issue%20%236/reducedComplexity.py

2. maze_search.py: Original: 13CCN, Refactored: 8CCN (According to Lizard). https://github.com/oscarzhpersson/algorithms/blob/Issue%236_jansen/Issue%20%236/refactored_maze_search.py

3. text_justification.py Original: 13CCN, Refactured: 2CCN (According to Lizard). https://github.com/oscarzhpersson/algorithms/blob/Issue%236_timjonss/algorithms/strings/text_justification_refactored.py

4. sort_matrix_diagonally.py: Original: 10CCN, Refactored: 5CCN (According to Lizard). https://github.com/oscarzhpersson/algorithms/blob/Issue%236_wsod/algorithms/matrix/sort_matrix_diagonally.py

The only function which could not be was the function **maximum_flow_bfs.py**. The reason identified for this is as follows.

By doing some tests for this algorithm the conclusion is that this specific algorihm cannot be refactored without large structural change to the entire function
The reason that this cannot be restructured is just by the way the entire function is set up. At line 33 there is a while loop that runs until there is no path not
covered and then it breaks from that loop, it ties together and makes the BFS search and maximum flow tied together. By doing so there is no simple way for the function to be refactored into smaller functions which would help the CC of this function. To summarise the function works atomically per loop-step.

The most prominent impact of this is of course the lower cyclomatic complexity. But as the most used method of refactoring was splitting it into smaller functions, this may make the code more difficult to read or comprehent at first glance, as not everything is as cohesive anymore.

## Coverage

### Tools

The tool used to evaluate coverage was coverage.py. coverage.py was easy to implement as it worked as a standalone tool, where one only needed to give it the files one wanted to evaluate and it would run. While the tool was well documented and for the most part, easy to set up, inconsistencies within the chosen repository made the tests difficult to run. Some of the functions had their tests within the unit test folder, while others ran them within the file itself; the latter proving troublesome for coverage.py. The tool worked well for most members however.

### Your own coverage tool

1. What is the quality of your own coverage measurement? Does it take into account ternary operators (condition ? yes : no) and exceptions, if available in your language?

It takes into account every ternary operator and exception it encounters. Each coverage measurement is tailored to the specific function chosen.

2. What are the limitations of your tool? How would the instrumentation change if you modify the program?

Since the tools are tailored towards the functions, they would need to be modified if the code of the function in question would be changed, since branches could increase or decrease.

3. If you have an automated tool, are your results consistent with the ones produced by existing tool(s)?

The results of our manual branch coverage matched the results from the automated coverage tool we used, which was coverage.py.

The links to each branch for each changed coverage tool is as follows:

1. intersection.py: https://github.com/oscarzhpersson/algorithms/blob/Issue%234_opers/Issue%20%234/coverage.py

2. maximum_flow_bfs.py: https://github.com/oscarzhpersson/algorithms/blob/Issue%234_Mustali/algorithms/graph/maximum_flow_bfs.py

3. maze_search.py: https://github.com/oscarzhpersson/algorithms/blob/Issue%234_jansen/Issue%234/manual_tool_test.py

4. text_justification.py: https://github.com/oscarzhpersson/algorithms/blob/Issue%234_timjonss/algorithms/strings/text_justification.py

5. sort_matrix_diagonally.py: https://github.com/oscarzhpersson/algorithms/blob/Issue%234_wsod/algorithms/matrix/sort_matrix_diagonally.py

The coverage tool sets flags within a boolean array. These flags are manually placed within the code and thus supports each step of the code that we desire. We decided to use the constructs specified by us using the metrics from the course: if statements, else statements, exceptions, loops, etc.

The accuracy of the tool is measured by checking the flags and are compared using the tool coverage.py
### Evaluation

1. How detailed is your coverage measurement?

The coverage measurement is static and only measured step-wise by checking which branches an execution will take using the tests. The flags are persistent between runs, so one can always check the total tally after a run with the custom tools.

2. What are the limitations of your own tool?

The limitation of the tool are dependent on the creator of the tool. If a flag was missed the tool will not take it into account. The tool is also tailored specifically to the function itself, and can not be moved anywhere else afterwards.

3. Are the results of your tool consistent with existing coverage tools?

The results on the tools were consistent with the tool we used to check externally, coverage.py. There was one instance however where the tool could not be run, for the function intersection.py. In that case it was counted manually again. The reason for this was because of how its tests were set up internally, which differed. The repository we picked seemed to suffer from inconsistencies of its users when they are contributing.

## Coverage improvement

### intersection.py:

Comments that needed to change:

The test did not check the flag "**flags["flag8-while"]**". This flag is enabled if one list is longer than the other, which the test does not examine.

The test did not check the flag "**flags["flag6"]**". This flag is enabled if one list has elements still, while the other one does not.

Report of old coverage: https://github.com/oscarzhpersson/algorithms/blob/Issue%235_opers/Issue%20%234/coverage_Original.py **9/11 flags**
Report of new coverage: https://github.com/oscarzhpersson/algorithms/blob/Issue%235_opers/Issue%20%235/coverage.py **11/11 flags**

Two test cases were added for these within the report of new coverage as unit tests: **test_Fixed_Flag8** and **test_Fixed_Flag6**.
### text_justification.py
The tests did not check flag 3, this part of the code should throw an exception if a Word cannot be fit on a line. I added a test case which decreases the row length. 

The second test added increases the path coverage, as flag 10 and flag 11 was not both visited. This tests whether it can both justify lines with several Words and lines with only one Word.

Previous coverage: 10/11 flags
New coverage 11/11 flags.

git diff main:tests/test_strings.py tests/test_strings.py

### sort_matrix_diagonally.py:

Comments that needed to change:

The test did not check the flag "flags["0"]". This flag is enabled if there is only one row in the input matrix.

The test did not check the flag "flags["1"]". This flag is enabled if the first row has only one column.

If statement changed in new coverage:

The new coverage split the untested if statement into two if statements, creating the flags "flags["0"]" and "flags["1"]", in order to test the separetely.
This made it so that there could be two test written, testing the if statements separetely.

Report of old coverage: https://github.com/oscarzhpersson/algorithms/blob/Issue%234_wsod/algorithms/matrix/sort_matrix_diagonally.py **one if statement not tested**
Report of new coverage: https://github.com/oscarzhpersson/algorithms/blob/Issue%235_wsod/algorithms/matrix/sort_matrix_diagonally.py **if statement split into two, both now tested**

Two test cases were added for these within the report of new coverage as unit tests: test_sort_diagonally.

### maximum_flow_bfs.py

The function already had 100% coverage so there is not lots of parts that needs to be tested for this function. There also hard to create smaller test cases because of how the function is built. The function first needs a connected graph and and then find a path using BFS. If there is no path then the function will leave the function and no maxflow can be find. Therefore this function depends heavily on the first part. What was done is to test the first part seperatly where there is no connected graph and then a test function was already applied for finding the maximum flow.

Instead there are other test cases were added for other functions that were not covered. New testcases were added to for the function delete_node in algorithms/algorithms/tree/bst/delete_node.py. There are no coverage for this function before and after most of the functions were covered.

Flags before for the function maximum_flow_bfs: 10/10
Flags after: 10/10

Flags before - delete_node.py: 0/7
Flags after - delete_node.py 7/7

### maze_search.py

The tests have a total of 6 flags, indicated in bfs.maze_search.py

The test did not check the flag 0, which is the first flag that checks if the initial_x & initial_y are 0.

Report of old coverage: https://github.com/oscarzhpersson/algorithms/blob/5ee39468c9c529f5578aa432ea3af0a15f99ae1e/Issue%235/original_coverage.py 5/6 flags.
Report of new coverage: https://github.com/oscarzhpersson/algorithms/blob/5ee39468c9c529f5578aa432ea3af0a15f99ae1e/Issue%235/coverage.py 6/6 flags.

The additional tests tested the flag 0 as it is seen to be iterated and reaches 100% coverage.

Show the comments that describe the requirements for the coverage.
Report of old coverage: [link]
Report of new coverage: [link]
Test cases added:
git diff ...
Number of test cases added: two per team member (P) or at least four (P+).

## Self-assessment: Way of working

Using the Essence Standards Checklist for Way-of-Working we have established that we are in the state In-Place. We have evaluated ourselves to still remain in the same state as previously. While we are more coherent as a group in general, and while we still follow the previously established ways of working no further progress was made in regards to the Essence standard because of the individual nature of this particular assignment. We still collaborate well, but we decided (as the assignment states) to individually progress then summarize in a group.

The self-assessment was written as a group, by the group. While we have not improved with regards to the essence steps we would like to add that we are closer to the next step than before. We just deem that the individual nature of the assignment prevents us from claiming to be one step further.

The largest step to progress to the step "working well" would be that the practices are naturally applied, as we still have to remind members occasionally.
## Overall experience

We learnt how to make use of coverage and how to implement it into the workflow in order to write well tested and testable code. We also learnt how to manually evaluate the coverage but also how to use tools which extracts the coverage from functions.

We agree that this could be done for any project henceforth, in order to make sure the entire program is tested. We also learnt how to minimise the cyclomatic complexity when writing code, and how to think with regards to this.

We also learnt the important for consistency when contributing to open source projects.