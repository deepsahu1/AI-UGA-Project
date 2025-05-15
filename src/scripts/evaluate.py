import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def eval_func(gt, pred, range_):
    mse = mean_squared_error(gt, pred)
    mae = mean_absolute_error(gt, pred)
    r2 = r2_score(gt, pred)   

    # regression plot, minimal scatter on dots is ideal.
    plt.scatter(gt,pred),plt.plot([min(gt), max(gt)],[min(pred),max(pred)], 'r:'),plt.xlabel('GT'),plt.ylabel('Pred'),plt.title('Ground vs Predicted')
    plt.show()

    ## residual plot, minimal vertical spread is ideal.
    resid = gt - pred
    plt.scatter(pred, resid),plt.axhline(0,color='red',linestyle='--'),plt.xlabel('Pred'),plt.ylabel('Residual'),plt.title('Residual Visualization')
    plt.show()

    print("Range:", range_)
    print("MSE:", mse)
    print("RMSE:", np.sqrt(mse))
    print("MAE:", mae)
    print("R2:", r2)

df = pd.read_csv("../../data/raw/data.csv")

## fake data creation for testing purposes
# organized = np.zeros((15,int(df.shape[0]/15),df.shape[1]))
# counties = pd.unique(df['Location/county'])
# vals = list(df.columns[2:])
# dates = df.Quarter_DDMMYYYY[0:organized.shape[1]].values

do_range = df['DO'].max() - df['DO'].min()
gt_do = df['DO'].values

pred_do = df.copy()
pred_do = gt_do + np.random.uniform(do_range*-1, do_range, size = df.shape[0])


eval_func(gt_do,pred_do,do_range)







