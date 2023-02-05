
import os

import torch


class EarlyStopping():
    """
    Early stopping to stop the training when the loss does not improve after
    certain epochs.
    """
    def __init__(self, patience=5, min_delta=0):
        """
        :param patience: how many epochs to wait before stopping when loss is
               not improving
        :param min_delta: minimum difference between new loss and old loss for
               new loss to be considered as an improvement
        """
        self.patience = patience
        self.min_delta = min_delta
        self.counter = 0
        self.best_loss = None
        self.early_stop = False
    def __call__(self, loss, model, args, name, iteration):
        if self.best_loss == None:
            self.best_loss = loss
        elif self.best_loss - loss > self.min_delta:
            self.best_loss = loss
            # torch.save(model.module.state_dict(), os.path.join(args.output_dir, 'param_' + name + '_WQ_' + str(iteration) +'.pt'), _use_new_zipfile_serialization = False)
            # reset counter if validation loss improves
            self.counter = 0
        elif self.best_loss - loss < self.min_delta:
            self.counter += 1
            print(f"INFO: Early stopping counter {self.counter} of {self.patience}")
            if self.counter >= self.patience:
                print('INFO: Early stopping')
                self.early_stop = True

if __name__ == '__main__':
    early = EarlyStopping()
    early(5)
    early(6)
    print(early.early_stop)
   