# Divorce_Prediction_V2.0
#### A new upgraded divorce prediction with less no. of question asked and even with high accuracy.

##Data Understanding:-

For data understanding please refer to the divorce_prediction V1.0

Link : https://github.com/dKC-7000001/Divorce_Prediction

## Steps

### <-- Step1 -->---------------->>>Data collection and preprocessing<<<

As the data has no null values and all the cells have ordinal value, there is not much required in data preprocessing.

### <-- Step1 -->---------------->>>Model Building<<<

As the output feature is class variable. Instead of using MLP as in V1.0, cause i wanted to use RFECV and o found out that you can't use Recurssive Feature Elimination with Cross Validation along on a Multi Layer Perceptron, so  i am going to use Support Vector Classifier with linear kernal along with Recursive feature elemination with cross validation. Model also has been cross-validated using test-train split.

With the help of RFECV graph, it is clear that selecting 17 no. of feature is the sweet spot. Which is giving 97.60% of accuracy.

### <-- Step2 -->---------------->>>Dumping Model<<<

After building the model with 97.60% accuracy, it is dumped into a pickle file to use again into the webapp to predict the divorce.

### <-- Step3 -->---------------->>>Building Webapp<<<

With the help of Streamlit library, a basic Webapp has been build, Asking 17 instead of 57 questions from user, and detect his/her divorce.

### If you want to run this Webapp, please go through the requirment.txt to get all the prerequisite. 
#### After creating virtual environment, you need to run this command in your terminal
#### -->conda activate ml
#### -->streamlit run app.py



