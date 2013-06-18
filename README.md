Answers for the 3 question :

Selection Sort:

in condition where we've sorted array and we want to add one more array (maybe sorted or not sorted) and den to get a 
complete sort of both, Selecton sort is going to start the procedure all from the first. we cant pull out the extra
benifit of having already sorted array here, thus selection sort is considered to be less adaptive in both the cases
i.e when coming array is sorted and when coming array is unsorted

and I belive the third question where user gives the input as and when he is ready, turns out to be one of the above 
situation......so we can say selection sort treats any input to be the new problem, and thus not helpful in our 
condition where we have a set of already sorted array.

Bubble Sort:

bubble sort again treats its input as a new problem when each time it is given with some inputs. thus as it is even 
bubble sort doesnt use the already sorted array (it will certainly minimize the swaps but not the iterations) 
but with the minute change in the bubble sort, it mite work very well for question 1 and fairly good to question 2
the change thats required is, " When any particular iteration ends up with no swap, we should terminate the procedure "
but it is bit dependednt on the input but i think better than selection sort

Insertion sort:

I would recomend this algorithm just for.. this method will certainly use the benifit of having already sorted array.
we can start our iteration index from the newly coming array(may be sorted or unsorted or by the user) comparing with 
already soted array, this is adaptive according to me


Question is in the description of first commit





