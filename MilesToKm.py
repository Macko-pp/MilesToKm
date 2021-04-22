#Imports-----------------------------------------------------------------------

import streamlit as st
import webbrowser

#Title-------------------------------------------------------------------------

co1, co2, co3 = st.beta_columns(3)

co2.title("Speed Converter")
co2.write(" ")
co2.write("Made By: Max Konietzko")
co2.write(" ")

#Input-&-Colomns---------------------------------------------------------------

col1, col2 = st.beta_columns(2)

mph1 = col1.number_input("Miles Per Hour:")
kmph1 = col2.number_input("Kilometers Per Hour:")

#Math--------------------------------------------------------------------------

mph2 = kmph1 * 0.621371
kmph2 = mph1 * 1.60934
ms1 = mph1 / 2.237
ms2 = kmph1 / 3.6
kpd = kmph2 * 24
mpd = mph2 * 24


#Result-Colomn-1---------------------------------------------------------------

col1.write("Kilometers per Day:")
col1.write(kpd)

col1.write("Kilometers Per Hour:")
col1.write(kmph2)

col1.write("Meters Per Second:")
col1.write(ms1)

#Result-Colomn-2---------------------------------------------------------------

col2.write("Miles per Day:")
col2.write(mpd)

col2.write("Miles Per Hour:")
col2.write(mph2)

col2.write("Meters Per Second:")
col2.write(ms2)

#Input-Ms----------------------------------------------------------------------

ms3 = st.number_input("Meters Per Second:")

#Math2-------------------------------------------------------------------------

msKph = ms3 * 3.6
msMph = ms3 * 2.23694

#Result-&-Colu-----------------------------------------------------------------

colu1, colu2 = st.beta_columns(2)

colu1.write("Miles Per Hour:")
colu2.write("Kilometers Per Hour:")

colu1.write(msMph)
colu2.write(msKph)
