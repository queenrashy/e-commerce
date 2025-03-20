from flask import jsonify, request
from app import app, db
from models import product, Admin_product


@app.route('/search', methods=['GET'])
def search():
    search_item = request.args.get('query')
    category_item = request.args.get('category')
    price_amount = request.args.get('price')
    
    query = Admin_product.query
    
    if  not search_item and not category_item and not price_amount :
        return jsonify({'error': 'Please enter a search term'}), 400
    
    if search_item:
        query = query.filter(Admin_product.product_name.ilike(f'%{search_item}%'))
        
    if category_item:
        query = query.filter(Admin_product.category.ilike(f'%{category_item}%'))
        
    if price_amount:
        query = query.filter(Admin_product.price.ilike(f'%{price_amount}%'))
        
    results = query.all()
     
  

    return jsonify({
        'result': [item.format() for item in results],
        'count': len(results)
    })
      
      
      
      
# Category and Tag System- Create categories
# (e.g., Electronics, Clothing).- 
# Allow products to belong to a category.- 
# Optionally, add a tag system for better filter


@app.route('/category', methods=['GET'])
def search_category():
    data = request.json
    category = data.get('category')
    
    