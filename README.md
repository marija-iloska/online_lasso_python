# Online LASSO

Note: A MATLAB implementation, which includes reproducibility of the figures in the paper can be found [here](https://github.com/marija-iloska/online_lasso_matlab).

This code is a Python implementation of our ICASSP 2025 paper by the name "Fast Sparse Learning from Streaming Data with LASSO". The proposed method is very easy to implement and we provide an example script how to run, as well as a script that reproduces the figures in the paper. We remark that the proposed method converges only for uncorrelated features. The paper will be linked here once it is published.


## Code
### To run the proposed method <br/>
Run the juptyer notebook example_code.m - specify the system settings in the top cells for the desired synthetic data (e.g., noise, length, sparsity). <br/>
<br/>


### Organization <br/>
module "proposed_method" contains "online_lasso"  - the fn where the proposed method is implemented. <br/>

util/generate_data.m - a fn that generates data. <br/>
util/bar_plot - a fn that makes bar plots to visualize feature seleciton. <br/>



