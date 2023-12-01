import unittest
from api import app

class TestFlaskApp(unittest.TestCase):

    def test_obtener_contactos_success(self):
        tester = app.test_client(self)
        response = tester.post('/billetera/contactos', json={'query': '123456789'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'contactos' in response.data)

    def test_obtener_contactos_error_method(self):
        tester = app.test_client(self)
        response = tester.put('/billetera/contactos')
        self.assertEqual(response.status_code, 405)

    def test_obtener_historial_error_post(self):
        tester = app.test_client(self)
        response = tester.post('/billetera/historial')
        self.assertEqual(response.status_code, 415)

    def test_obtener_historial_error_invalid_account(self):
        tester = app.test_client(self)
        response = tester.get('/billetera/historial?minumero=invalid_account')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
