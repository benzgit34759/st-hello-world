import streamlit as st
import math


# In[3]:


st.title("คำนวณจำนวน Insulin ที่ต้องจ่ายใน OPD Case")
st.sidebar.success("Select Any Page from here")


# In[6]:


insulin_type = st.selectbox("ประเภทของอินซูลิน: ", ['Insulin Glargine 300 U/mL, 1.5 mL','Insulin HN70/30 100 IU/mL, 10 mL','NovoRapid 100 U/mL, 3 mL','NovoMix30 100 U/mL, 3 mL','Insulatard 100 IU/mL, 3 mL','Mixtard30 100 IU/mL, 3 mL'])


if insulin_type=='Insulin Glargine 300 U/mL, 1.5 mL':
    unit_per_item=450
    
    
elif insulin_type=='Insulin HN70/30 100 IU/mL, 10 mL':
    unit_per_item=1000
    
elif insulin_type=='NovoRapid 100 U/mL, 3 mL':
    unit_per_item=300
    
elif insulin_type=='NovoMix30 100 U/mL, 3 mL':
    unit_per_item=300
    
elif insulin_type=='Insulatard 100 IU/mL, 3 mL':
    unit_per_item=300
    
else:   #Mixtard30 100 IU/mL, 3 mL
    unit_per_item=300
    
    
unit_use_day = st.number_input("ปริมาณอินซูลินที่ใช้ใน 1 วัน")    
day_of_appointment = st.number_input("จำนวนวันนัด")

amount_of_dispense=unit_use_day*day_of_appointment/unit_per_item

if (st.button('คำนวณจำนวนที่ต้องจ่าย')):
    a="ต้องจ่าย {}".format(math.ceil(amount_of_dispense))
    b=" อัน"
    st.text(a+b)
