import streamlit as st
st.text("*"*100)
st.subheader("Welcome to Our Page!!!")
st.text("We will tell your future depending on your choosing number")
st.text("So you can enter one number from 1 to 9 ")
st.caption("Just for fun !!!!")

form = st.form(key='my_form')
name=form.text_input(label='Enter your name:')
number=form.text_input(label='Enter your number')
submit_button = form.form_submit_button(label='Submit')
if (submit_button):
    if(name=="" or number==""):
        st.text("Please Fill your data")
    else:
        st.text("*"*80)
        if int(number)==1:
            st.write(name,", you will get some gift from someone")
        elif int(number)==2:
            st.write(name,", you will lose your money so takecare yourself")
        elif int(number)==3:
            st.write(name,", you will get pocket money from someone")
        elif int(number)==4:
            st.write(name,", you will be happy with your someone special")
        elif int(number)==5:
            st.write(name,", you will hear good news for your jobs")
        elif int(number)==6:
            st.write(name,", you will get boyfriend/girlfriend soon")
        elif int(number)==7:
            st.write(name,", you will lose your shoes ")
        elif int(number)==8:
            st.write(name,", you will lose your pocket but you will get new one ")
        elif int(number)==9:
            st.write(name,", you will be happy in our new house")
        st.text("*" * 80)
st.text("*"*100)
st.text("In this section we will tell your inner mind dependign on your favourite color")
genre = st.radio("What's your favorite color",('purple','black','white','gray','red','pink','orange','blue'))

if genre=='purple':
    st.caption('You are a perfectionist who requires emotional security in life, and you are a good humanitarian who helps others in need.')
    st.caption('You have a good mind, a ready wit, and an ability to observe things that go unnoticed by others. You have a degree of vanity. You display a fine-art creativity.')
elif genre=='black':
    st.caption('You strive for power and control in life, but are often artistic and intuitive and do not share things well with others.')
    st.caption('You’re above average, worldly, conventional, proper, polite, and regal. While black may mean “depression” to the clinical psychologist, to you it means “dignity.”')
elif genre=='white':
    st.caption('You are organized and very independent, and you rely on logic to solve every problem.')
elif genre=='gray':
    st.caption('You are cool and composed and a very reliable person who tends to conform to keep the peace.')
    st.caption('Favoring gray shows that you’re cautious and seek to strive a compromise in most situations you encounter. You seek composure and peace, and try very hard to fit yourself into a mold of your own design.')
elif genre=='red':
    st.caption('You have drive and determination, and you prefer action and risk-taking behaviors. Your biggest need is for physical fulfillment and fitness.')
    st.caption('Red shows that you’re outgoing, assertive, vigorous, and prone to impulsive actions and variable moods. You feel deep sympathy for fellow human beings, and have a strong sex drive. ')
elif genre=='pink':
    st.caption('All you want in life is unconditional love and to be accepted for who you are by your peers.')
elif genre=='orange':
    st.caption('Favoring orange shows that you’re good-natured, enjoy being with other people, and are swayed by outside opinions. You do good work,, have strong loyalties, feel good will toward others, and have a solicitous heart.')
elif genre=='blue':
    st.caption('Preferring blue shows that you’re deliberate and introspective. You have conservative convictions, retreat to gentler surroundings in times of stress, and are sensitive to the feelings of others. You’re a loyal friends and lead a sober life.')
st.text("*"*100)
st.text("*"*100)
st.caption("Be Happy and Lucky Person !!! Have a nice day !!!")

col1, col2, col3,col4 = st.columns(4)
with col1:
    st.image("1.jpg")
with col2:
    st.image("2.jpg")
with col3:
    st.image("3.jpg")
with col4:
    st.image("4.jpg")
st.text("*"*100)

