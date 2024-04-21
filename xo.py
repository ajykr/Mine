import streamlit as st

def largest_number(a, b, c):
    return max(a, b, c)

def main():
    st.title('Find the Largest Number')
    
    st.write('Enter three numbers below:')
    num1 = st.number_input('Number 1', value=0)
    num2 = st.number_input('Number 2', value=0)
    num3 = st.number_input('Number 3', value=0)
    
    if st.button('Find Largest'):
        largest = largest_number(num1, num2, num3)
        st.write(f'The largest number is: {largest}')

if __name__ == "__main__":
    main()
