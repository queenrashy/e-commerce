from flask import jsonify, request
from app import app, db
from models import  Admin_product


# admin can to add and delete and update 

# Admin add
@app.route('/admin_add', methods=['POST'])
def admin_add():
    data = request.json
    product_name = data.get('product_name')
    description = data.get('description')
    price =  data['price']
    stock =  data.get('stock')
    category = data.get('category')
    
    if product_name is None or description is None or price is None or stock is None or category is None:
        return jsonify({'error': 'Please fill all field'}), 400
    
    # if price is None:
    #     return jsonify({'error': 'Enter price'})
    
    try:
        new_product = Admin_product(product_name=product_name,description=description,price=price,stock=stock,category=category)
        db.session.add(new_product)
        db.session.commit()
        return jsonify({'success': True, 'message': ' new product added'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Can not add new a product: {e}'}), 400
        
        


# admin delete
@app.route('/<int:id>', methods=['DELETE'])
def delete_product(id):
       product = Admin_product.query.filter(Admin_product.id == id).first()
       if product is None:
           return jsonify({'error': "product don't not exist"}), 404
       
       db.session.delete(product)
       db.session.commit()
       return jsonify({'done': True, 'message': ' Has been deleted successfully.'}), 200
   
   
# admin update
@app.route('/<int:id>', methods=['PUT'])
def update_product(id):
    product = Admin_product.query.get(id)   
    data= request.json
    product.product_name = data.get('product_name') or product.product_name
    product.description = data.get('description') or product.description
    product.price = data.get('price') or product.price
    product.stock =data.get('stock') or product.stock
    product.category = data.get('category') or product.category
    if product is None:
        return jsonify({'error':'Product not found'}), 404
    if product:
        db.session.commit()
        return jsonify({'done': True, 'message': 'updated successfully'})
