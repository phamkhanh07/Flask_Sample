# all the import
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# configuration
DATABASE = 'E:\Python\Flask_Sample\ex1.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'