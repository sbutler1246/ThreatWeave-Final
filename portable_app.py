"""Streamlit entry point for the independently installed development application."""
from portable_sources import install
install()
from streamlit_app import main
main()
