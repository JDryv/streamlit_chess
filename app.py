import streamlit as st
import chess
import chess.svg
import streamlit.components.v1 as components

# Initialize session state for the board
if "board" not in st.session_state:
    st.session_state.board = chess.Board()

# Function to render the chessboard
def render_board(board):
    board_svg = chess.svg.board(board=board).encode("utf-8")
    return components.html(board_svg, height=400)

# Function to make a move
def make_move(move):
    try:
        st.session_state.board.push_san(move)
    except ValueError:
        st.error("Invalid move!")

st.title("Play Chess")

# Display the chessboard
render_board(st.session_state.board)

# User input for the move
move = st.text_input("Enter your move in UCI format (e.g., e2e4):")

# Make the move if the button is clicked
if st.button("Make move"):
    make_move(move)

# Reset the board if the button is clicked
if st.button("Reset Board"):
    st.session_state.board.reset()
    st.experimental_rerun()
