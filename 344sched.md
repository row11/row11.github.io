| Date | Topic | Lecture Notes| Suggested Reading |
|-------|--------|--------|------ |
| {{ dates | first | date: "%b %d" }} {% assign dates = dates | shift %}     | Course Overview and Basics Review | | [Handout on Big-O notation and recurrences from Anupam Gupta](https://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15750-s21/www/handouts/recurrences-and-big-oh.pdf), [Chapter 0](https://jeffe.cs.illinois.edu/teaching/algorithms/book/00-intro.pdf) of Algorithms by Jeff Erickson
| **Divide and Conquer** |
| {{ dates | first | date: "%b %d" }} {% assign dates = dates | shift %}     | Proof by Induction, Recursion, Tower of Hanoi, Divide and Conquer, Mergesort | | [Appendix I](https://jeffe.cs.illinois.edu/teaching/algorithms/notes/98-induction.pdf), [Chapter 1](https://jeffe.cs.illinois.edu/teaching/algorithms/book/01-recursion.pdf) of Algorithms by Jeff Erickson
| {{ dates | first | date: "%b %d" }} {% assign dates = dates | shift %}     | Karatsuba Multiplication, Master Theorem | |
| {{ dates | first | date: "%b %d" }} {% assign dates = dates | shift %}     | Strassen's Algorithm, the word-RAM model, Median of Medians | | [Handout about the word-RAM](https://bowaggoner.com/courses/gradalg/notes/lect01-intro.pdf) model by Bo Waggoner, [Notes about word-RAM](https://introtcs.org/public/lec_07_other_models.html) (and models of computation more generally) by Boaz Barak, [Chapter 3.4](https://cs.brown.edu/people/jsavage/book/pdfs/ModelsOfComputation.pdf) of John Savage's textbook gives a fully formal description.
| **Dynamic Programming** |
| {{ dates | first | date: "%b %d" }} {% assign dates = dates | shift %}     | Fibonacci, 0/1 Knapsack, Longest Increasing Subsequence| | [Chapter 3](https://jeffe.cs.illinois.edu/teaching/algorithms/book/03-dynprog.pdf) of Algorithms by Jeff Erickson.
| {{ dates | first | date: "%b %d" }} {% assign dates = dates | shift %}     | Edit Distance | |
| {{ dates | first | date: "%b %d" }} {% assign dates = dates | shift %}     | Optimal BST, 1d K-clustering | |
| **Greedy Algorithms** |
| {{ dates | first | date: "%b %d" }} {% assign dates = dates | shift %}     | Wrap-up 1d K-clustering, Interval Scheduling | | [Chapter 4](https://jeffe.cs.illinois.edu/teaching/algorithms/book/04-greedy.pdf) of Algorithms by Jeff Erickson.
| {{ dates | first | date: "%b %d" }} {% assign dates = dates | shift %}     | Fractional Knapsack, Huffman Coding | | [Notes on fractional knapsack](https://courses.cs.duke.edu/compsci330/spring19/lecture8scribe.pdf) from Rong Ge's class
| **Graph Algorithms** |
| {{ dates | first | date: "%b %d" }} {% assign dates = dates | shift %}     | Wrapup Huffman Coding, Intro to Graphs | | [Chapter 5](https://jeffe.cs.illinois.edu/teaching/algorithms/book/05-graphs.pdf) and [Chapter 6](https://jeffe.cs.illinois.edu/teaching/algorithms/book/06-dfs.pdf) of Algorithms by Jeff Erickson
| {{ dates | first | date: "%b %d" }} {% assign dates = dates | shift %}     | BFS, Shortest Paths, DFS, Topological Sort | |
| {{ dates | first | date: "%b %d" }} {% assign dates = dates | shift %}     | Strongly Connected Components | |
| **Data Structures and Amortized Analysis** |
| {{ dates | first | date: "%b %d" }} {% assign dates = dates | shift %}     | Dijkstra's Algorithm | | [Chapter 8](https://jeffe.cs.illinois.edu/teaching/algorithms/book/08-sssp.pdf) of Algorithms by Jeff Erickson. Advanced reading: Kevin Wayne's slides on [binary & binomial heaps](https://www.cs.princeton.edu/~wayne/kleinberg-tardos/pdf/BinomialHeaps.pdf) and on [Fibonacci heaps](https://www.cs.princeton.edu/~wayne/kleinberg-tardos/pdf/FibonacciHeaps.pdf) |
| {{ dates | first | date: "%b %d" }} {% assign dates = dates | shift %}     | Bellman-Ford, Floyd-Warshall, Amortized Analysis | | [Chapter 9](https://jeffe.cs.illinois.edu/teaching/algorithms/book/09-apsp.pdf) of Algorithms by Jeff Erickson.
| {{ dates | first | date: "%b %d" }} {% assign dates = dates | shift %}     | MIDTERM | | 
| {{ dates | first | date: "%b %d" }} {% assign dates = dates | shift %}     | **Spring Break, No Class** | 
| {{ dates | first | date: "%b %d" }} {% assign dates = dates | shift %}     | **Spring Break, No Class** | 
| {{ dates | first | date: "%b %d" }} {% assign dates = dates | shift %}     | Amortized Analysis | |  [Director's Cut, Chapter 9](https://jeffe.cs.illinois.edu/teaching/algorithms/notes/09-amortize.pdf) of Algorithms by Jeff Erickson
| {{ dates | first | date: "%b %d" }} {% assign dates = dates | shift %}     | Minimum Spanning Trees and Union Find| |  [Chapter 7](https://jeffe.cs.illinois.edu/teaching/algorithms/book/07-mst.pdf) of Algorithms by Jeff Erickson
| **Randomized Algorithms** |
| {{ dates | first | date: "%b %d" }} {% assign dates = dates | shift %}     | Probability Review, Quicksort| | [Director's Cut, Chapter 1](https://jeffe.cs.illinois.edu/teaching/algorithms/notes/01-random.pdf) and [Chapter 2](https://jeffe.cs.illinois.edu/teaching/algorithms/notes/02-nutsbolts.pdf) of Algorithms by Jeff Erickson
| {{ dates | first | date: "%b %d" }} {% assign dates = dates | shift %}     | Hashing | | [Director's Cut, Chapter 5](https://jeffe.cs.illinois.edu/teaching/algorithms/notes/05-hashing.pdf) of Algorithms by Jeff Erickson 
| {{ dates | first | date: "%b %d" }} {% assign dates = dates | shift %}     | Hashing Wrap-up, Balls and Bins | |
| **Linear Programming and Optimization** |
| {{ dates | first | date: "%b %d" }} {% assign dates = dates | shift %}     | Flows and Matchings | | [Chapter 10](https://jeffe.cs.illinois.edu/teaching/algorithms/book/10-maxflow.pdf) of Algorithms by Jeff Erickson 
| {{ dates | first | date: "%b %d" }} {% assign dates = dates | shift %}     | Ford Fulkerson | |
| {{ dates | first | date: "%b %d" }} {% assign dates = dates | shift %}     | Linear Programming, Modeling, Intuition behind algorithms | | [Chapter H](https://jeffe.cs.illinois.edu/teaching/algorithms/notes/H-lp.pdf) of Algorithms by Jeff Erickson
| {{ dates | first | date: "%b %d" }} {% assign dates = dates | shift %}     | Polytopes and Integrality | |
| **Limits of Computation** |
| {{ dates | first | date: "%b %d" }} {% assign dates = dates | shift %}     | Limits of Computation and the Complexity Hierarchy | | [Chapter 12](https://jeffe.cs.illinois.edu/teaching/algorithms/book/12-nphard.pdf) of Algorithms by Jeff Erickson
| {{ dates | first | date: "%b %d" }} {% assign dates = dates | shift %}     | NP-Completeness, Cook-Levin Theorem, Reductions | |
| {{ dates | first | date: "%b %d" }} {% assign dates = dates | shift %}     | More Reductions | |
| **Advanced Topics** |
| {{ dates | first | date: "%b %d" }} {% assign dates = dates | shift %}     | Wrap-up Complexity, Review | |  
| {{ dates | first | date: "%b %d" }} {% assign dates = dates | shift %}     | FINAL | |  