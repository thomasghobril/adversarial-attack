# DeepSafe: A Data-driven Approach for Checking Adversarial Robustness in Neural Networks

> Use an approach based on data to evaluate the robustness of a NN.
The work aims to determine input areas where all the points are mapped to the same label.

## The method DeepSafe

> To do that, they use correctly classified points (train/test points) and apply Kmeans on them.
As Kmeans is an unsupervised clustering technique, they execute it with K=nb of possible labels and
hope that Kmeans will identify cluster of points that are mapped to the same label by the NN.
Apparently they achieve to do that. 

> Therefore, they now have clusters of points, each one of them corresponding to a specific
output label of the NN. They also consider the centroid xk of each cluster and rk a typical radius
for each cluster.
Then, for each cluster, they define a zone Sk by the sphere centered on xk with radius rk.
They want to check it that zone is safe or not <=> all the points in that zone will be given label k
by the NN. They use Reluplex to do that. 

> They also want to know if there exists any point in the sphere Sk which is mapped to a label j!=k.
If it's not the case, then Sk is safe against j-targeted attacks. Let's note that Sk is a safe zone
iff Sk is safe for all j-targeted attacks for j!=k.

## For our project ?

> DeepSafe uses datapoints. We don't have datapoints (unless we generate them).

> DeepSafe is used on ACAS-Xu but doesn't care about properties. And properties is what we have to check !

> So don't very useful but gives ideas.