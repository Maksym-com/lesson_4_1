import datetime, hashlib

from flask import Blueprint, render_template, redirect, url_for, flash, request
from sqlalchemy import select
from flask_login import login_user

from app.models import User
from app.database import Session
from app.forms import RegistrationForm, LoginForm

bp = Blueprint('company', __name__)