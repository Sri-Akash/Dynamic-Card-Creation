from flask import Flask, render_template, request, jsonify
from mongoengine import connect, connection
from models import Product

app = Flask(__name__)

print(__name__)

try:
    connect(host="mongodb://localhost:27017/DynamicCardCreation")
    if connection.get_connection():
        print("Database connected Successfully.")
    else:
        print("Database not connected.")
except Exception as e:
    print(f"Error, {str(e)}")

cardList = []

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/product/new")
def newProduct():
    try:
        product = request.get_json()
        print(product)

        if not product:
            return jsonify({"status": "error", "message": "All fields required."})    

        imageUrl = product.get("imageUrl")
        name = product.get("name")
        category = product.get("category")
        stock = product.get("stock")
        price = product.get("price")
        description = product.get("description")

        # cardList.append(product)

        Product(
            imageUrl = imageUrl,
            name = name,
            category = category,
            stock = int(stock),
            price = float(price),
            description = description
        ).save()

        return jsonify({"status": "success", "message": "Product Added Successfully."})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error {str(e)}"})
    

@app.get("/product/getAll")
def getAllProduct():
    try:
        products = Product.objects()

        if not products:
            return jsonify({"status": "error", "message": "Products Empty."}) 
        
        productList = []
        for product in products:
            data = {
                "id": str(product.id),
                "imageUrl": product.imageUrl,
                "name": product.name,
                "category": product.category,
                "stock": product.stock,
                "price": product.price,
                "description": product.description,
                "addedTime": product.addedTime
            }

            productList.append(data)

        return jsonify({"status": "success", "message": "Product Retrieved Successfully.", "data": productList})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error {str(e)}"})
    

@app.get("/product/getSingle")
def getSingleProduct():
    try:
        id = request.args.get("id")

        if not id:
            return jsonify({"status": "error", "message": "Id is required."}) 
        
        product = Product.objects(id=id).first()

        if not product:
            return jsonify({"status": "error", "message": "Products Empty."}) 
        
        data = {
            "id": str(product.id),
            "imageUrl": product.imageUrl,
            "name": product.name,
            "category": product.category,
            "stock": product.stock,
            "price": product.price,
            "description": product.description,
            "addedTime": product.addedTime
        }

        return jsonify({"status": "success", "message": "Product Retrieved Successfully.", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error {str(e)}"})
    

@app.put("/product/update")
def updateProduct():
    try:
        id = request.args.get("id")

        if not id:
            return jsonify({"status": "error", "message": "Id is required."})    
        
        product = request.get_json()
        print(product)

        if not product:
            return jsonify({"status": "error", "message": "All fields required."})    

        imageUrl = product.get("imageUrl")
        name = product.get("name")
        category = product.get("category")
        stock = product.get("stock")
        price = product.get("price")
        description = product.get("description")

        product = Product.objects(id=id).first()
        if not product:
            return jsonify({"status": "error", "message": "Product not found."})
        

        product.imageUrl = imageUrl
        product.name = name
        product.category = category
        product.stock = int(stock)
        product.price = float(price)
        product.description = description

        product.save()

        return jsonify({"status": "success", "message": "Product Updated Successfully."})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error {str(e)}"})
    

@app.delete("/product/delete")
def deleteProduct():
    try:
        id = request.args.get("id")

        if not id:
            return jsonify({"status": "error", "message": "Id is required."}) 
        
        product = Product.objects(id=id).first()
        if not product:
            return jsonify({"status": "error", "message": "Product not found."})
        
        product.delete()
         
        return jsonify({"status": "success", "message": "Product Deleted Successfully."})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error {str(e)}"})
      

if "__main__" == __name__:
    app.run(debug=True)


#hello
#hi
#hahahahahahha
