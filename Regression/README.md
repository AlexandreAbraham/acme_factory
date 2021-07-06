# Benchmark on California Housing

|      Package     |                                       Model                                     |     Score     |
| ---------------- | -------------------------------------------------------------------------------:|:------------- |
| scikit-learn     |                                                                    RandomForest | 0.787         |
| scikit-learn     |                         [GradientBoostingRegressor](GradientBoostingRegressor/) | 0.847         |
| scikit-learn     |                                         [AdaboostRegressor](AdaboostRegressor/) | 0.661         |
| scikit-garden    |                 [MondrianForestRegressor](scikit-garden-MondrianTreeRegressor/) | 0.736         |
| scikit-garden    |   [RandomForestQuantileRegressor](scikit-garden-RandomForestQuantileRegressor/) | 0.794         |
| scikit-garden    |       [ExtraTreesQuantileRegressor](scikit-garden-ExtraTreesQuantileRegressor/) | 0.769         |
| node (pytorch)   |                                                 [NodeRegressor](NodeRegressor/) | 0.570         |
| lightning        |                                       [SGDRegressor](scikit-contrib-lightning/) | -9.36e+191    |
| lightning        |                                        [CDRegressor](scikit-contrib-lightning/) | -2.616        |
| lightning        |                                       [SAGRegressor](scikit-contrib-lightning/) | -3.136        |
| lightning        |                                      [SAGARegressor](scikit-contrib-lightning/) | -3.131        |
| lightning        |                                          [LinearSVR](scikit-contrib-lightning/) | 0.555         |
| lightning        |                                      [SVRGRegressor](scikit-contrib-lightning/) | -             |
| lightning        |                                     [FistaRegressor](scikit-contrib-lightning/) | -2.616        |
| lightning        |                                      [SDCARegressor](scikit-contrib-lightning/) | -2.821        |
| lightning        |                                   [AdaGradRegressor](scikit-contrib-lightning/) | -2.822        |
| RGF              |                                                            [RGFRegressor](rgf/) | -             |
| RGF              |                                                        [FastRGFRegressor](rgf/) | -             |

