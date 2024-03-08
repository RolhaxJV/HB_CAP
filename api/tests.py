import json
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from api.views import Detail_Table,List_Table
from covid_project.settings import API_KEY


factory = APIRequestFactory()

# region TestDose
table = 'dose'
pk = 'AstraZeneca_2021-06-13_84_63_Puy-de-Dôme'
# region test Detail 
view = Detail_Table.as_view()
req = factory.get('Detail/',headers={'Authorization': API_KEY})
do_res_tg = view(req, table=table, pk=pk)
do_res_tg.render()
do_json_res_tg = json.loads(do_res_tg.content)

do_res_tgonf = view(req, table=table, pk=None)
do_res_tgonf.render()

do_res_git = view(req, table="invalid_table", pk=pk)
do_res_git.render()

do_res_gip = view(req, table=table, pk='invalid_pk')
do_res_gip.render()

# endregion

# region test List
view = List_Table.as_view()

req = factory.get('List/',{'table': table},headers={'Authorization': API_KEY})
do_res_ndl = view(req)
# endregion
# endregion

class TestDose(TestCase):
    def setUp(self):
        """
        Set up the test fixture. This method is called before the execution of each test function.
        """
        pass

    def test_get(self):
        """
        Test the get method by comparing the result with a predefined data dictionary.
        """
        data = {
                "pk_dose": "AstraZeneca_2021-06-13_84_63_Puy-de-Dôme",
                "nb_ucd": 388.0,
                "nb_dose": 3880.0,
                "Type": "AstraZeneca",
                "Date": "2021-06-13",
                "Depart": "84_63_Puy-de-Dôme"
                }
        self.assertEqual(do_json_res_tg, data)
    
    def test_get_object_not_found(self):
        """
        Test for handling the case when the object is not found.
        """
        self.assertEqual(do_res_tgonf.status_code, 404)
        self.assertEqual(do_res_tgonf.data['message'], 'Objet non trouvé')

    def test_get_invalid_table(self):
        """
        Test for getting an invalid table.
        """
        self.assertEqual(do_res_git.status_code, 404)
        self.assertEqual(do_res_git.data['message'], 'queryset nonetype')

    def test_get_invalid_pk(self):
        """
        Test case for checking the behavior of getting an invalid primary key.
        """
        self.assertEqual(do_res_gip.status_code, 404)
        self.assertEqual(do_res_gip.data['message'], 'Objet non trouvé')

    def test_nombre_de_lignes(self):
        """
        Test the number of lines in the data with the expected value of 32954.
        """
        self.assertEqual(do_res_ndl.status_code, 200)
        self.assertEqual(do_res_ndl.data['nombre_de_lignes'], 32954)

# region TestDate
table = 'date'
pk = '2021-06-13'
# region test Detail 
view = Detail_Table.as_view()
req = factory.get('Detail/',headers={'Authorization': API_KEY})

da_res_tg = view(req, table=table, pk=pk)
da_res_tg.render()
da_json_res_tg = json.loads(da_res_tg.content)

da_res_tgonf = view(req, table=table, pk=None)
da_res_tgonf.render()

da_res_git = view(req, table="invalid_table", pk=pk)
da_res_git.render()

da_res_gip = view(req, table=table, pk='2025-01-01')
da_res_gip.render()

# endregion

# region test List
view = List_Table.as_view()

req = factory.get('List/',{'table': table},headers={'Authorization': API_KEY})
da_res_ndl = view(req)
# endregion
# endregion

class TestDate(TestCase):   
    def setUp(self):
        """
        Set up the test fixture. This method is called before the execution of each test function in the test class.
        """
        pass

    def test_get(self):
        """
        This function is used to test the get method. It doesn't take any parameters and doesn't return anything.
        """
        data = {
                "date": "2021-06-13"
                }
        self.assertEqual(da_json_res_tg, data)
        
    def test_get_object_not_found(self):
        """
        Test for getting an object that is not found.
        """
        self.assertEqual(da_res_tgonf.status_code, 404)
        self.assertEqual(da_res_tgonf.data['message'], 'Objet non trouvé')

    def test_get_invalid_table(self):
        """
        Test for getting an invalid table.
        """
        self.assertEqual(da_res_git.status_code, 404)
        self.assertEqual(da_res_git.data['message'], 'queryset nonetype')

    def test_get_invalid_pk(self):
        """
        Test case for checking the behavior when getting an invalid primary key.
        """
        self.assertEqual(da_res_gip.status_code, 404)
        self.assertEqual(da_res_gip.data['message'], 'Objet non trouvé')
        
    def test_nombre_de_lignes(self):
        """
        Test the nombre_de_lignes function.
        """
        self.assertEqual(da_res_ndl.status_code, 200)
        self.assertEqual(da_res_ndl.data['nombre_de_lignes'], 100)

# region TestDepart
table = 'departement'
pk = '84_63_Puy-de-Dôme'
# region test Detail 
view = Detail_Table.as_view()
req = factory.get('Detail/',headers={'Authorization': API_KEY})

de_res_tg = view(req, table=table, pk=pk)
de_res_tg.render()
de_json_res_tg = json.loads(de_res_tg.content)

de_res_tgonf = view(req, table=table, pk=None)
de_res_tgonf.render()

de_res_git = view(req, table="invalid_table", pk=pk)
de_res_git.render()

de_res_gip = view(req, table=table, pk='invalid_pk')
de_res_gip.render()

# endregion

# region test List
view = List_Table.as_view()

req = factory.get('List/',{'table': table},headers={'Authorization': API_KEY})
de_res_ndl = view(req)
# endregion
# endregion

class TestDepart(TestCase):
    def setUp(self):
        """
        A method to set up the test fixture. No parameters or return types specified.
        """
        pass

    def test_get(self):
        """
        This function is a test for the get method. It sets up a test data dictionary and asserts that a certain variable is equal to the test data.
        """
        data = {
                "pk_depart": "84_63_Puy-de-Dôme",
                "code_region": "84",
                "code_depart": "63",
                "label_region": "ARA",
                "label_depart": "Puy-de-Dôme"
                }
        self.assertEqual(de_json_res_tg, data)

    def test_get_object_not_found(self):
        """
        Test case for handling the scenario when the object is not found.
        """
        self.assertEqual(de_res_tgonf.status_code, 404)
        self.assertEqual(de_res_tgonf.data['message'], 'Objet non trouvé')

    def test_get_invalid_table(self):
        """
        A test function to check for invalid table retrieval, using assertions to verify the status code and error message.
        """
        self.assertEqual(de_res_git.status_code, 404)
        self.assertEqual(de_res_git.data['message'], 'queryset nonetype')

    def test_get_invalid_pk(self):
        """
        Test case for checking the behavior of getting an invalid primary key.
        """
        self.assertEqual(de_res_gip.status_code, 404)
        self.assertEqual(de_res_gip.data['message'], 'Objet non trouvé')

    def test_nombre_de_lignes(self):
        """
        Test the nombre_de_lignes function with assertions for status code and data value.
        """
        self.assertEqual(de_res_ndl.status_code, 200)
        self.assertEqual(de_res_ndl.data['nombre_de_lignes'], 103)

# region TestType
table = 'type'
pk = 'Pfizer'
# region test Detail
view = Detail_Table.as_view()
req = factory.get('Detail/',headers={'Authorization': API_KEY})

ty_res_tg = view(req, table=table, pk=pk)
ty_res_tg.render()
ty_json_res_tg = json.loads(ty_res_tg.content)

ty_res_tgonf = view(req, table=table, pk=None)
ty_res_tgonf.render()

ty_res_git = view(req, table="invalid_table", pk=pk)
ty_res_git.render()

ty_res_gip = view(req, table=table, pk='invalid_pk')
ty_res_gip.render()

# endregion

# region test List
view = List_Table.as_view()

req = factory.get('List/',{'table': table},headers={'Authorization': API_KEY})
ty_res_ndl = view(req)
# endregion
# endregion

class TestType(TestCase):
    def setUp(self):
        """
        Set up the test fixture. It is called before every test function to set up the test environment.
        """
        pass

    def test_get(self):
        """
        Test the get method with a specific data payload and check the equality of the response.
        """
        data = {
                    "label": "Pfizer"
                }
        self.assertEqual(ty_json_res_tg, data)

    def test_get_object_not_found(self):
        """
        Test case for checking the behavior when the object is not found.
        """
        self.assertEqual(ty_res_tgonf.status_code, 404)
        self.assertEqual(ty_res_tgonf.data['message'], 'Objet non trouvé')

    def test_get_invalid_table(self):
        """
        Function to test the retrieval of an invalid table, asserting the status code and error message.
        """
        self.assertEqual(ty_res_git.status_code, 404)
        self.assertEqual(ty_res_git.data['message'], 'queryset nonetype')

    def test_get_invalid_pk(self):
        """
        A test for getting an invalid primary key.
        """
        self.assertEqual(ty_res_gip.status_code, 404)
        self.assertEqual(ty_res_gip.data['message'], 'Objet non trouvé')

    def test_nombre_de_lignes(self):
        """
        Test the number of lines function with the expected status code and number of lines.
        """
        self.assertEqual(ty_res_ndl.status_code, 200)
        self.assertEqual(ty_res_ndl.data['nombre_de_lignes'], 5)
