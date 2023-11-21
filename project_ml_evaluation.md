#### SER594: Machine Learning Evaluation
#### Social Media and Attention Span
#### James Thayer
#### 11/20/2023

## Evaluation Metrics
### Metric 1
**Name:**  
d2_rt [float]  
  
**Choice Justification:**  
d2_rt is the average response time per processed symbol in the d2 cancellation test expressed in seconds.  
The d2 test is a cancellation test to measure attention, visual scanning, and processing speed.  
  
### Metric 2  
**Name:**  
d2_fa_rate [float]  
  
**Choice Justification:**  
d2_fa_rate is the average rate ([0-1]) at which a child incorrectly cancelled a symbol in  
the d2 cancellation test. This will allow for measurement of error and enable comparisons  
with other d2_rt.   
  
## Original Model   
**Construction:**  
The linear regression model assumes a linear relationship between d2_rt and d2_fa_rate.  
The coeffients are estimated to minimize the sum of the squared differences between actual  
and predicted values. The LinearRegression training method was used.  
  
**Evaluation:**  
There is a low MSE meaning that its predictions are close to the actual values.
  
## Alternative Models    
### Alternative 1
**Construction:** 
Ridge Regression was constructed by including L2 regularization to prevent overfitting.  
It is an extension of linear regression. Training was done with the Ridge class.  
  
**Evaluation:**  
The Ridge Regression model's performance is similar to the linear regression model.    
The regularization term in Ridge Regression might have limited the impact of coefficients,  
but the overall performance is about the same.  
  
## Alternative Models    
### Alternative 2  
**Construction:**  
Decision Tree Resgression was constructed by having each input is an internal node and  
each predicted value represented as a leaf node. It was used to be able to see non-linear 
correlations. Training was done with the DecisionTreeRegressor class.  
  
**Evaluation:**  
The Decision Tree model has a higher MSE compared to the linear models, suggesting that its  
predictions have more variance from the actual values.  
  
## Alternative Models  
### Alternative 3  
**Construction:**  
Random Forest was constucted by make multiple decision trees during training and taking the  
average prediction of the trees. It was trained using the RandomForestRegressor class.  
  
**Evaluation:**
Similar to the Decision Tree model, the Random Forest model has a higher MSE compared to  
linear models.  
  
## Best Model  
**Model:**  
Ridge Regression