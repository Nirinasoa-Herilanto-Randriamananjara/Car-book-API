from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from models import setup_db, Car

CAR_PAGINATION_PER_PAGE = 10

def paginated_car(selection, page):
    start = (page - 1) * CAR_PAGINATION_PER_PAGE
    end = page * CAR_PAGINATION_PER_PAGE
    
    data = [car.format() for car in selection]
    
    return data[start:end]

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE,OPTIONS')
        return response
      
    @app.route('/')
    def welcome_app():
        return jsonify({
            "message": "Welcome to Car book API"
        })
    
    @app.route('/cars')
    def retrieve_cars():
        page = request.args.get('page', 1, type=int)
        
        all_cars = Car.query.order_by(Car.id).all()
        data = paginated_car(all_cars, page)
        
        if len(data) == 0:
            abort(404)
            
        return jsonify({
            "success": True,
            "cars": data,
            "total_cars": len(all_cars)
        })
        
    @app.route('/cars/<int:car_id>')
    def view_single_car(car_id):
        car = Car.query.get(car_id)
        
        if car is None:
            abort(404)
        else:
            return jsonify({
                "success": True,
                "car": car.format()
            })
        
    @app.route('/cars', methods=['POST'])
    def create_car():
        try:
            body = request.get_json()
            page = request.args.get('page', 1, type=int)
        
            name = body.get('name', None)
            model = body.get('model', None)
            image_link = body.get('image_link', None)
            search_term = body.get('search_term', None)
            
            if search_term:
                search_results = Car.query.order_by(Car.name).filter(Car.name.ilike('%' + search_term + '%')).all()

                # data = [result.format() for result in search_results]
                data = paginated_car(search_results, page)
                
                return jsonify({
                    "success": True,
                    "results": data,
                    "total_results": len(search_results),
                })
                
            else:
                car = Car(name=name, model=model, image_link=image_link)
                car.insert()
                
                all_cars = Car.query.order_by(Car.id).all()
                data = paginated_car(all_cars, page)
                
                return jsonify({
                    "success": True,
                    "created": car.id,
                    "message": "Car created successfully",
                    "cars": data,
                    "total_cars": len(all_cars)
                })
    
        except:
            abort(422)  
            
    @app.route('/cars/<int:car_id>', methods=['PUT', 'PATCH'])
    def update_car(car_id):
        try:
            body = request.get_json()
            car = Car.query.get(car_id)
            
            if car is None:
                abort(404)
            
            if "name" in body:
                car.name = body.get('name')
    
            if "model" in body:
                car.model = body.get('model')
                
            if "image_link" in body:
                car.image_link = body.get('image_link')
            
            car.update()
            
            return jsonify({
                "success": True,
                "car_id": car.id,
                "message": "Car updated successfully",
            })
            
        except:
            abort(400)
            
    @app.route('/cars/<int:car_id>', methods=['DELETE'])
    def delete_car(car_id):
        try:
            car = Car.query.get(car_id)
            page = request.args.get('page', 1, type=int)
            
            if car is None:
                abort(404)
                
            car.delete()
            
            all_cars = Car.query.order_by(Car.id).all()
            data = paginated_car(all_cars, page)
            
            return jsonify({
                "success": True,
                "deleted": car.id,
                "message": "Car deleted successfully",
                "cars": data,
                "total_cars": len(all_cars)
            })
            
        except:
            abort(422)
            
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400
        
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404
        
    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "method not allowed"
        }), 405
        
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422
            
    return app