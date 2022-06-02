# #==== AI ROBUSTNESS AGAINST ADVERSARIAL ATTACKS ====#
#### --------------------------------------------------- Neural Network compression of ACAS-Xu ----------------------------------------------------
					    	  AI project at CentraleSupélec - June 2022


## The project :
> This README gives an insight of the files (mainly jupyter notebooks) composing this S8 
> project which studies the robustness of ACAS-Xu neural networks. This work can be found
> on GitHub using the following link : https://github.com/thomasghobril/adversarial-attack


## Authors : 
> - Tom LABIAUSSE
> - Thomas GHOBRIL
> - Pierre OLLIVIER
> - Vincent MICHELANGELI
> - Shruthi SUNDARANAND


## Requirements :
> - numpy : 1.19.5
> - pandas : 1.0.5
> - seaborn : 0.11.2
> - sklearn : 0.23.1
> - matplotlib : 3.2.2
> - tensorflow : 2.4.1
> - art : 1.9.1
> - gurobipy : 9.5.0


## Jupyter notebooks :

> **network_analysis.ipynb**
> - Analyses the similarities between networks based on the repartition of the predicted labels
> on a set of random points in the inputs domain. 
> - Gives a method to construct clusters and 
> reduces the study from 45 networks to 9 clusters, each of them having specific properties.

> **confusion_matrix_analysis.ipynb**
> - Analyses the behaviour of the networks in each clusters by arbitrary choosing a neural net
> in each cluster.
> - Computes a confusion matrix for a given set of {network, points, attack}.
> - Gives graphic tools to visualize the evolution of confusion matrixes when increasing the
> intensity of a given attack on a network.
> - Provides global trends concerning the switch of
> predicted labels that can almost always be observed when attacking a network.

> **adv_pts_displacement_analysis.ipynb**
> - Analyses the evolution of the points before and after the attacks.
> - Gives graphical representations of how the coordinates change.
> - Also allows to change the intensity of the attacks.

> **robustness_metric_analysis.ipynb**
> - Analyses the robustness of ACAS-Xu networks from a statistical point of view,
> independently of the attacks, using linear optimization.




