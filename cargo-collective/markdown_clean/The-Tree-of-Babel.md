# The Tree of Babel

 _**[Blog](https://youjin.io/Thesis)**_  

## [Project Website](http://treebabel.herokuapp.com/)

  
  
  

![](images/The-Tree-of-Babel/ezgif.com-optimize.gif)

  

## Concept  

The project goal is understanding and generating interactive narrative
structures using Machine Learning models.  
This project is inspired by the idea of [Standard Patterns in Choice-Based
Games](https://heterogenoustasks.wordpress.com/2015/01/26/standard-patterns-
in-choice-based-games/), that analyzing interactive narrative structures of
games as graph and design pattern.  
The dataset is customized for ML libraries and scraped from
[TransverseReadingGallery](https://jeremydouglass.github.io/transverse-
gallery/).  
  
Basic concept:  

     1. Convert graphs to feature matrix of vector embeddings*.  

     2. Categorize graphs by clustering algorithms.  

     3. Generate new graphs from categories using autoencoder.  

  
Used libraries and ML models:  

    * [NetworkX](https://networkx.github.io/): graph properties (width, length, clustering, degree, cycle)
    * [graph2vec](https://github.com/benedekrozemberczki/graph2vec): extracting feature matrix
    * [scikit-learn](https://scikit-learn.org/stable/modules/clustering.html#clustering): K-means, Spectral, Agglomerative, Mean Shift Clustering
    * [PyTorch geometric](https://rusty1s.github.io/pytorch_geometric/build/html/modules/nn.html#torch_geometric.nn.models.GAE): Autoencoder

  
*An embedding is a relatively low-dimensional space into which you can translate high-dimensional vectors. Embeddings make it easier to do machine learning on large inputs like sparse vectors representing words. Ideally, an embedding captures some of the semantics of the input by placing semantically similar inputs close together in the embedding space. An embedding can be learned and reused across models. (Google Developers Machine Learning Course)   
  

## Classification  

The clustering of graphs from their feature matrix looks like below.  
I have tried to use different algorithms to classify them automatically, but I
could not find significant differences between groups when I checked the
properties of graphs.  
When I look at the image of clustering visualization, it looks like rather the
problem of way of vector embedding than clustering algorithms themselves.  
Since the X coordinate just represents the index of graph orders, significant
values are Y coordinates only.  
To fix this problem, I need to try with the array of feature matrixes of each
graph, rather than just a feature matrix of whole graphs.  

![](http://treebabel.herokuapp.com/static/img/cluster_wo.png)  

Instead of using computed categorization, I categorized graphs with names that
I made up. The names are inspired by graph properties.  
  

### Basic

They are basic directed graphs.  
  
Mostly have tree shapes.  
  
They look clean and straightforward.

### Broad

They have larger widths.  
  
Short playthrough, Strong replayability.

### Linear

This shape indicates  
the linearity of narrative structure.  
  
Easy control of drama. Immersive storytelling through long playtime.

  

### Merged

The graphs merge into certain points.  
  
Those points usually represent important events in a story.  

  

### Clustered

Grouped clusters of nodes make a modular structure.  
  
The groups of nodes could be detailed choices in a single situation.  
  
A tendency to be organized by geography.  
  
Fragmentary, episodic.  

  

### Cyclic

Reversibility. End nodes are redirected to early-stage nodes.  
  
Players can unlock new status while looping similar narratives.  
  
Commonly used for time loops or geo geographic travel.

According to the categorization, the dataset is classified by graph
properties.  
Each class is a group of graphs which have prominent values of graph
properties. (degree, average_clustering, cycle_basis, treewidth_min_degree,
all_pairs_shortest_path_length)  
  

## Further Steps

  * Labeling nodes with text: make semantic narratives  
Using similarity of document matrix of word embeddings and graph feature
matrix, assign sentences to node labels.

  * Better vector representation of graphs for categorization

  * Visual representation of the comparison of generated and original graphs  

  * Add json file download feature of generated graphs

  
  

New York, Spring 2019