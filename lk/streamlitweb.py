import streamlit as st
import checkdb
checkdb.chdbn()
infobaseIDData = checkdb.infobaseIDData
infobaseDescriptionData = checkdb.infobaseDescriptionData
infobaseNameData = checkdb.infobaseNameData

def streamlt():
    st.write(infobaseIDData)
    st.write(infobaseDescriptionData)
    st.write(infobaseNameData)

streamlt()



if __name__ == '__main__':
        os.system('streamlit run streamlitweb.py')
        




