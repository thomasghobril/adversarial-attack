# Policy Compression for Aircraft Collision Avoidance Systems


## ACAS X and score tables

> A look-up table gives the action to take when facing a given set of inputs=states measured by the aircraft (angle/speed...)
Given a set of inputs, the table associates a score to each of the 5 possible outcomes (COC/WL/SL/WR/SR). The action to choose is the one maximizing the score.
However, states are continuous numbers (angle/speed...). Therefore, they are discretized and that's why we speak about table.
That discretization needs to be very thin to ensure good performances in the real world with many possible situations.
Therefore ACAS Xu table is extremely large (hundreds of GB of floating point storage) but one can downsample the table because many values are close to each others.
In fact, for many discrete states, the scores for the available actions are identical.
This process allows to reduce the table to approximately 2GB of floating point storage.
For ACAS Xu, we take into consideration horizontal and vertical moves, therefore there is even more data and previous techniques are not sufficient.


## Present 2 methods to compress look-up tables (= score tables)

> Origami folding
Uses the natural symmetry present in the tables to compress them in smaller tables

> Neural Networks
Find a robust non-linear function that approximates the tables. Instead of storing the table itself, only the parameters of the NN could be stored !
Choose fully-connected neural networks with ReLU activation functions. Choose the architecture given that gives around 600K parameters => that means that
the table could be compressed to occupy only a few MB.
However, with this method, there is no longer a guarantee that the optimal advisory remains the same given a set of inputs. In fact, for many of the states in
the score tablen the difference between the 1st and 2nd best advisories is relatively small. Therefore, need to choose a loss function that penalize the network
when it predicts the wrong advisory while still learning an accurate representation of the table.
Instead of origami method, NN takes directly the measured states as inputs. No need to discretize the values. Moreover, the NN often gives better results/advisories
then the original table and produces alerts earlier when used in a simulation. The ability to use continous inputs may explain these results.