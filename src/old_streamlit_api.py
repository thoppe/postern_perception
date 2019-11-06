# streamlit run P1_API.py

import streamlit as st
import numpy as np
from P0_generate_samples import eyeGAN

#@st.cache(allow_output_mutation=True)
def load_model():
    return eyeGAN()

G = load_model()

st.title('My first app')
st.write('Hello, world!')

a0 = st.slider('angle0',-1.,1.,0.1)
a1 = st.slider('angle1',-1.,1.,0.1)

st.write(f'Angles {a0} {a1}')

res = G('sample.jpg', [a0], [a1])
img = (res[0, :, :, :] + 1 * 127.5).astype(np.uint8)
#img = (res[0, :, :, :] + 1 * 127.5).astype(np.uint8)
#st.image(img, use_column_width=True)
#st.image(img, use_column_width=True)
st.write(img)


#G = eyeGAN()
#res = G('sample.jpg', AX, AY)
#print(res)
