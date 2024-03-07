from django.test import TestCase
from rest_framework.test import APIRequestFactory
from api.views import Detail_Table,List_Table
import json

factory = APIRequestFactory()

# region test Detail 
view = Detail_Table.as_view()
req = factory.get('Detail/')

li_res_tg = view(req, table="dose", pk='AstraZeneca_2021-06-13_84_63_Puy-de-Dôme')
li_res_tg.render()
li_json_res_tg = json.loads(li_res_tg.content)

li_res_tgonf = view(req, table="dose", pk='12345')
li_res_tgonf.render()

li_res_git = view(req, table="invalid_table", pk='12345')
li_res_git.render()

li_res_gip = view(req, table="dose", pk='invalid_pk')
li_res_gip.render()

# endregion

# region test List
view = List_Table.as_view()

req = factory.get('List/',{'table': 'Dose'})
li_res_ndl = view(req)
# endregion


class TestLicence(TestCase):
    def setUp(self):
        pass

    def test_get(self):
        data = {
                "pk_dose": "AstraZeneca_2021-06-13_84_63_Puy-de-Dôme",
                "nb_ucd": 388.0,
                "nb_dose": 3880.0,
                "Type": "AstraZeneca",
                "Date": "2021-06-13",
                "Depart": "84_63_Puy-de-Dôme"
            }
        self.assertEqual(li_json_res_tg, data)
    
    def test_get_object_not_found(self):
        self.assertEqual(li_res_tgonf.status_code, 404)
        self.assertEqual(li_res_tgonf.data['message'], 'Objet non trouvé')

    def test_get_invalid_table(self):
        self.assertEqual(li_res_git.status_code, 404)
        self.assertEqual(li_res_git.data['message'], 'queryset nonetype')

    def test_get_invalid_pk(self):
        self.assertEqual(li_res_gip.status_code, 404)
        self.assertEqual(li_res_gip.data['message'], 'Objet non trouvé')

    def test_nombre_de_lignes(self):
        self.assertEqual(li_res_ndl.status_code, 200)
        self.assertEqual(li_res_ndl.data['nombre_de_lignes'], 31766)
