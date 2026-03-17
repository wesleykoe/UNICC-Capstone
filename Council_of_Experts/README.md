## Updates (03/07):

1. Previously, training data sets contained rows with outputs but no inputs. This has been fixed and now please refer to the training data labeled |expert_name|_merged. 
2. Currently, we are beginning to train each (expert adapter) with the training data we built.
3. After training each expert, we would factor in the arbitration rule into the workflow.
4. All coding has been moved from Pycharm (local) to Google Colab due to better processing power. We are also using Mistral7 currently as the base model.
