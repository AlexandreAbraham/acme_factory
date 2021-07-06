# Benchmark on Covertype

|      Package     |                                       Model                                     |    ROC AUC    |   Accuracy    |
| ---------------- | -------------------------------------------------------------------------------:|:------------- |:------------- |
| scikit-learn     |                                                                    RandomForest | 0.991         | 0.905         |
| scikit-learn     |                                       [AdaboostClassifier](AdaboostClassifier/) | 0.822         | -             |
| scikit-garden    |             [MondrianForestClassifier](scikit-garden-MondrianForestClassifier/) | 0.983         | 0.899         |
| fylearn          |           [FuzzyReductionRuleClassifier](fylearn-FuzzyReductionRuleClassifier/) | -             | 0.659         |
| node (pytorch)   |                                               [NodeClassifier](NodeClassifier/) | 0.956         | 0.830         |
| lightning        |                                       [CDClassifier](scikit-contrib-lightning/) | -             | 0.815         |
| lightning        |                                     [SAGAClassifier](scikit-contrib-lightning/) | -             | 0.664         |
| lightning        |                                    [FistaClassifier](scikit-contrib-lightning/) | -             | 0.810         |
| lightning        |                                     [SDCAClassifier](scikit-contrib-lightning/) | -             | 0.614         |
| lightning        |                                          [KernelSVC](scikit-contrib-lightning/) | -             | -             |
| lightning        |                                     [SVRGClassifier](scikit-contrib-lightning/) | -             | 0.021         |
| lightning        |                                      [SAGClassifier](scikit-contrib-lightning/) | -             | 0.664         |
| lightning        |                                  [AdaGradClassifier](scikit-contrib-lightning/) | -             | 0.614         |
| lightning        |                                      [SGDClassifier](scikit-contrib-lightning/) | -             | 0.745         |
| RGF              |                                                       [FastRGFClassifier](rgf/) | 0.931         | 0.688         |
| RGF              |                                                           [RGFClassifier](rgf/) | -             | -             |
