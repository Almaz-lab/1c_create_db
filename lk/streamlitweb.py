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




if __name__ == '__main__':
        streamlt()




