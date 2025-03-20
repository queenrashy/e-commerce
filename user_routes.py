from flask import jsonify, request
from app import app, db
from models import User
from toolz import is_valid_email
from werkzeug.security import generate_password_hash

# user sign up
@app.route('/sign_up', methods=['POST'])
def signup():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    # role = data.get('role')
    
    # check names
    if name is None or len(name) < 2:
        return jsonify({'error': 'Please enter a valid name;!'}), 400
    
    # check if email is valid
    if not is_valid_email(email):
        return jsonify({'error': 'Please enter a valid email!'}), 400
    
      # check password
    if password is None or len(password) < 6:
        return jsonify({'error': 'Password must be more than 6 characters'}), 400
    
    # check if email is unique
    exists = User.query.filter(User.email == email).first()
    if exists is not None:
        return jsonify({'error': 'Email already exists'}), 400

    # create new user
    try:
        new_user = User(name=name, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Account created successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'User signup error: {e}'}), 400
        
        
#user login
@app.route('/login')
def login_user():
    email = request.json.get('email')
    password = request.json.get('password')
    
    if email is None or password is None:
        return jsonify({'error': 'Please enter email and password'}), 401
    
    if not is_valid_email(email):
        return jsonify({'error': 'Please enter a valid email address!'}), 400
    
    # find user
    
    user = User.query.filter_by(email=email).first()
    if user is None:
        return jsonify({'error': 'User with this email does not exist'}), 401
   
    
    # validate password
    if user.check_password(password):
        #password is correct, generate jwt token
        # token = user.generate_auth_token()
        return jsonify({'success': True, 'message': 'you are logged in'})
    
    return jsonify({'error': 'Invalid email or password.'})



# logout 
# @app.routes('/logout'):

# update name or email
@app.route('/<email>', methods=['PUT'])
def update_user(email):
    user = User.query.filter(User.email == email).one_or_404()
    data = request.json
    user.email = data.get('email') or user.email
    user.name = data.get('name') or user.name
    user.role = data.get('role') or user.role
    
    if email  is None:
        return jsonify({'error': 'user with this email does not exist'}), 404
    db.session.commit()
    return jsonify({'done':True, 'message': f'{user} updated successfully'})


# Users should be able to view all products or filter/search them.



















# update password