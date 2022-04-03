#from matplotlib.pyplot import step
import streamlit as st
import pickle
import numpy as np
import time

def load_model():
    with open('./saved_steps_v2.pkl', 'rb') as file:
        data = pickle.load(file)

    return data

data = load_model()
model = data['model']

def predict_func():

    st.title("Divorce Detection// by_dKC")
    st.markdown("![Alt Text](https://media.giphy.com/media/fv8KclrYGp5dK/giphy.gif)")
    st.write("""### Go through the questionnaire to predict your divorce""")
    st.write("""##### _Answer your quesions 0 being the lowest and 4 being the highest._""")
    Q1 = st.slider('Q1. When we need it, we can take our discussions with my spouse from the beginning and correct it.',0,4)
    Q2 = st.slider('Q2. We dont have time at home as partners.',0,4)
    Q3 = st.slider('Q3. Our dreams with my spouse are similar and harmonious.',0,4,)
    Q4 = st.slider('Q4. We share the same views about being happy in our life with my spouse',0,4,)
    Q5 = st.slider('Q5. My spouse and I have similar ideas about how roles should be in marriage',0,4,)
    Q6 = st.slider('Q6. My spouse and I have similar values in trust.',0,4,)
    Q7 = st.slider('Q7. I know my spouses basic anxieties.',0,4,)
    Q8 = st.slider('Q8. I know my spouses hopes and wishes.',0,4,)
    Q9 = st.slider('Q9. I know my spouse very well.',0,4,)
    Q10 = st.slider('Q10. I know my spouses friends and their social relationships.',0,4,)
    Q11 = st.slider('Q11. I feel aggressive when I argue with my spouse.',0,4,)
    Q12 = st.slider('Q12. I can use offensive expressions during our discussions.',0,4,)
    Q13 = st.slider('Q13. We are just starting a discussion before I know what is going on.',0,4,)
    Q14 = st.slider('Q14. Sometimes I think it is good for me to leave home for a while.',0,4,)
    Q15 = st.slider('Q15. I have nothing to do with what I have been accused of.',0,4,)
    Q16 = st.slider('Q16.  I wouldn not hesitate to tell my spouse about her/his inadequacy.',0,4,)
    Q17 = st.slider('Q17. When I discuss, I remind my spouse of her/his inadequacy.',0,4,)

    ok = st.button('predict divorce')

    if ok:
        x = np.array([[Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17]])

        my_bar = st.progress(0)

        for percent_complete in range(100):
            time.sleep(0.001)
            my_bar.progress(percent_complete + 1)
        
        ans = model.predict(x)

        if ans[0] == 1:
            st.subheader('Possible chance of Divorce')
        elif ans[0] == 0:
            st.subheader('No chance of divorce enjoy')
        else:
            pass

predict_func()