import src.password_generator as pg
import streamlit as pt

# streamlit run main.py

def main():
    types=("Random Password", "Memorable Password", "PIN")
    pt.write('The Password Generator')
    with pt.form('password_generation'):
        try:
            option = pt.selectbox(
                "Choose a type of password generation",
                options=types,
                index=None,
                placeholder='Select option here...',
            )
            submmited=pt.form_submit_button(label='Submit')

            if submmited:
                generator=pg.PasswordGenerator(choosed_type=types.index(option))
            else:
                raise ValueError
        except ValueError as e:
            print(e)
            @pt.dialog('Error')
            def show():
                pt.write('Choose between the options')

if __name__ == "__main__":
    main()