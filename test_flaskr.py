import os
import unittest
from flask import json
from flaskr import create_app
from models import setup_db, Car


class CarBookTestCase(unittest.TestCase):
    '''This class represents a Car Book test'''
  
    def setUp(self):
        '''Define test variable and initialize app'''
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "carbook_test"
        self.database_path = "postgresql://postgres:nirinasoa@localhost:5432/{}".format(self.database_name)
        setup_db(self.app, self.database_path)
        
        self.new_car = {
          "name": "Voiture",
          "model": "XZ",
          "image_link": "http://voiture.image"
        }
        
    def tearDown(self):
        pass
      
    def test_create_new_car(self):
        res = self.client().post('/cars', json=self.new_car)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['cars'])
        self.assertTrue(len(data['cars']))
        
    def test_retrieve_car_paginate(self):
        res = self.client().get('/cars')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['cars'])
        
    def test_view_single_car(self):
        res = self.client().get('/cars/2')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['car'])
        
    def test_search_car(self):
        res = self.client().post('/cars', json={"search_term":"bmw"})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['results'])
        self.assertTrue(len(data['results']))
        
    def test_update_car(self):
        res = self.client().put('/cars/2', json={"image_link":"http://bmw.png"})
        data = json.loads(res.data)
        
        car = Car.query.get(2)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], "Car updated successfully")
        self.assertEqual(car.id, 2)
        
    def test_patch_car(self):
        res = self.client().patch('/cars/13', json={"name":"Ferrari", "image_link":"ferrari.png"})
        data = json.loads(res.data)
        
        car = Car.query.get(13)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(car.id, 13)
        
    def test_delete_car(self):
        res = self.client().delete('/cars/15')
        data = json.loads(res.data)
    
        car = Car.query.get(15)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 15)
        self.assertTrue(len(data['cars']))
        self.assertEqual(car, None)
        
    def test_400_bad_request(self):
        res = self.client().patch('/cars/100', json={"name":"Honda"})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "bad request")
        
    def test_404_resource_not_found(self):
        res = self.client().get('/cars/100')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "resource not found")
        
    def test_405_method_not_allowed(self):
        res = self.client().post('/cars/100', json=self.new_car)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "method not allowed")
    
    def test_422_unprocessable(self):
        res = self.client().delete('/cars/100')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "unprocessable")    
    
    
if __name__ == "__main__":
    unittest.main()