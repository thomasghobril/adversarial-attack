# Some ideas for the task of finding adversarial datapoints

> For Property 1, we could use a FGSM method but with a gradient calculated with respect to the
COC score. We want to maximize the score of COC with the hope that it will get greater than 1500
in the search zone defined by the input constraints.

> For Property 2, same idea and we hope that the COC score will get greater than the others.
